# Suite de recherche produit Amazon

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

## Installation et utilisation

Télécharger ou cloner le dépôt, puis copier le répertoire du Skill indiqué, avec ses references, scripts, assets et autres dépendances existantes, dans le répertoire de Skills de l’hôte. Conserver son nom et SKILL.md. Changer la langue de documentation ne demande pas de nouvelle installation. Les commandes proposées ne prouvent ni installation ni activation.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## Différenciation produit fondée sur les preuves

`amazon-product-differentiation-rd`

Transformer les difficultés clients en mécanismes produit, spécifications mesurables, expériences peu coûteuses et critères d’abandon prédéfinis.

Répertoire du Skill: `skills/amazon-product-differentiation-rd`

**Fondements et dépendances**

Preuves clients traçables, produit de référence et tâche utilisateur. Contraintes métier pour faisabilité ; prototype et revues brevet/fournisseur selon besoin. Aucun service en direct avec preuves fournies.

**Entrées**

Obligatoires : avis/entretiens/retours, images ou spécifications de référence, tâche principale. Conditionnels : prix, coût, dimensions, matériaux, compatibilité, MOQ, conformité. Seuils proposés étiquetés hypothèses.

**Sorties**

Carte preuve-mécanisme, portefeuille de concepts, spécifications, protocoles expérimentaux et risques ouverts en Markdown/JSON/tableau. Chaque recommandation relie preuve, mécanisme, exigence et test.

[Déroulement · Limites et conditions d’arrêt · Exemple de demande](skills/amazon-product-differentiation-rd/references/i18n/fr.md)

> Utilise `$amazon-product-differentiation-rd` — Pour un support qui glisse, définir maintien, force de libération, masse du téléphone, vibration et température plutôt qu’un simple aimant renforcé ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Suite de recherche produit Amazon

`amazon-product-research-suite`

Orienter une décision couvrant au moins deux domaines vers le minimum de Skills spécialisés ; traiter une tâche étroite directement avec son spécialiste.

Répertoire du Skill: `skills/amazon-product-research-suite`

**Fondements et dépendances**

Hôte Agent Skills et spécialistes choisis installés. Travail hors ligne possible sur preuves fournies ; collecte en direct avec réseau et permission. Python 3.10+ pour les outils facultatifs.

**Entrées**

Décision produit obligatoire ; selon besoin ASIN/identité, marché, juridiction, période et droits. Facultatifs : CSV/JSON/XLSX/PDF/images, devis et contraintes. Les inconnues restent des lacunes.

**Sorties**

route-plan.json, contrat de preuves commun, Skills et ordre, entrées manquantes et destinations. L’orientation seule n’installe rien et ne contacte aucun service.

[Déroulement · Limites et conditions d’arrêt · Exemple de demande](skills/amazon-product-research-suite/references/i18n/fr.md)

> Utilise `$amazon-product-research-suite` — Évaluer un support automobile par marché, avis, différenciation, fournisseur et économie ; ajouter l’examen des dessins et modèles si des visuels existent ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Faisabilité fournisseur et validation des échantillons

`amazon-supplier-feasibility`

Préparer RFQ, devis comparables et critères d’acceptation étayés ; ne pas contacter l’usine ni commander par défaut.

Répertoire du Skill: `skills/amazon-supplier-feasibility`

**Fondements et dépendances**

Spécification produit obligatoire ; devis datés comparables pour classement. Conformité, accès aux échantillons et communication selon besoin. Contacter une usine exige un accord distinct.

**Entrées**

Spécification/dessin avec unités et tolérances, hypothèses de quantité/demande ; conditionnels devise, Incoterm, budget outillage et paiement ; devis PDF/XLSX/CSV et preuves qualité facultatifs.

**Sorties**

Dossier RFQ, comparaison coût/délai, registre des risques et plan d’échantillons. Statuts READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL ou INSUFFICIENT_EVIDENCE.

[Déroulement · Limites et conditions d’arrêt · Exemple de demande](skills/amazon-supplier-feasibility/references/i18n/fr.md)

> Utilise `$amazon-supplier-feasibility` — Aligner aimant, adhésif, couple, essai thermique, propriété de l’outillage et emballage avant de comparer des supports ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Économie unitaire et trésorerie initiale

`amazon-unit-economics-cashflow`

Calculer marge contributive, ACOS d’équilibre, sensibilité aux retours et trésorerie de première commande à partir d’hypothèses explicites.

Répertoire du Skill: `skills/amazon-unit-economics-cashflow`

**Fondements et dépendances**

Prix/coûts numériques et frais de plateforme documentés. Python 3.10+ pour le calculateur sans dépendance tierce. Trésorerie : quantités et calendrier de paiement supplémentaires.

**Entrées**

JSON : prix, commission, exécution, coût rendu, taux/perte de retour, ACOS et autres coûts variables. Trésorerie : quantité, outillage, démarrage, acompte et réserve. Une devise ; taux de0 à1.

**Sorties**

JSON/fichier choisi : contribution/marge, ACOS d’équilibre, perte attendue, trésorerie initiale et scénarios. Entrée invalide : code non nul ; aucune opération réseau/compte.

[Déroulement · Limites et conditions d’arrêt · Exemple de demande](skills/amazon-unit-economics-cashflow/references/i18n/fr.md)

> Utilise `$amazon-unit-economics-cashflow` — Avec prix/coûts fournis, comparer retours et ACOS d’un support et afficher séparément contribution et trésorerie initiale ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.
