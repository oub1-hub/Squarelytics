# Importation des classes et modules nécessaires
from builtins import Exception  # Importation de la classe Exception, bien qu'elle soit déjà incluse dans Python
from django.core.management import execute_from_command_line  # Importation de la fonction pour exécuter des commandes Django
import os  # Importation du module os pour interagir avec le système d'exploitation
import sys  # Importation du module sys pour accéder aux arguments de la ligne de commande

# Fonction principale qui exécute les commandes Django
def main():
    # Définit la variable d'environnement DJANGO_SETTINGS_MODULE avec le chemin vers le fichier settings.py de votre projet
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'applicationWEB.settings')
    
    try:
        # Exécution de la commande Django en passant les arguments de la ligne de commande
        execute_from_command_line(sys.argv)
    except Exception as exc:
        # Si une exception est levée lors de l'exécution, lever une nouvelle exception avec un message personnalisé
        raise Exception("An error occurred while running manage.py") from exc

# Point d'entrée du programme, la fonction main est appelée si ce fichier est exécuté directement
if __name__ == '__main__':
    main()  # Appel de la fonction main pour lancer le processus
