# Prompt de reconstruction du site

Crée ou reconstruis le site vitrine statique de l'association Chats sans Familles. Si le projet existe déjà, inspecte ses fichiers et réutilise les éléments disponibles au lieu de repartir de zéro.

## But et contraintes

Le site doit présenter l'association et orienter les visiteurs vers l'adoption, les dons, les articles et les contacts. Facebook reste le lieu principal des annonces et de la vie quotidienne de l'association ; le site est une vitrine complémentaire.

- Utiliser HTML5 et CSS3 simples, sans framework, backend, base de données, CMS ni dépendance inutile.
- N'ajouter du JavaScript que si une fonctionnalité l'exige réellement.
- Assurer la compatibilité avec GitHub Pages et l'affichage mobile sans défilement horizontal.
- Utiliser des chemins relatifs pour les images, styles et liens internes.
- Respecter l'accessibilité : HTML sémantique, `lang="fr"`, titres hiérarchisés, textes alternatifs pertinents, focus visible et liens clairs.
- Ne pas inventer d'informations sur l'association.

## Identité et informations confirmées

Écrire le nom officiel exactement : **Chats sans Familles**.

Chats sans Familles est une association à but non lucratif, créée le 9 novembre 2015. Son numéro RNA est `W272002242`. Elle intervient dans le secteur de Beuzeville et de Pont-Audemer, dans l'Eure. Elle sauve les chats errants, leur apporte les premiers soins vétérinaires, les fait stériliser, les place en famille d'accueil puis les fait adopter afin qu'ils puissent vivre dans la joie et en bonne santé.

Ne pas inventer d'adresse postale, de statistiques, de témoignages, de date, de partenaire ou de coordonnées supplémentaires.

## Images disponibles

- `logo.jpeg` : logo utilisé dans l'en-tête.
- `logo_officiel.jpeg` : copie de sauvegarde du logo.
- `logo_legacy.jpeg` : ancien logo, ne pas utiliser comme logo courant.
- `photo-accueil.png` : visuel principal de l'accueil.
- `photo-presentation.jpg` : photo de présentation montrant deux chats blottis l'un contre l'autre.
- `favicon.svg` : favicon actuelle.

Ne pas remplacer ces fichiers par des images Internet. Afficher les visuels sans cadre rose ni recadrage qui couperait le sujet. Utiliser des textes alternatifs qui décrivent fidèlement chaque image.

## Direction visuelle

Créer une vitrine chaleureuse, soignée, humaine et facile à lire. S'inspirer de la palette de l'infographie du reçu fiscal : fond crème, vert sauge modéré, rose en accent et texte sombre. Garder le vert minoritaire et éviter les grands aplats verts. Ne pas ajouter de cadre rose autour des photos. Les cartes de Contact doivent toutes suivre le même format.

## Structure de la page

Créer une page unique avec les sections et ancres suivantes : Accueil, L'association, Adopter, Nous soutenir, Actualités, Contact et pied de page. Prévoir une navigation desktop et un menu compact mobile, utilisable au clavier.

### Accueil

- Afficher le secteur « Eure · Beuzeville / Pont-Audemer ».
- H1 : « Chats sans Familles ».
- Phrase : « Sauver les chats errants, les soigner, les stériliser et les accompagner vers une famille. »
- Utiliser `photo-accueil.png` sans cadre coloré.
- Boutons « Découvrir l'adoption » et « Nous soutenir ».
- Ne pas afficher de numéro décoratif comme « 01 ».

### L'association

Présenter ces informations sans les déformer :

« Créée le 9 novembre 2015, Chats sans Familles est une association à but non lucratif qui sauve les chats errants du secteur de Beuzeville et de Pont-Audemer, dans l'Eure. Elle leur apporte les premiers soins vétérinaires, les fait stériliser, puis les place en famille d'accueil avant de les faire adopter. Son souhait : qu'ils puissent vivre leur vie dans la joie et en bonne santé. »

Afficher également : « Identifiant RNA : W272002242 ».
Utiliser `photo-presentation.jpg` sans la recadrer.

### Adopter

Expliquer que les chats à adopter sont présentés principalement sur Facebook. Ajouter un lien visible « Voir les chats à adopter » vers :

`https://www.facebook.com/share/1LhmT93sBK/`

Ne pas recopier ni inventer d'annonces d'adoption. Ne pas ajouter de repère « 01 » à gauche de cette section.

### Nous soutenir

Présenter quatre cartes dans cet ordre, sans lettres ou numéros décoratifs :

