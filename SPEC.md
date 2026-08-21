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
