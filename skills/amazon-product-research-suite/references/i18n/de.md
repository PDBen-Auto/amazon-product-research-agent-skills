# Amazon-Produktrecherche-Suite

`amazon-product-research-suite` · Deutsch

## Zweck und Einsatzbereich

Bereichsübergreifende Entscheidungen mit mindestens zwei Belegdomänen an möglichst wenige passende Spezial-Skills leiten; enge Einzelaufgaben direkt behandeln.

## Umsetzungsgrundlage und Abhängigkeiten

Agent-Skills-Host und ausgewählte installierte Spezialisten. Vorhandene Belege erlauben Offlinearbeit, Live-Recherche braucht Netz und Berechtigung. Python 3.10+ für optionale Hilfsprogramme.

## Eingaben

Produktentscheidung erforderlich; je nach Aufgabe ASIN/Identität, Marktplatz, Rechtsordnung, Zeitraum und Rechte. Optional CSV/JSON/XLSX/PDF/Bilder, Angebote und Geschäftsgrenzen. Fehlendes bleibt eine Lücke.

## Ausgaben

route-plan.json, gemeinsamer Belegvertrag, Skills und Reihenfolge, fehlende Eingaben und Ausgabeziele. Routing installiert nichts und kontaktiert keinen Dienst.

## Ablauf

1. Entscheidung und Umfang definieren
2. Skills und Verfügbarkeit prüfen
3. Route und Belegvertrag erstellen
4. nur erlaubte Schritte ausführen
5. beobachtet/berechnet/modelliert/abgeleitet/angenommen unterscheiden
6. Übergabeschemas und Dateien prüfen
7. Teilergebnisse bei Blockern erhalten.

## Grenzen und Abbruchbedingungen

Keine erfundenen Marktgrößen, Gebühren, Lieferantenzusagen, Rechtsurteile oder privaten Scores. Bei CAPTCHA, fehlendem Zugang, sensibler Übertragung oder Finanzannahmen den betroffenen Schritt stoppen.

## Beispielanfrage

Verwende `$amazon-product-research-suite` — Einen Autohalter über Markt, Rezensionen, Differenzierung, Lieferbarkeit und Wirtschaftlichkeit prüfen; bei Bildern eine Designrechtsprüfung ergänzen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Vollständige Spezifikation

[Skill-Einstieg und Detailreferenzen](../../SKILL.md).

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

