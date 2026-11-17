# Lieferantenmachbarkeit und Mustertests

`amazon-supplier-feasibility` · Deutsch

## Zweck und Einsatzbereich

RFQ, vergleichbare Angebote und belegte Musterabnahmen vorbereiten; standardmäßig keine Fabrik kontaktieren und nichts bestellen.

## Umsetzungsgrundlage und Abhängigkeiten

Produktspezifikation erforderlich; für Vergleiche datierte vergleichbare Angebote. Vorschriften, Musterzugang und Kommunikationsrechte bedingt. Kontakt zur Fabrik braucht gesonderte Freigabe.

## Eingaben

Spezifikation/Zeichnung mit Einheiten und Toleranzen, Mengen-/Nachfrageannahmen; bedingt Währung, Incoterm, Werkzeugbudget und Zahlungsbedingungen; optional PDF/XLSX/CSV-Angebote und Qualitätsbelege.

## Ausgaben

RFQ-Paket, Kosten-/Terminvergleich, Fertigungsrisiken und Musterplan. Status READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL oder INSUFFICIENT_EVIDENCE.

## Ablauf

1. Spezifikationslücken und Musskriterien prüfen
2. Angebotsfelder vorbereiten
3. Menge, Währung, Lieferbedingung, Leistungen und Datum angleichen
4. Werkzeuge, Kapazität, Qualität, Compliance und Logistik prüfen
5. Tests vor Mustereingang festlegen
6. Gesamtmachbarkeit vergleichen und Kosten weitergeben.

## Grenzen und Abbruchbedingungen

Unvergleichbare Angebote nicht rangieren, unbelegte Zertifikate nicht bestätigen. Kritisches Testversagen wird nicht durch niedrigen Preis ausgeglichen. Kein Senden, Verhandeln oder Bestellen ohne Erlaubnis.

## Beispielanfrage

Verwende `$amazon-supplier-feasibility` — Halterangebote erst nach Abgleich von Magnetgüte, Klebung, Drehmoment, Temperaturprüfung, Werkzeugbesitz und Verpackung vergleichen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Vollständige Spezifikation

[Skill-Einstieg und Detailreferenzen](../../SKILL.md).

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

