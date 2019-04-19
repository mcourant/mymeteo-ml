# mymeteo-ml
Init project my meteo, predict the weather for 1 week


## Datasource
Nos données proviennent de l'API open data de nantes (site: https://data.nantesmetropole.fr/pages/home/).
Depuis cette API nous pourrons récupérer les température (min, max et moyenne) pour chaque jour depuis le premier janvier 2016.

## Méthode 
Nous allons effectuer l'entrainement en utilisant les années précédent celle de la date du jour.
En comptant les jours de l'année sur un interval de 0 à 365 on obtient un modele analysable.

## Equipe
- Maxime COURANT
- Thomas PICHARD
- Matthieu SAINT-MARTIN

