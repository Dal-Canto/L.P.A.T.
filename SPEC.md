# 📋 Specifiche Tecniche di L.P.A.T.

## Overview

L.P.A.T. è un **Domain-Specific Language (DSL)** dichiarativo, non Turing-complete,
che permette di definire regole di digital detox in modo sicuro e trasparente.

---

## Architettura

File .detox (testo umano) ↓ Parser Lark ↓ AST (Abstract Syntax Tree) ↓ Validatore di Sicurezza ↓ Interprete Python ↓ Output JSON (per client mobile/web)


---

## Grammatica Lark

```lark
?start: program

program: "program" ":" NAME
         ("duration" ":" DURATION)?
         ("apps_blocked" ":" app_list)?
         ("reminder" ":" reminder_rule)?
         ("accountability" ":" accountability_rule)?

app_list: "[" NAME ("," NAME)* "]"

reminder_rule: "every" DURATION
               | "at" TIME

accountability_rule: "share_with" "(" NAME ("," NAME)* ")"

DURATION: /\d+min|\d+h|\d+d|all_day/
TIME: /\d{2}:\d{2}/
NAME: /[a-z_]+/

%import common.WS
%ignore WS

Feature Implementate (v0.1.0-beta)
✅ Parser completo — Legge file .detox senza errori ✅ Validazione — Controlla che app_blocked siano reali ✅ Interprete — Esegue regole e genera output JSON ✅ 10 template — Pronti da usare ✅ Logging — Tutto è registrato in chiaro

Limiti di Sicurezza
1. Non è Turing-Complete
❌ Niente while, for, if (niente logica arbitraria)
✅ Solo dichiarazioni semplici
Motivo: Non vogliamo che tu scrivi una loop infinita che ti intrappolà
2. Niente Backdoor per Genitori
✅ Tu controlli le regole, non un'azienda
✅ Niente "admin mode" nascosto
✅ Open Source: chiunque può controllare il codice
3. Transparenza Totale
✅ Tutti i file .detox sono testo umano (no "black magic")
✅ Puoi leggere esattamente cosa succede
✅ Niente encryption che nasconde le cose
Come Impedisci che mi Intrappi?
Regola 1: Duration è Limitata
# ✅ Buono
duration: 60min

# ❌ Non permesso (max 24h per volta)
duration: 999999999999h

Regola 2: Apps Sono Validate
# ✅ Buono (app reali)
apps_blocked: [instagram, tiktok]

# ❌ Non permesso (app fake)
apps_blocked: [fake_malware_app]

Regola 3: Reminders Sono Ragionevoli
# ✅ Buono
reminder: every 15min

# ❌ Non permesso (spammy)
reminder: every 1second

File di Output
Quando esegui un programma, L.P.A.T. genera:
{
  "program": "study_session",
  "status": "active",
  "apps_blocked": ["instagram", "tiktok", "youtube"],
  "duration_total": 3600,
  "duration_elapsed": 0,
  "reminders": [
    {"at": "00:15:00", "message": "Continuando forte! 💪"},
    {"at": "00:30:00", "message": "Metà strada! 🎯"}
  ],
  "accountability": ["mom", "best_friend"],
  "created_at": "2026-08-21T10:00:00Z"
}

Roadmap Tecnico
 Runtime Android (Kotlin)
 Runtime iOS (Swift)
 Web dashboard (React)
 Database cloud per template
 Integrazione con device reali (effettivo blocco app)
 Notifiche push per reminders
 Analytics (traccia il tuo progresso)
Per domande tecniche, apri un Issue.
