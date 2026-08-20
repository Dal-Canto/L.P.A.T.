# PowerShell script to setup venv and run LPAT
param(
  [string]$file = "templates/60min.detox"
)

if (-not (Test-Path .\venv)) {
  py -3 -m venv venv
}

try {
  .\venv\Scripts\Activate.ps1
} catch {
  Write-Host "Attenzione: non posso attivare il venv automaticamente a causa della ExecutionPolicy. Puoi eseguire manualmente: .\\venv\\Scripts\\Activate.ps1" -ForegroundColor Yellow
}

python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pyyaml

if (-not $file) {
  Write-Host "Usage: .\run.ps1 templates/60min.detox"
  exit 1
}

python -m lpat $file
