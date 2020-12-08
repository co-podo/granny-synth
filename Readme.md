# Granny Synth

## Abstract

Granny Synth ist ein für Liverperformance konzipierter Granularer Snythesizer. Dabei setzen wir Pure Data auf Softwareseite und Raspberry Pi, blabla

## 1. Motivation

Problemstellung: Granulare Synthese 

Bei der Erstellung elektronischer Musik kommt es darauf an stets eigene, neue Klänge zu gestalten. Eine sehr vielseitige, mächtige Möglichkeit Klänge zu gestalten und zu Formen it die sogenannte "Granularsynthese". Vor allem in der Improvisation lassen sich mit dieser Syntheseart stark eigenständige, eindrucksvolle Klänge erzeugen.
Da es sich um eine digitale Syntheseart handelt, gibt es bereits ein Vielzahl an Software-Synthesizern. Diese eignen sich für die Liveperformance nur bedingt, benötigen sie doch immer einen Rechner mit einer entsprechenden DAW. Vor allem in der Außenwahrnehmung durch  Publikum entsteht dabei häufig der Eindruck, dass weniger Live auf der Bühne geschieht, als dass vieles vom Rechner abgespielt wird. Diese Wahrnehmung ist verständlich, sieht es manchmal doch tatsächlich so aus, als würde man seine Mails checken, wenn man angestrengt auf einen Bildschirm sieht. 
Ziel von Granny Synth ist es, dieses Problem zu beseitigen, indem auf Basis eines Kleinstrechners und geeigneter Interfacegestaltung ein Liveperformance-geeigneter Granularsynthesesystem gestaltet wird.

Dieses Paper beschreibt die Erstellung eines Prototypen des Systems "Granny Synth". Folgende Schritte werden im folgenden durchlaufen:

1. Motivation
2. Verwandte Arbeiten
3. Anwendungszenarion
   1. Anwendungsfall allgemein
   2. Konkreter Anwendungsfall
4. Entwurf des Prototyps
   1. Technischer Ansatz
   2. Konzeptueller Aufbau des Prototypen
5. Implementierung
   1. Hard- und Softwareumgebung
   2. Kern der Implementierung
   3. Umfang des Prototypen
6. Evaluation
   1. Ziele der Evaluation und Methodik
   2. Durchführung der Evaluation
   3. Interpretation der Evaluationsergebnisse
7. Zusammenfassung
   1. Erzielte Ergebnisse
   2. Erweiterungsmöglchkeiten

## 2. Verwandte Arbeiten

Wie in der Motivation beschrieben, gibt es bereits eine Vielzahl von Softwarelösungen für Granulare Synthese. Ein Prominentes Beispiel ist der in Ableton Live (Digital Audio Workstation) verfügbare "Granulator" https://www.monolake.de/technology/granulator.html

Diese Implementierung der Granularsynthese besticht durch eine vielzahl von Parametern und eine Verhältnismäßig einfache Bedienbarkeit. Dazu trägt insbesondere das sinnvoll gestaltete Bedieninterface entscheidend bei. 

In der Welt der Hardware finden sich vergleichsweise wenig Implementierungen von brauchbarer Granularsynthese. Am häufigsten noch sind Lösungen im Bereich der Modularen Synthesizersysteme zu finden. Ein prominentes Beispiel hier ist Mutable Instruments "Clouds" Eurorack-Modul. https://mutable-instruments.net/modules/clouds/ Hier besteht das Problem, dass man darauf angewiesen ist, ein entsprechendes Rack mit allen weiteren nötigen Modulen aufzubauen. Das ist aufwändig und vor allem teuer.

Ein System, das aufgrund seines Aufbaus viele Arten der Synthese zulässt, indem es auf die Open Source Software "Pure Data" zurückgreift, ist Critter and Guitaris "Organelle". https://www.critterandguitari.com/organelle Dabei kommt es auf die Community an, die neue Patches auch frei zur Verfügung stellen kann. Dieses System funktioniert sehr gut, ist aber Aufgrund kleiner Auflagen eher teuer.

Aufgrund dieser vorhergehenden Arbeiten soll mit "Granny Synth" eine Lösung für entscheidende Probleme der genannten Beispiele geschaffen werden. 
Der Klangerzeugungsaufbau und die Modulationsparamter  des Granulator dienen als Grundlage zur Gestaltung der Softwareseite.
Als Basis für das System soll - wie bei Critter and Guitaris "Organelle" ein Raspberry Pi und Pure Data dienen. Im Gegensatz zur Organelle setzen wir explizit auf granulare Synthese, sowie auf niedrigere Kosten.







