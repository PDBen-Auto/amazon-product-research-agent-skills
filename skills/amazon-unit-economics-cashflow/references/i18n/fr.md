# Économie unitaire et trésorerie initiale

`amazon-unit-economics-cashflow` · Français

## Objectif et périmètre

Calculer marge contributive, ACOS d’équilibre, sensibilité aux retours et trésorerie de première commande à partir d’hypothèses explicites.

## Fondements et dépendances

Prix/coûts numériques et frais de plateforme documentés. Python 3.10+ pour le calculateur sans dépendance tierce. Trésorerie : quantités et calendrier de paiement supplémentaires.

## Entrées

JSON : prix, commission, exécution, coût rendu, taux/perte de retour, ACOS et autres coûts variables. Trésorerie : quantité, outillage, démarrage, acompte et réserve. Une devise ; taux de0 à1.

## Sorties

JSON/fichier choisi : contribution/marge, ACOS d’équilibre, perte attendue, trésorerie initiale et scénarios. Entrée invalide : code non nul ; aucune opération réseau/compte.

## Déroulement

1. Valider hypothèses, source des frais, date et unités
2. exécuter le calculateur ou déclarer le calcul manuel
3. rapprocher le cas de base
4. varier publicité/retours/coûts
5. séparer bénéfice unitaire et trésorerie de stock, expliciter les exclusions.

## Limites et conditions d’arrêt

Ne pas inventer frais, demande, taxes, transport ou conditions. Sans calendrier, limiter à l’unitaire. Ce modèle n’est pas un conseil comptable, fiscal ou d’investissement.

## Exemple de demande

Utilise `$amazon-unit-economics-cashflow` — Avec prix/coûts fournis, comparer retours et ACOS d’un support et afficher séparément contribution et trésorerie initiale ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Spécification complète

[Point d’entrée du Skill et références détaillées](../../SKILL.md).

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

