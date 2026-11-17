# Amazon-Produktrecherche-Suite

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

Die ausdrücklich gewünschte Ausgabesprache verwenden, sonst der Sprache der Anfrage folgen. Befehle, Skill-IDs, JSON-Schlüssel, Enumerationswerte, Einheiten und Originalzitate unverändert lassen. Übersetzungen kennzeichnen. Land, Währung und Rechtsordnung nicht aus der Sprache ableiten. Relevante Detailreferenzen lesen und sämtliche bestehenden Prüfungen und Berechtigungsgrenzen einhalten.

## Installation und Nutzung

Das Repository herunterladen oder klonen und das angegebene Skill-Verzeichnis mit seinen vorhandenen references, scripts, assets und weiteren Abhängigkeiten in das Skill-Verzeichnis des Hosts kopieren. Name und SKILL.md beibehalten. Ein Sprachwechsel erfordert keine weitere Installation. Installationsbefehle sind Optionen und kein Nachweis einer Installation oder Aktivierung.

```sh
git clone https://github.com/PDBen-Auto/amazon-product-research-agent-skills.git
```

## Beleggestützte Produktdifferenzierung

`amazon-product-differentiation-rd`

Kundenprobleme in Wirkmechanismen, messbare Spezifikationen, günstige Experimente und vorab definierte Abbruchkriterien übersetzen.

Skill-Verzeichnis: `skills/amazon-product-differentiation-rd`

**Umsetzungsgrundlage und Abhängigkeiten**

Nachvollziehbare Kundenbelege, Ausgangsprodukt und zentrale Nutzeraufgabe. Geschäftsgrenzen für Machbarkeit; Prototypen sowie Patent-/Lieferantenprüfung bei Bedarf. Kein Live-Dienst bei bereitgestellten Belegen nötig.

**Eingaben**

Pflicht: Rezensionen/Interviews/Retourenbelege, Produktbilder oder Spezifikation und Nutzeraufgabe. Bedingt Preis, Kosten, Abmessungen, Material, Passform, MOQ und Vorschriften. Vorgeschlagene Schwellen als Annahmen markieren.

**Ausgaben**

Beleg-Mechanismus-Matrix, Konzeptvergleich, messbare Anforderungen, Versuchspläne und offene Risiken als Markdown/JSON/Tabelle. Jede Empfehlung braucht Beleg, Mechanismus, Anforderung und Test.

[Ablauf · Grenzen und Abbruchbedingungen · Beispielanfrage](skills/amazon-product-differentiation-rd/references/i18n/de.md)

> Verwende `$amazon-product-differentiation-rd` — Bei rutschenden Haltern Halte-/Lösekraft, Telefongewicht sowie Vibrations- und Temperaturtests spezifizieren statt nur stärkere Magnete zu fordern; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Amazon-Produktrecherche-Suite

`amazon-product-research-suite`

Bereichsübergreifende Entscheidungen mit mindestens zwei Belegdomänen an möglichst wenige passende Spezial-Skills leiten; enge Einzelaufgaben direkt behandeln.

Skill-Verzeichnis: `skills/amazon-product-research-suite`

**Umsetzungsgrundlage und Abhängigkeiten**

Agent-Skills-Host und ausgewählte installierte Spezialisten. Vorhandene Belege erlauben Offlinearbeit, Live-Recherche braucht Netz und Berechtigung. Python 3.10+ für optionale Hilfsprogramme.

**Eingaben**

Produktentscheidung erforderlich; je nach Aufgabe ASIN/Identität, Marktplatz, Rechtsordnung, Zeitraum und Rechte. Optional CSV/JSON/XLSX/PDF/Bilder, Angebote und Geschäftsgrenzen. Fehlendes bleibt eine Lücke.

**Ausgaben**

route-plan.json, gemeinsamer Belegvertrag, Skills und Reihenfolge, fehlende Eingaben und Ausgabeziele. Routing installiert nichts und kontaktiert keinen Dienst.

[Ablauf · Grenzen und Abbruchbedingungen · Beispielanfrage](skills/amazon-product-research-suite/references/i18n/de.md)

