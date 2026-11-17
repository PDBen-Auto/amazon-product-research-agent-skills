# Stückwirtschaftlichkeit und Erstbestellungsliquidität

`amazon-unit-economics-cashflow` · Deutsch

## Zweck und Einsatzbereich

Deckungsbeitrag, Werbe-Break-even, Retourensensitivität und Startliquidität aus ausdrücklichen Annahmen berechnen.

## Umsetzungsgrundlage und Abhängigkeiten

Numerische Preise/Kosten und belegte Marktplatzgebühren. Python 3.10+ für den Rechner ohne Drittanbieterpakete. Liquidität braucht zusätzlich Menge und Zahlungszeitpunkte.

## Eingaben

JSON: Preis, Verkaufs-/Versandgebühren, Einstandskosten, Retourenrate/-verlust, Werbe-ACOS und weitere variable Kosten. Liquidität: Menge, Werkzeuge, Einrichtung, Anzahlung und Puffer. Eine Währung, Raten zwischen0 und1.

## Ausgaben

JSON/gewählte Datei mit Beitrag/Marge, Break-even-ACOS, Retourenverlust, Erstbestellungsliquidität und Szenarien. Ungültige Eingaben erzeugen Fehlerstatus; keine Netz-/Kontoänderung.

## Ablauf

1. Annahmen, Gebührenquelle, Datum und Einheiten prüfen
2. Rechner ausführen oder Handrechnung kennzeichnen
3. Basisfall abstimmen
4. Werbung/Retouren/Kosten variieren
5. Stückgewinn und Lagerliquidität trennen und Ausschlüsse nennen.

## Grenzen und Abbruchbedingungen

Keine Gebühren, Nachfrage, Steuern, Fracht oder Zahlungsziele erfinden. Fehlender Zeitplan begrenzt das Ergebnis auf Stückrechnung. Keine Buchhaltungs-, Steuer- oder Anlageberatung.

## Beispielanfrage

Verwende `$amazon-unit-economics-cashflow` — Mit bereitgestellten Halterpreisen Retouren-/ACOS-Szenarien vergleichen und Deckungsbeitrag sowie Startliquidität getrennt ausweisen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Vollständige Spezifikation

[Skill-Einstieg und Detailreferenzen](../../SKILL.md).

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

