#!/usr/bin/env python3
"""
PhoneFree DSL runtime (prototipo sicuro).
- Legge un file YAML/JSON con la definizione della sessione.
- Applica VALIDAZIONI di sicurezza prima di eseguire (emergency obbligatoria, durata massima, nessun codice eseguibile).
- Simulazione: non tenta di bloccare app su Android/iOS; serve per validare la logica e per generare sessioni sicure.
Uso:
  python phonefree_lang.py session.detox
Durante l'esecuzione puoi scrivere su stdin:
  open:<appname>    -> simula apertura app
  notify:<text>     -> simula notifica
  emergency         -> simula richiesta d'emergenza (uscita immediata)
  unlock            -> prova sblocco (se configurata con frizione)
  quit              -> termina sessione manualmente
"""
import sys
import time
import threading
import yaml
import json
from pathlib import Path

MAX_DURATION_SECONDS = 24 * 3600  # 24 ore massimo di default

ALLOWED_KEYS = {
    'name', 'duration', 'mode', 'allow_apps', 'block_notifications', 'on_violation',
    'emergency', 'metadata', 'share'
}


def parse_duration(s):
    if isinstance(s, int):
        return s
    if s is None:
        return 0
    s = str(s).strip()
    if s.endswith('m'):
        return int(s[:-1]) * 60
    if s.endswith('h'):
        return int(s[:-1]) * 3600
    if s.endswith('s'):
        return int(s[:-1])
    return int(s)


def validate_spec(spec):
    # chiavi sconosciute
    unknown = set(spec.keys()) - ALLOWED_KEYS
    if unknown:
        raise ValueError(f"Spec contiene chiavi non permesse: {unknown}")

    # emergency obbligatoria
    em = spec.get('emergency')
    if not em or not isinstance(em, dict):
        raise ValueError("Spec invalida: campo 'emergency' obbligatorio e deve essere un oggetto.")
    if not em.get('enabled', False):
        raise ValueError("Emergency deve essere abilitata (emergency.enabled: true).")
    methods = em.get('methods') or []
    if not methods:
        raise ValueError("Emergency deve specificare almeno un metodo in emergency.methods (es. ['call_112'] o ['trusted_contact:+391234567']).")

    # durata
    duration_s = parse_duration(spec.get('duration', '0m'))
    if duration_s <= 0:
        raise ValueError("Duration deve essere > 0.")
    if duration_s > MAX_DURATION_SECONDS and not spec.get('metadata', {}).get('allow_long_duration', False):
        raise ValueError(f"Duration eccede il limite massimo di {MAX_DURATION_SECONDS} secondi (24h). Per superare, aggiungi metadata.allow_long_duration: true con consenso esplicito.")

    # mode
    mode = spec.get('mode','soft')
    if mode not in ('soft','medium','strict'):
        raise ValueError("Mode deve essere 'soft', 'medium' o 'strict'. Non sono permesse modalità di lock permanente.")

    # allow_apps
    allow_apps = spec.get('allow_apps', [])
    if not isinstance(allow_apps, list):
        raise ValueError("allow_apps deve essere una lista.")
    # assicuriamo che almeno un metodo di comunicazione d'emergenza sia permesso (telefono)
    emergency_phone_allowed = any(m.startswith('call_') for m in methods)
    if emergency_phone_allowed and 'phone' not in allow_apps and 'call' not in allow_apps:
        # non forziamo ma segnaliamo: per sicurezza è meglio che phone sia permessa
        print("ATTENZIONE: hai dichiarato metodo di emergenza telefonico ma 'phone' non è in allow_apps. Il runtime prototipo non bloccherà le chiamate d'emergenza; nell'app reale assicurati che le chiamate siano consentite.")

    return True


