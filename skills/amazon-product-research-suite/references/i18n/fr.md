# Suite de recherche produit Amazon

`amazon-product-research-suite` · Français

## Objectif et périmètre

Orienter une décision couvrant au moins deux domaines vers le minimum de Skills spécialisés ; traiter une tâche étroite directement avec son spécialiste.

## Fondements et dépendances

Hôte Agent Skills et spécialistes choisis installés. Travail hors ligne possible sur preuves fournies ; collecte en direct avec réseau et permission. Python 3.10+ pour les outils facultatifs.

## Entrées

Décision produit obligatoire ; selon besoin ASIN/identité, marché, juridiction, période et droits. Facultatifs : CSV/JSON/XLSX/PDF/images, devis et contraintes. Les inconnues restent des lacunes.

## Sorties

route-plan.json, contrat de preuves commun, Skills et ordre, entrées manquantes et destinations. L’orientation seule n’installe rien et ne contacte aucun service.

## Déroulement

1. Définir décision/périmètre
2. choisir et vérifier les Skills
3. établir route et contrat
4. exécuter seulement les étapes autorisées
5. distinguer observation/calcul/modèle/inférence/hypothèse
6. valider schémas et fichiers
7. garder les résultats partiels aux blocages.

## Limites et conditions d’arrêt

Ne pas inventer dénominateur de marché, frais, engagements fournisseurs, avis juridique ou score privé. Arrêter l’étape concernée sur CAPTCHA, accès absent, transfert sensible ou hypothèses financières insuffisantes.

## Exemple de demande

Utilise `$amazon-product-research-suite` — Évaluer un support automobile par marché, avis, différenciation, fournisseur et économie ; ajouter l’examen des dessins et modèles si des visuels existent ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Spécification complète

[Point d’entrée du Skill et références détaillées](../../SKILL.md).

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

