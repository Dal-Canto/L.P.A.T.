import sys
import os
import traceback
from phonefree_lang import esegui_programma # Cambia con la tua funzione principale di parsing/esecuzione

def main():
    print("==================================================")
    print("      📱 L.P.A.T. - Launcher Automatico 📚       ")
    print("==================================================")
    
    # 1. Recupera il file .detox passandolo come argomento (Drag & Drop o Linea di comando)
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # 2. Fallback se l'utente fa solo doppio clic sull'eseguibile: cerca un file default
        file_path = os.path.join("templates", "60min.detox")
        
        if not os.path.exists(file_path):
            print("\n[!] Nessun file .detox specificato.")
            print("💡 Trascina un file .detox sopra questa icona per avviarlo!")
            input("\nPremi Invio per uscire...")
            return

    # 3. Verifica l'estensione del file per sicurezza
    if not file_path.endswith('.detox'):
        print(f"\n[Errore] Il file '{os.path.basename(file_path)}' non è un profilo L.P.A.T. valido (.detox).")
        input("\nPremi Invio per uscire...")
        return

    # 4. Esecuzione del file di configurazione
    try:
        print(f"\n[+] Caricamento del profilo: {os.path.basename(file_path)}")
        print("--------------------------------------------------")
        
        # Sostituisci questo blocco con la reale chiamata del tuo interprete Lark
        # Esempio: interprete.valida_ed_esegui(file_path)
        esegui_programma(file_path)
        
    except Exception as e:
        print(f"\n[❌ Errore durante il detox]: {e}")
        print("\nDettagli tecnici dell'errore:")
        traceback.print_exc()
    
    finally:
        print("\n--------------------------------------------------")
        input("Sessione terminata. Premi Invio per chiudere...")

if __name__ == "__main__":
    main()
