import sys
import argparse
from pathlib import Path
import yaml

# Import runtime functions from the script in repo root
try:
    from phonefree_lang import validate_spec, run_session
except Exception:
    # If import fails, give a helpful message
    def validate_spec(spec):
        raise RuntimeError("Impossibile importare phonefree_lang. Assicurati di eseguire 'python -m pip install -e .' o di usare il python del venv.")
    def run_session(spec, spec_path=None):
        raise RuntimeError("Impossibile importare phonefree_lang. Installa il pacchetto in editable mode or run phonefree_lang.py directly.")


def main():
    parser = argparse.ArgumentParser(prog="lpat", description="L.P.A.T. runtime")
    parser.add_argument("file", nargs='?', help="path to .detox file (YAML)")
    args = parser.parse_args()
    if not args.file:
        parser.print_help()
        sys.exit(1)
    p = Path(args.file)
    if not p.exists():
        print(f"File non trovato: {p}")
        sys.exit(2)
    try:
        spec = yaml.safe_load(p.read_text())
        validate_spec(spec)
    except Exception as e:
        print("Errore di validazione spec:", e)
        sys.exit(2)
    run_session(spec, spec_path=str(p))


if __name__ == '__main__':
    main()
