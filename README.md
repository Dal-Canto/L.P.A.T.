# L.P.A.T. — Linguaggio per il distacco dal telefono

Un linguaggio e runtime pensati per aiutare adolescenti (e non) a staccare dal telefono in modo sicuro, trasparente e condivisibile.

Contenuti del repository

- README.md — questa descrizione e istruzioni rapide.
- LICENSE — MIT.
- phonefree_lang.py — prototipo interprete sicuro (simulazione, non blocca app).
- grammar/phonefree.lark — grammatica Lark per il DSL (dichiarativo, non Turing-complete).
- templates/*.detox — 10 template pronti da condividere (es. 60min, focus, family_time).
- SPEC.md — specifiche di sicurezza e design per evitare che il linguaggio "incastri" gli utenti.
- assets/social_copy.md — copy e script per post virali.
- CONTRIBUTING.md, .gitignore

Uso rapido

1. Clona il repo:
   git clone https://github.com/gargoalexdc-afk/L.P.A.T.
2. Esegui un esempio (richiede Python 3.8+ e PyYAML):
   python3 phonefree_lang.py templates/60min.detox

Nota importante: il prototipo non può modificare il comportamento delle app su Android/iOS. Serve per validare la logica del DSL, la condivisione di template e la sicurezza.
