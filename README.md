# Flask SQLite Web App

Ce projet est une application web simple développée avec Flask qui permet d'afficher des données stockées dans une base de données SQLite. Les données sont présentées sous forme de tables HTML en fonction des routes consultées.

## Fonctionnalités

- Affichage d'une page d'accueil simple.
- Consultation des données d'une table spécifique (à l'aide de routes dynamiques).
- Affichage des résultats combinés de plusieurs tables via une jointure SQL.

## Prérequis

Avant d'exécuter ce projet, assurez-vous que votre environnement satisfait les conditions suivantes :

- Python 3.6 ou version supérieure
- Flask (peut être installé via pip)
- Une base de données SQLite nommée `data.db` contenant les tables suivantes :
  - `customer`
  - `customer_order`
  - `order_detail`
  - `product`

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DEPOT>
   ```

2. Installez les dépendances nécessaires :

   ```bash
   pip install flask
   ```

3. Assurez-vous que le fichier `data.db` existe dans le répertoire racine.

## Structure du projet

Voici un aperçu de la structure du projet :

```
/
├── app.py                 # Code principal de l'application Flask
├── templates/
│   └── simple_page.html   # Modèle HTML pour afficher les résultats
├── static/                # Dossier pour les fichiers statiques (CSS, JS, etc.)
├── data.db                # Base de données SQLite
└── README.md              # Documentation du projet
```

## Utilisation

1. Lancez l'application Flask :

   ```bash
   python app.py
   ```

2. Ouvrez un navigateur web et accédez à l'adresse suivante :

   - Page d'accueil : `http://127.0.0.1:5000/`
   - Affichage des données d'une table spécifique : `http://127.0.0.1:5000/table/<nom_de_la_table>`
     - Exemple : `http://127.0.0.1:5000/table/customer`
   - Affichage des données combinées de toutes les tables : `http://127.0.0.1:5000/table/all`

## Détails Techniques

### Routes

#### Page d'accueil : `/`
Affiche une page simple basée sur le modèle `simple_page.html`.

#### Route dynamique : `/table/<name>`
Affiche les 50 premières entrées de la table SQLite spécifiée par `name`.

- Gère les tables suivantes :
  - `customer` (colonnes : `id`, `country`)
  - `customer_order` (colonnes : `id`, `invoice_nb`, `invoice_date`, `customer_id`)
  - `order_detail` (colonnes : `id`, `quantity`, `order_id`, `product_id`)
  - `product` (colonnes : `id`, `description`, `price`)

#### Route combinée : `/table/all`
Effectue une jointure sur toutes les tables et affiche les 50 premières entrées combinées.

### Exemple de Jointure SQL

La route `/table/all` utilise la requête suivante pour combiner les données :

```sql
SELECT * FROM customer as t1 
INNER JOIN customer_order as t2 ON t1.id = t2.customer_id
INNER JOIN order_detail as t3 ON t2.id = t3.order_id
INNER JOIN product as t4 ON t4.id = t3.product_id
LIMIT 50
```

## Modèle HTML

Le fichier `simple_page.html` affiche dynamiquement les résultats sous forme de table, avec les colonnes et les données correspondantes.

## Améliorations possibles

- Ajouter des validations pour les noms de table dans la route `/table/<name>`.
- Implémenter une pagination pour les résultats des requêtes SQL.
- Ajouter des tests unitaires pour valider les fonctionnalités.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.
