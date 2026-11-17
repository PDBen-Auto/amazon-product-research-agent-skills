# Faisabilité fournisseur et validation des échantillons

`amazon-supplier-feasibility` · Français

## Objectif et périmètre

Préparer RFQ, devis comparables et critères d’acceptation étayés ; ne pas contacter l’usine ni commander par défaut.

## Fondements et dépendances

Spécification produit obligatoire ; devis datés comparables pour classement. Conformité, accès aux échantillons et communication selon besoin. Contacter une usine exige un accord distinct.

## Entrées

Spécification/dessin avec unités et tolérances, hypothèses de quantité/demande ; conditionnels devise, Incoterm, budget outillage et paiement ; devis PDF/XLSX/CSV et preuves qualité facultatifs.

## Sorties

Dossier RFQ, comparaison coût/délai, registre des risques et plan d’échantillons. Statuts READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL ou INSUFFICIENT_EVIDENCE.

## Déroulement

1. Vérifier lacunes et exigences impératives
2. préparer champs RFQ
3. aligner quantité, devise, Incoterm, inclusions et date
4. examiner outillage/capacité/qualité/conformité/logistique
5. définir tests avant réception
6. comparer la faisabilité totale et transmettre les coûts au modèle économique.

## Limites et conditions d’arrêt

Ne pas classer des devis incomparables ni confirmer une certification sans document. Un échec critique n’est pas compensé par le prix. Aucun envoi, négociation ou achat sans autorisation.

## Exemple de demande

Utilise `$amazon-supplier-feasibility` — Aligner aimant, adhésif, couple, essai thermique, propriété de l’outillage et emballage avant de comparer des supports ; réponds en français en conservant les preuves, les inconnues et les limites d’autorisation.

## Spécification complète

[Point d’entrée du Skill et références détaillées](../../SKILL.md).

Utiliser la langue explicitement demandée, sinon celle de la demande. Conserver les commandes, identifiants de Skill, clés JSON, valeurs d’énumération, unités et citations originales. Distinguer traduction et original. Ne déduire ni pays, ni devise, ni juridiction de la langue. Lire les références détaillées utiles et maintenir tous les contrôles et autorisations existants.

Avant livraison, rapprocher entrées, preuves, valeurs manquantes, fichiers et critères d’achèvement d’origine. Marquer les étapes non exécutées comme non vérifiées ; la réussite d’un script ne valide pas une conclusion métier.

## Couverture linguistique et validation

Ce guide localisé couvre objectif, prérequis, entrées, sorties, étapes, exemples et limites. Il ne traduit pas chaque référence ligne par ligne. Les références techniques détaillées, cas historiques, erreurs de scripts, interfaces d’exemple et images restent dans leur langue originale et peuvent être expliqués à la demande. Structure, liens et contraintes essentielles sont vérifiés ; aucune relecture par un locuteur natif de chaque langue n’est revendiquée.

