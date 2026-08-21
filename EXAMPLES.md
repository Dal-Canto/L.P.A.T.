# 📚 Esempi di Programmi L.P.A.T.

Qui troverai esempi reali di file `.detox` che puoi usare, modificare, o condividere.

---

## Esempio 1: Studio Concentrato (60 minuti)

**Caso d'uso**: Devo studiare matematica senza distrazioni

```detox
program: math_study
duration: 60min
apps_blocked: [instagram, tiktok, youtube, whatsapp]
reminder: every 20min
accountability: share_with(mom)
reward: gelato 🍦

Cosa fa:

Blocca 4 app per 60 minuti
Ti ricorda ogni 20 minuti che stai facendo bene
Tua mamma lo sa (puoi mandarle il file)
Dopo 60 minuti: gelato premio!
Esempio 2: Riduzione Graduale (4 settimane)
Caso d'uso: Voglio ridurre TikTok da 2 ore al giorno a 10 minuti

program: tiktok_detox
week1: 120min/day
week2: 90min/day
week3: 60min/day
week4: 30min/day
week5: 10min/day
reminder: daily_summary
accountability: share_with(best_friend, therapist)

Cosa fa:

Ogni settimana riduci il tempo su TikTok
Ricevi un riassunto ogni giorno
I tuoi amici sanno che stai facendo lo sforzo
Dopo 4 settimane: libero da TikTok addiction 🎉
Esempio 3: Family Time (Dinner 19:00-20:00)
Caso d'uso: A cena niente telefoni, vogliamo stare insieme

program: family_dinner
when: 19:00 - 20:00
who: [me, brother, sister]
apps_blocked: [all]
reward: movie_night 🎬
note: "Questo è tempo nostro, lontani dagli schermi"

Cosa fa:

Blocca TUTTE le app dalle 19:00 alle 20:00
Vale per te, tuo fratello, tua sorella
Dopo: serata film insieme
Tempo di qualità con la famiglia

Esempio 4: Morning Routine (No Phone Until 8am)
Caso d'uso: Non voglio controllare il telefono appena sveglio

program: mindful_morning
when: 06:00 - 08:00
apps_blocked: [instagram, tiktok, youtube, discord, reddit]
alarm_allowed: true
meditation: 10min
breakfast: mindful
accountability: share_with(meditation_group)

Cosa fa:

Dalle 6 alle 8 del mattino: no social
L'allarme funziona (ovvio)
10 minuti di meditazione guidata
Colazione consapevole
Il tuo gruppo di meditazione vede che sei serio

Esempio 5: Exam Season (2 Weeks Intensive)
Caso d'uso: Esami di maturità, voglio bloccare distrazioni completamente

program: exam_marathon
duration: 14days
apps_blocked: [instagram, tiktok, youtube, gaming, discord, snapchat]
reminder: every 2h "Prendi una pausa, vai al bagno, bevi acqua"
study_blocks: [2h study, 15min break] x 8/day
accountability: share_with(mom, dad, tutor)
reward: vacation 🏖️
motivation: "Tra 2 settimane Maturità finita!"

Cosa fa:

14 giorni senza niente
Ricordi di fare break ogni 2 ore
8 blocchi di 2h study + 15min break al giorno
Genitori e tutor sanno che ce la fai
Dopo: vacanza premio!
Esempio 6: Bedtime Routine (No Screen After 21:00)
Caso d'uso: Voglio dormire meglio, zero schermi prima di letto

program: good_sleep
when: 21:00 - 23:00
apps_blocked: [all]
blue_light_filter: true
reading_time: 30min
journal_time: 10min
sleep_meditation: 10min
goal: "Dormi 8 ore, svegliati felice"

Cosa fa:

Dalle 21:00 alle 23:00: tutto bloccato
Filtro luce blu attivo
30 minuti di lettura calma
10 minuti per scrivere un diario
10 minuti di meditazione per dormire
Risultato: sonno migliore = giorno migliore
Esempio 7: Weekend Challenge (24h Digital Detox)
Caso d'uso: Sabato voglio staccarmi completamente dal mondo digitale

program: digital_detox_weekend
when: Saturday 00:00 - 23:59
apps_blocked: [all_social, all_gaming, all_news]
allowed: [phone_calls, sms, emergency_apps]
activities: [hiking, cooking, reading, family_time, outdoor_sports]
reward: sunday_brunch 🥐
reflection: "Che cosa hai imparato?"
accountability: share_with(digital_detox_community)

Cosa fa:

Tutto il sabato: zero social media
Puoi ancora ricevere chiamate (importante!)
Solo attività reali: escursioni, cucina, lettura
Domenica brunch speciale
Rifletti su cosa hai imparato
La community sa che l'hai fatto
Esempio 8: Work Focus (Deep Work 4 Hours)
Caso d'uso: Sono freelancer, devo concentrarmi su progetti senza interruzioni

program: deep_work_session
duration: 4h
apps_blocked: [email, slack, discord, telegram, instagram, youtube]
notifications: disabled
pomodoro: true
breaks: every 50min for 10min
snacks: ready_on_desk
goal: "Finisci il modulo API entro le 12:00"
accountability: share_with(accountability_partner)

Cosa fa:

4 ore di lavoro puro (zero distrazioni)
Email, Slack, Discord BLOCCATI completamente
Notifiche spente
Pomodoro: 50 minuti lavoro, 10 minuti break
Snack pronti (non perdi tempo)
Obiettivo specifico e misurabile
Partner sa che stai lavorando
Esempio 9: Dopamine Detox (3 Days)
Caso d'uso: Ho abusato di piaceri istantanei, voglio resettare il cervello

program: dopamine_reset
duration: 3days
apps_blocked: [all_social, all_gaming, all_entertainment, all_news]
allowed: [water, food, exercise, sleep, meditation, nature]
activities: [walking, journaling, cold_shower, yoga]
goal: "Reset neurotransmitter levels"
note: "Questo è scienza, non punizione. Ti sentirai nuovo dopo."

Cosa fa:

3 giorni senza stimoli dopaminergici
Solo base: acqua, cibo, esercizio, sonno
Meditazione e natura
Passeggiate lunghe
Freddo (cold shower) per stimolare consapevolezza
Dopo 3 giorni: tutto sarà più interessante, meno "scrolling"
Esempio 10: Social Media Boycott (1 Month)
Caso d'uso: Voglio un mese senza social per testare come mi sento

program: social_media_boycott
duration: 30days
apps_blocked: [instagram, tiktok, facebook, snapchat, twitter, reddit, youtube]
allowed: [messaging_apps, email, news_websites]
daily_log: "Come mi sento? Che ho imparato?"
weekly_check: share_with(therapist, close_friends)
goal: "Scopri chi sei senza social media"
reward: "Decide TU cosa vuoi fare con il tempo liberato"

Cosa fa:

30 giorni ZERO social media
Puoi ancora messaggiare (amici rimangono contattabili)
Email e notizie OK
Ogni giorno scrivi come ti senti
Una volta a settimana condividi con persone di fiducia
Scoprirai cose di te che non sapevi
Il premio? Il tempo che hai libero (fai quello che vuoi!)
Come Usare Questi Esempi
Copia uno che ti piace
Modifica parametri per il TUO caso
Condividi con amici/genitori
Esegui: python3 phonefree_lang.py your_file.detox
Condividi il risultato nella community!
Vuoi Creare il Tuo?
Template vuoto per iniziare:

program: your_program_name
duration: XXmin
apps_blocked: [app1, app2]
reminder: every XXmin
accountability: share_with(person1, person2)
goal: "Descrivi il tuo obiettivo qui"

Poi apri un Issue con il tuo file .detox e lo featured come "Community Template"!

Creato con ❤️ da e per persone che vogliono vivere meglio online.
