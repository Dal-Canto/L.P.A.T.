# SPEC.md

Questo file descrive le specifiche di safety e design del linguaggio L.P.A.T. (PhoneFree) per garantire che il linguaggio non "incastri" gli utenti.

Principi chiave

- Dichiarativo: il DSL è solo un formato di dichiarazione; non può contenere codice eseguibile, network call o plugin che modifichino comportamento del dispositivo.
- Emergency obbligatoria: ogni sessione deve avere emergency.enabled: true e almeno un metodo in emergency.methods.
- Durata massima: default 24h; durate maggiori richiedono metadata.allow_long_duration: true e conferma esplicita.
- Nessun lock permanente: le modalità di lock sono soft/medium/strict ma non prevedono il blocco irreversibile.
- Validazione rigorosa: il parser rifiuta chiavi sconosciute e valori non validi.
- Trasparenza: tutto il logging è locale e esportabile; l'utente può sempre vedere cosa è stato registrato.

Enforcement mobile (nota tecnica)

- Android: usare NotificationListenerService, UsageStats, AccessibilityService o DeviceOwner per enforcement forte. Queste integrazioni vanno sviluppate nell'app mobile e non nel DSL.
- iOS: molto limitato senza MDM; favorire UX di self-control e meccaniche persuasive.

UX

- Emergency exit visibile sempre.
- Sblocco con frizione (es. delay, mini-task) invece di punizioni.
- Trusted-unlock opzionale con consenso esplicito.

Privacy

- Nessun dato inviato a server senza consenso.
- Opzione per sincronizzare template via backend solo con esplicito opt-in.

Contributi

Segui CONTRIBUTING.md per proposte di template, miglioramenti della grammatica o del runtime.
