# Data Analysis and Visualization Tool

A lightweight Django application for analyzing and visualizing CSV data with interactive features.

## Features
- CSV file upload and parsing
- Row/column-based data access
- Statistical analysis
- Interactive matplotlib visualizations with zoom capabilities
- Real-time data exploration
- No database required - all operations in memory

## Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

## Usage
1. Upload CSV file through web interface
2. Access specific rows/columns using the index tools
3. View statistical summaries
4. Create visualizations:
   - Scatter plots
   - Line charts
   - Bar graphs
   - Histograms
   - Box plots

## Requirements
```
django>=4.2.0
pandas>=2.0.0
matplotlib>=3.7.0
numpy>=1.24.0
```

## Project Structure
```
application WEB/
├── ── applicationWEB/  #la configuration principale de projet 
│   ├── _init_.py  #Indique que ce dossier est un package Python.
│   ├── asgi.py    #Point d'entrée pour les serveurs compatibles ASGI. Utilisé pour les applications asynchrones.
│   ├── settings.py#Fichier principal de configuration de Django. Il contient les paramètres du projet 
│   ├── urls.py  # URL routing
│   └── wsgi.py  # Utilisé pour déployer l'application sur un serveur web.
|─── ── app_name/  
│   ├── models.py #Contient les définitions des modèles de base de données (tables).
    |── views.py  #Contient la logique métier. Chaque fonction ou classe représente une vue qui retourne une réponse HTTP.
    |── forms.py  #Gère les formulaires HTML, la validation des champs et le traitement des données saisies.
│   │── init__.py 
├── templates/ # HTML templates
|   |── upload.htm
|   |── visualize_date.htl
|   |── index.html
|   |── about.html  
|   |── contact.html  
├── static/    #Contient les fichiers statiques comme les CSS, images, ou JavaScript.      
|   |── css/ # CSS files
|   |── images/ #images files
|   |── js/     #js files
├── manage.py   #Il est utilisé pour exécuter des tâches administratives comme lancer le serveur
└── requirements.txt #Utile pour installer toutes les bibliothèques requises avec pip install -r requirements.txt
```

## Notes
- Data persists only during session
- Refresh page requires re-upload
- Supports numeric and text data
- Uses matplotlib for all visualizations