> Verwende `$amazon-product-research-suite` — Einen Autohalter über Markt, Rezensionen, Differenzierung, Lieferbarkeit und Wirtschaftlichkeit prüfen; bei Bildern eine Designrechtsprüfung ergänzen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Lieferantenmachbarkeit und Mustertests

`amazon-supplier-feasibility`

RFQ, vergleichbare Angebote und belegte Musterabnahmen vorbereiten; standardmäßig keine Fabrik kontaktieren und nichts bestellen.

Skill-Verzeichnis: `skills/amazon-supplier-feasibility`

**Umsetzungsgrundlage und Abhängigkeiten**

Produktspezifikation erforderlich; für Vergleiche datierte vergleichbare Angebote. Vorschriften, Musterzugang und Kommunikationsrechte bedingt. Kontakt zur Fabrik braucht gesonderte Freigabe.

**Eingaben**

Spezifikation/Zeichnung mit Einheiten und Toleranzen, Mengen-/Nachfrageannahmen; bedingt Währung, Incoterm, Werkzeugbudget und Zahlungsbedingungen; optional PDF/XLSX/CSV-Angebote und Qualitätsbelege.

**Ausgaben**

RFQ-Paket, Kosten-/Terminvergleich, Fertigungsrisiken und Musterplan. Status READY_FOR_RFQ, READY_FOR_SAMPLE, CONDITIONAL oder INSUFFICIENT_EVIDENCE.

[Ablauf · Grenzen und Abbruchbedingungen · Beispielanfrage](skills/amazon-supplier-feasibility/references/i18n/de.md)

> Verwende `$amazon-supplier-feasibility` — Halterangebote erst nach Abgleich von Magnetgüte, Klebung, Drehmoment, Temperaturprüfung, Werkzeugbesitz und Verpackung vergleichen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Stückwirtschaftlichkeit und Erstbestellungsliquidität

`amazon-unit-economics-cashflow`

Deckungsbeitrag, Werbe-Break-even, Retourensensitivität und Startliquidität aus ausdrücklichen Annahmen berechnen.

Skill-Verzeichnis: `skills/amazon-unit-economics-cashflow`

**Umsetzungsgrundlage und Abhängigkeiten**

Numerische Preise/Kosten und belegte Marktplatzgebühren. Python 3.10+ für den Rechner ohne Drittanbieterpakete. Liquidität braucht zusätzlich Menge und Zahlungszeitpunkte.

**Eingaben**

JSON: Preis, Verkaufs-/Versandgebühren, Einstandskosten, Retourenrate/-verlust, Werbe-ACOS und weitere variable Kosten. Liquidität: Menge, Werkzeuge, Einrichtung, Anzahlung und Puffer. Eine Währung, Raten zwischen0 und1.

**Ausgaben**

JSON/gewählte Datei mit Beitrag/Marge, Break-even-ACOS, Retourenverlust, Erstbestellungsliquidität und Szenarien. Ungültige Eingaben erzeugen Fehlerstatus; keine Netz-/Kontoänderung.

[Ablauf · Grenzen und Abbruchbedingungen · Beispielanfrage](skills/amazon-unit-economics-cashflow/references/i18n/de.md)

> Verwende `$amazon-unit-economics-cashflow` — Mit bereitgestellten Halterpreisen Retouren-/ACOS-Szenarien vergleichen und Deckungsbeitrag sowie Startliquidität getrennt ausweisen; antworte auf Deutsch und erhalte Belege, unbekannte Werte und Berechtigungsgrenzen.

## Sprachumfang und Prüfung

Dieser lokalisierte Leitfaden umfasst Zweck, Voraussetzungen, Ein- und Ausgaben, Ablauf, Beispiele und Grenzen. Er übersetzt nicht jede Referenz Zeile für Zeile. Technische Detailreferenzen, historische Fälle, Skriptfehler, Beispieloberflächen und Bilder bleiben in der Originalsprache und können auf Wunsch erläutert werden. Struktur, Links und Kernbedingungen werden geprüft; ein muttersprachliches Lektorat je Sprache wird nicht behauptet.

Vor der Übergabe Eingaben, Belege, fehlende Werte, Ausgabedateien und ursprüngliche Abschlusskriterien abgleichen. Nicht ausgeführte Schritte als ungeprüft kennzeichnen; ein erfolgreicher Skriptablauf bestätigt keine geschäftliche Aussage.