1. Leetchi — « Soutenir sur Leetchi » :
   `https://www.leetchi.com/fr/c/soutien-aux-chats-sans-famille-2013675?u=d46b979b-0b80-43e3-bbbd-5d1c2c670728&utm_source=copylink&utm_medium=social_sharing&fbclid=IwdGRjcAUzRRJjbGNrBLXwoGV4dG4DYWVtAjExAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHqJikDpVY8LvuYmvM7QxL86hH-DW_U8w7nQ44wbdVqr27IcKcKDSiTfflqyy_aem_ZUcAYzZMm82dqfqg9fTywg`
2. HelloAsso — « Faire un don sur HelloAsso » :
   `https://www.helloasso.com/associations/association-chats-sans-familles/formulaires/1`
3. Dons en nature — Wishlist Amazon, « Consulter la wishlist » :
   `https://www.amazon.fr/hz/wishlist/ls/3J3U32HWTZ4PF?ref_=wl_share&fbclid=IwdGRjcAUzRb1jbGNrBTNFuGV4dG4DYWVtAjExAHBkb2YBc3J0YwZhcHBfaWQMMzUwNjg1NTMxNzI4AAEeogpzB4S8UrX8AmMQwpSfRnZc18elcb5h91hK3DOHGZk-wLNExHP9L8lhN70_aem_1a_0dNkC78nRrFQLbYybgg`
4. Demande de reçu fiscal, dans une carte au même niveau :

   « Vous souhaitez obtenir un reçu fiscal pour votre don ? Contactez-nous par message privé sur Facebook ou directement via nos coordonnées, et nous nous en chargerons. »

   Lier « message privé sur Facebook » à la page Facebook ci-dessus et « coordonnées » à `#contact`. Afficher les exemples fournis : 10 € → 6,60 €, 20 € → 13,20 €, 50 € → 33 €, 100 € → 66 €. Indiquer que 66 % du don peut être déduit, sans présenter cela comme une garantie ; rappeler que le taux doit être vérifié avant publication.

Ouvrir les liens externes dans un nouvel onglet avec `rel="noopener noreferrer"`.

### Actualités

Prévoir un seul article :
- Titre : « 150 chatons recueillis en un an : un record affligeant pour cette association animalière de l'Eure »
- Média : Actu.fr
- Date : à compléter
- Lien :
  `https://actu.fr/normandie/foulbec_27260/150-chatons-recueillis-en-un-an-un-record-affligeant-pour-cette-association-animaliere-de-leure_64696677.html?at_content=photo&at_term=eveil.pontaudemer&at_campaign=facebook&at_medium=Social&at_source=nonli&fbclid=IwVERTSAT5E0pwZG9mAWV4dG4DYWVtAjEwAHNydGMGYXBwX2lkDDM1MDY4NTUzMTcyOAABHnyzyuEVRDCbdX4dM_V0bLdDAdvD1ssMSi0uzGcARVI-xPBda-QLYnS16u_J_aem_Qe064xf0qACyU2fCGpfY7g`

Ne pas ajouter d'autres articles ni inventer de date. Ne pas afficher de numéro « 01 » à gauche de l'article.

### Contact

Présenter les coordonnées sous forme de cartes identiques et cliquables :
- E-mail : `chatsansfamilles@orange.fr`, lien `mailto:chatsansfamilles@orange.fr`.
- Cassandra — Présidente de l'association : `+33 6 03 69 48 42`, lien `tel:+33603694842`.
- Claire — Secrétaire de l'association : `+33 6 29 36 99 68`, lien `tel:+33629369968`.
- Facebook : « Écrivez-nous en message privé », vers `https://www.facebook.com/share/1LhmT93sBK/`.

Titre de section : « Une question ? Contactez-nous. »

### Pied de page

Afficher le nom « Chats sans Familles », la phrase « Aux côtés des chats errants, autour de Beuzeville et Pont-Audemer. », ainsi que Facebook et les ancres Adoption, Nous soutenir, Actualités et Contact. Garder un emplacement pour les mentions légales sans en inventer le contenu.

## README et vérifications

Rédiger ou mettre à jour un README en français : ouverture locale, modification des textes, remplacement des images et liens, coordonnées, publication GitHub Pages et connexion ultérieure d'un domaine `.fr`.

Vérifier le HTML/CSS, les liens internes, les images, le menu clavier/mobile, les liens `mailto:` et `tel:`, les largeurs mobile et desktop, et l'absence de défilement horizontal. Ne pas ouvrir ni suivre les liens externes pendant les vérifications.