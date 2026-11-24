# Mise à jour de la galerie de parrainage

- Placez les photos des chats disponibles dans `a-parrainer/`.
- Placez les photos des chats déjà parrainés dans `parraines/`.
- Le nom de chaque fichier devient le nom affiché sur la fiche. Renommez le fichier pour corriger le nom du chat.
- Formats pris en charge : JPG, JPEG, PNG et WebP.
- Python 3 est requis ; aucun paquet supplémentaire n'est nécessaire.
- Depuis le dossier du site, lancez le script avant de publier :
	- Linux/macOS : `python3 generer_galerie_parrainage.py`
	- Windows : `py -3 generer_galerie_parrainage.py`
- Le script met à jour uniquement les cartes situées entre les marqueurs de génération dans `index.html`.

Les images d'origine dans `Fwd__Photo_mimi/` ne sont pas modifiées.