def run_session(spec, spec_path=None):
    name = spec.get('name','session')
    duration_s = parse_duration(spec.get('duration','0m'))
    allow_apps = set(spec.get('allow_apps', []))
    block_notifications = bool(spec.get('block_notifications', False))
    on_violation = spec.get('on_violation', {})
    emergency = spec.get('emergency', {})
    mode = spec.get('mode','soft')

    print(f"VALIDAZIONE completata. Avvio sessione '{name}' ({mode}) durata {duration_s}s")
    print("EMERGENCY methods:", emergency.get('methods'))
    end_time = time.time() + duration_s
    violations = []

    def ticker():
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            print(f"[{name}] rimangono {remaining}s", end='\r')
            time.sleep(1)
        print()

    t = threading.Thread(target=ticker, daemon=True)
    t.start()

    session_logs = []
    # Simula eventi da stdin
    while time.time() < end_time:
        try:
            line = sys.stdin.readline()
            if not line:
                time.sleep(0.1)
                continue
            line = line.strip()
            if not line:
                continue
            if line == 'quit':
                print("Sessione interrotta dall'utente (quit).")
                session_logs.append({'event':'quit','time':time.time()})
                break
            if line == 'emergency':
                print("EMERGENCY invoked: esco immediatamente dalla sessione (simulazione).")
                session_logs.append({'event':'emergency','time':time.time()})
                # scriviamo un log di uscita per audit locale
                Path(f"{name}_emergency_exit.json").write_text(json.dumps({'session': name, 'time': time.time(), 'reason': 'emergency_command'}))
                break
            if line.startswith('open:'):
                app = line.split(':',1)[1]
                session_logs.append({'event':'open','app':app,'time':time.time()})
                if app not in allow_apps:
                    print(f"VIOLAZIONE: apertura app non permessa: {app}")
                    violations.append(('open', app, time.time()))
                    # comportamento "gentile" dipende da mode
                    if mode == 'soft':
                        print("Warn: prova a non aprire app non permesse.")
                    elif mode == 'medium':
                        print("Medium: aggiunta frizione (simulazione).")
                    else:
                        print("Strict: registrata violazione; in app reale possibile escalation.")
                else:
                    print(f"Apertura app permessa: {app}")
            elif line.startswith('notify:'):
                content = line.split(':',1)[1]
                session_logs.append({'event':'notify','content':content,'time':time.time()})
                if block_notifications:
                    print(f"Notifica bloccata: {content}")
                else:
                    print(f"Notifica mostrata: {content}")
            elif line == 'unlock':
                # Simulazione di frizione: delay + task
                print("Richiesta sblocco: avvio frizione (simulazione 10s). Completa un piccolo task per sbloccare.")
                for i in range(10,0,-1):
                    print(f"Attendi {i}s...", end='\r'); time.sleep(1)
                print("\nSblocco consentito (simulazione).")
                session_logs.append({'event':'unlock','time':time.time()})
                # log sblocco
                Path(f"{name}_unlock.json").write_text(json.dumps({'session': name, 'time': time.time(), 'method': 'unlock_task'}))
                break
            else:
                print("Comando non riconosciuto. Usa open:<app>, notify:<text>, emergency, unlock, quit")
        except KeyboardInterrupt:
            print("Interrotto da KeyboardInterrupt.")
            session_logs.append({'event':'keyboard_interrupt','time':time.time()})
            break

    # fine sessione - riepilogo
    if violations:
        first_violation_time = violations[0][2]
        print(f"Sessione '{name}' terminata con {len(violations)} violazioni.")
    else:
        print(f"Sessione '{name}' completata senza violazioni.")
    # scrive log sessione locale
    summary = {
        'session': name,
        'duration_requested': duration_s,
        'mode': mode,
        'violations': len(violations),
        'events': session_logs,
        'timestamp_end': time.time()
    }
    Path(f"{name}_summary.json").write_text(json.dumps(summary, indent=2))
    if spec_path:
        print(f"Summary salvato in {name}_summary.json (origine: {spec_path})")
    else:
        print(f"Summary salvato in {name}_summary.json")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: phonefree_lang.py session.detox")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File non trovato: {path}")
        sys.exit(1)
    try:
        spec = yaml.safe_load(path.read_text())
        validate_spec(spec)
    except Exception as e:
        print("Errore di validazione spec:", e)
        sys.exit(2)
    run_session(spec, spec_path=str(path))
