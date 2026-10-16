# Chats Sans Familles

Première version d'une vitrine statique, faite en HTML et CSS et compatible avec GitHub Pages. Aucun serveur, framework ou script JavaScript n'est nécessaire.

## Ouvrir le site localement

Ouvrez `index.html` dans un navigateur. Dans VS Code, l'extension Live Server peut aussi servir à prévisualiser les changements, mais elle n'est pas obligatoire.

## Modifier la page

- Textes et sections : `index.html`.
- Couleurs, typographie, mise en page et responsive : `style.css`.
- Logo utilisé dans l'en-tête : `logo.jpeg`. `logo_officiel.jpeg` en est la copie de sauvegarde actuelle. Pour changer le logo plus tard, remplacer `logo.jpeg` par le nouveau visuel en gardant ce nom : le HTML n'aura pas besoin d'être modifié.
- Ancien logo noir et blanc : `logo_legacy.jpeg`.
- Visuel d'accueil : `photo-accueil.png`. Photo de présentation : `photo-presentation.jpg`. Ces fichiers sont indépendants et chacun peut être remplacé en gardant le même nom, sans modifier le HTML.
- Icône temporaire de l'onglet : `favicon.svg`. Elle pourra être remplacée par le favicon officiel si l'association en fournit un.
- Photos supplémentaires : déposer les fichiers dans `images/` et ajouter des éléments `<img>` avec un texte alternatif pertinent dans `index.html`. Utiliser uniquement des visuels dont l'association possède les droits.

## Informations à compléter avant publication

Le courriel, les numéros de téléphone officiels et la date de publication de l'article sont intégrés. Le lien Teaming fourni est intégré.

- Facebook : le lien fourni est utilisé dans l'accueil, l'adoption, les demandes de reçu fiscal, le contact et le pied de page. Les événements et collectes sont également signalés dans l'accueil.
- Adoption : la chronologie des étapes et obligations des chatons est distinguée de la note indiquant que les modalités d'adoption d'un chat adulte sont précisées au cas par cas. Elle présente la réservation avec acompte, le certificat d'engagement signé au moins 7 jours avant la cession, le départ dès 12 semaines, les options de vaccination et de test, puis la stérilisation avant 7 mois avec justificatif sous 15 jours. Le certificat d'engagement est téléchargeable depuis la page. Les contrats sont à réviser pour 2027 : intégrer le certificat au contrat de réservation et le bon de stérilisation au contrat d'adoption.
- Les options sont regroupées ainsi : dons en nature (Wishlist Amazon), dons financiers (Leetchi, Teaming, HelloAsso), puis reçu fiscal. Les liens Leetchi, HelloAsso et Amazon sont intégrés.
- La page précise que les dons financiers financent en priorité les soins vétérinaires et que les dons en nature servent à fournir nourriture et matériel.
- Parrainage : le principe et le montant de 15 € par mois sont confirmés. Les chats concernés et les modalités de parrainage restent à préciser. Les conditions de famille d'accueil restent à compléter avec l'association.
- Reçu fiscal : la demande peut se faire par message privé sur Facebook ou via le lien vers les coordonnées dans la section Contact. Le taux de 66 % et les exemples fournis sont confirmés.
- Articles Actu.fr : deux liens, titres et dates sont intégrés dans l'ordre du plus récent au plus ancien.
- Contact : le courriel `chatsansfamilles@orange.fr` utilise un lien `mailto:`. Cassandra (présidente) et Claire (secrétaire) ont chacune leur numéro affiché avec un lien `tel:`. La page Facebook permet aussi d'écrire en message privé.
- Présentation : la page indique le statut non lucratif, la date de création, le secteur et les étapes de prise en charge des chats errants communiquées par l'association.
- Numéro RNA fourni : `W272002242`, affiché dans la section « L'association ».
- Mentions légales : les coordonnées communiquées pour l'association, la responsable de publication et l'hébergement GitHub Pages figurent dans le bloc provisoire du pied de page. Faire confirmer le bloc par l'association avant la mise en ligne.
- Référencement : ajouter l'URL canonique, l'URL de l'image Open Graph et éventuellement le secteur géographique une fois le domaine et les informations officiels connus.

Les liens du menu et du pied de page sont des ancres internes vers les sections de cette page. Le menu mobile utilise l'élément HTML natif `<details>` et fonctionne sans JavaScript.

## Publier avec GitHub Pages

1. Créer un dépôt GitHub et y ajouter les fichiers du site.
2. Dans le dépôt, ouvrir **Settings > Pages**.
3. Choisir le déploiement depuis une branche, puis sélectionner la branche publiée et le dossier `/ (root)`.
4. Enregistrer et attendre la publication. GitHub Pages affichera l'adresse du site dans cette page de réglages.

L'accès à GitHub Pages dépend des paramètres du compte et du dépôt. Vérifier que le dépôt et son mode de publication conviennent à l'offre GitHub utilisée.

## Connecter un nom de domaine en `.fr`

Acheter ou utiliser un domaine auprès d'un bureau d'enregistrement, puis le renseigner dans **Settings > Pages > Custom domain**. Configurer les DNS chez le bureau d'enregistrement selon les valeurs indiquées dans la documentation GitHub Pages, attendre leur propagation, puis activer HTTPS dans les réglages Pages quand l'option est disponible. Ne pas ajouter de fichier `CNAME` tant que le nom de domaine n'a pas été choisi.