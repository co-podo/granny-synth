# Granny Synth

Adrian Ludwig
 Im Sack 11
 86152 Augsburg
 +49 157 71704314

hello@adrianludwig.de



Codrin Podoleanu

2rd author's affiliation
 1st line of address
 2nd line of address
 Telephone number, incl. country code

codrin.podoleanu@hs-augsburg.de

## ABSTRACT

Kurze Zusammenfassung worum es geht und welche Ergebnisse erzielt wurden. Das Abstract schreibt man am besten als Letztes, wenn man den Inhalt des Papiers aufgeschrieben hat.

 #### Categories and Subject Descriptors

C.3 [SPECIAL-PURPOSE AND APPLICATION-BASED SYSTEMS] *,* H5.5 [SOUND AND MUSIC COMPUTING], [H.5.2](http://www.acm.org/about/class/ccs98-html#H.5.2) [USER INTERFACES]

#### General Terms

Design, Experimentation

#### Keywords

Granularsynthese, Raspberry Pi, Pure Data, Liveperformance

#### 1. MOTIVATION

##### Problemstellung: Granulare Synthese 

Bei der Erstellung elektronischer Musik kommt es darauf an stets eigene, neue Klänge zu gestalten. Eine sehr vielseitige, mächtige Möglichkeit Klänge zu gestalten und zu Formen it die sogenannte "Granularsynthese". Vor allem in der Improvisation lassen sich mit dieser Syntheseart stark eigenständige, eindrucksvolle Klänge erzeugen.

Da es sich um eine digitale Syntheseart handelt, gibt es bereits ein Vielzahl an Software-Synthesizern. Diese eignen sich für die Liveperformance nur bedingt, benötigen sie doch immer einen Rechner mit einer entsprechenden DAW. Vor allem in der Außenwahrnehmung durch Publikum entsteht dabei häufig der Eindruck, dass weniger Live auf der Bühne geschieht, als dass vieles vom Rechner abgespielt wird. Diese Wahrnehmung ist verständlich, sieht es manchmal doch tatsächlich so aus, als würde man seine Mails checken, wenn man angestrengt auf einen Bildschirm sieht. 

Ziel von Granny Synth ist es, dieses Problem zu beseitigen, indem auf Basis eines Kleinstrechners und geeigneter Interfacegestaltung ein Liveperformance-geeigneter Granularsynthesesystem gestaltet wird.

Dieses Paper beschreibt die Erstellung eines Prototypen des Systems "Granny Synth". Folgende Schritte werden im folgenden durchlaufen:

- Motivation

- Verwandte Arbeiten

- Anwendungszenarion

- - Anwendungsfall allgemein
  - Konkreter Anwendungsfall

- Entwurf des Prototyps

- - Technischer Ansatz
  - Konzeptueller Aufbau des Prototypen

- Implementierung

- - Hard- und Softwareumgebung
  - Kern der Implementierung
  - Umfang des Prototypen

- Evaluation

- - Ziele der Evaluation und Methodik
  - Durchführung der Evaluation
  - Interpretation der Evaluationsergebnisse

- Zusammenfassung

- - Erzielte Ergebnisse
  - Erweiterungsmöglchkeiten

#### 2. Verwandte Arbeiten

Wie in der Motivation beschrieben, gibt es bereits eine Vielzahl von Softwarelösungen für Granulare Synthese. Ein Prominentes Beispiel ist der in Ableton Live (Digital Audio Workstation) verfügbare "Granulator" https://www.monolake.de/technology/granulator.html

Diese Implementierung der Granularsynthese besticht durch eine vielzahl von Parametern und eine Verhältnismäßig einfache Bedienbarkeit. Dazu trägt insbesondere das sinnvoll gestaltete Bedieninterface entscheidend bei. 

In der Welt der Hardware finden sich vergleichsweise wenig Implementierungen von brauchbarer Granularsynthese. Am häufigsten noch sind Lösungen im Bereich der Modularen Synthesizersysteme zu finden. Ein prominentes Beispiel hier ist Mutable Instruments "Clouds" Eurorack-Modul. https://mutable-instruments.net/modules/clouds/ Hier besteht das Problem, dass man darauf angewiesen ist, ein entsprechendes Rack mit allen weiteren nötigen Modulen aufzubauen. Das ist aufwändig und vor allem teuer.

Ein System, das aufgrund seines Aufbaus viele Arten der Synthese zulässt, indem es auf die Open Source Software "Pure Data" zurückgreift, ist Critter and Guitaris "Organelle". https://www.critterandguitari.com/organelle Dabei kommt es auf die Community an, die neue Patches auch frei zur Verfügung stellen kann. Dieses System funktioniert sehr gut, ist aber Aufgrund kleiner Auflagen eher teuer.

Aufgrund dieser vorhergehenden Arbeiten soll mit "Granny Synth" eine Lösung für entscheidende Probleme der genannten Beispiele geschaffen werden. 

Der Klangerzeugungsaufbau und die Modulationsparamter des Granulator dienen als Grundlage zur Gestaltung der Softwareseite.

Als Basis für das System soll - wie bei Critter and Guitaris "Organelle" ein Raspberry Pi und Pure Data dienen. Im Gegensatz zur Organelle setzen wir explizit auf granulare Synthese, sowie auf niedrigere Kosten.

#### 3.ANWENDUNGSSZENARIO & Use Case

1. ##### 3.1 Portabler Granularsynthesizer

2. Entwicklung eines portablen, preiswerten Granularsynthesizers. Nutzer:innen sollen mit dem Gerät ein          flexibles,  Portables Gerät für die Liveanwendung von Granularsynthese zur Hand haben. 

1. ##### 3.2 Definition der Use Cases

2. Die wichtigsten Uses Cases werden im Folgenden erläutert.

###### 	3.2.1 Hardwaresystem für Granularsynthese

Ein:e Nutzer:in benutzt das System um einen Granularen Synthesizer zu steuern. Dafür werden die eingesetzten Hardwarekomponenten zur Kommunikation zwischen Akteur und Hardwaresystem genutzt. 
  - User dreht Encoder im Uhrzeigersinn: 
       nkrement eines Parameterwertes

  - User dreht Encoder gegen Uhrzeigersinn: 
       ekrement einesParameterwertes

  - User drückt Encoder nach unten: 
       odus des jeweiligen Encoders wird ausgewählt

       ###### 3.2.2 Modulares Hardwaresystem zur Bedienung von Pure Data 

       Ein:e Nutzer:in definiert ein eigenes Pure Data Patch, das über die vorhandene Hardware gesteuert werden kann. Hierfür muss die Nutzer:in eine entsprechende Konfigurationsdatei für die Hardware, sowie ein „Pure Data“- Patch anlegen.

#### 4. **ENTWURF EINES PROTOTYPS**

1. ##### 4.1 Technischer Ansatz

2. Das Gerät basiert auf der Hardwareseite aus einem Raspberry-pi 3, Fünf Ky-040 Drehencodern, sowie einem 20x4 Zeichen LCD Display. Die Komponenten befinden sich in einem einfachen, aus Holz gefertigten Gehäuse.
    Zur Verarbeitung der IO-Befehle verwenden wir python und die zum Raspberry korrespondierende python Library RPi.GPIO. 
    Als System für die Granularsynthese verwendet das System die Open Source Software „Pure Data“. 
    Die Kommunikation zwischen GPIO und Pure Data erfolgt über das OSC-Protokoll.

1. ##### 4.2 **Konzeptueller Aufbau des Prototypen**

2. Das System besteht aus mehreren, miteinander kommunizierenden Untersystemen. 

3. Beschreiben Sie hier aus welchen Systemkomponenten Ihr Prototyp besteht, welche Schnittstellen Sie zwischen den Komponenten festlegen. Evtl. ist es sinnvoll, weitere Unterpunkte zu bilden, etwa zur Beschreibung eines „Servers“ und eines „Clients“ oder zwischen „Sensorik“ und „Steuerung“ usw., je nachdem, welche Komponenten Ihr Konzept umfasst.

1. 1. ###### 4.2.1 GPIO - Server

   2. Die Verarbeitung der Sensordaten erfolgt über einen GPIO-Server, der die entsprechenden Inputs und 	Outputs überwacht. Er empfängt die Signale von Encodern und Display und handlet die Ausgabe von 	Daten an das Display.

1. 1. ###### 4.2.2 OSC-Client

   2.  Die Kommunikation der GPIO Signale zur Audioverarbeitungssoftware erfolgt über einen OSC-Client.

   3. ###### 4.2.3 OSC-Server

   4. In der Umgebung des Klangerzeugers empfängt ein Server die über OSC Übertragenen Befehle zur Kontrolle des Klangerzeugers.

1. 1. ###### 4.2.4. Klangerzeuger/Granularer Synthesizer

   2. Die Audioverarbeitung erfolgt über eine eigene Sofware, in diesem Fall „Pure Data“.
      Innerhalb der Software wird ein „Patch“ für die Granularsynthese angefertigt. Die Steuerung erfolgt über OSC. Das Programm steuert auch die Audioausgabe auf dem Gerät.* 

Beachten Sie, in diesem Abschnitt sollten Sie weitgehend von Implementierungsdetails abstrahieren. Diese bündeln Sie in einem separaten Abschnitt



#### 5. IMPLEMENTIERUNG 

1. ##### 5.1. Hard- und Softwareumgebung

Hardware: 

- 5 x KY-040 Drehimpulsgeber
- 1 x 20x4 LCD-Display
- 1 x IC2 Adapter
- 1 x kurzes Breadboard
- 1 x Breakout-Adapter Rasperry pi
- 1 x Raspberrry Pi 3 B

Auf dem Raspberry Pi läuft das Debian-basierte Linux-Betriebssystem Raspbian. Als Sprache für die IO-Kommunikation wird Python genutzt. Folgende Libraries werden dafür verwendet:

- Python-osc
- RPI.GPIO
- ADAFRUIT_LCD1602
- PCF857
- time
- argparse

Für die Synthese wird die Software „Pure Data“ verwendet. Folgende Pakete werden genutzt:

### CODY SCHREIB HIER MAL WAS HIN 

Beschreiben Sie hier kurz Ihre Entwicklungsumgebung (Hardware, Betriebssystem, Programmiersprachen / Bibliotheken, eingesetzte Tools etc.). Evtl. können Sie hier auch noch auf die Entwicklungsmethode eingehen, etwa, wenn Sie verschiedene Testaufbauten gemacht haben, die letztlich zum finalen Prototypen geführt haben.

1. ##### 5.2  Kern der Implementierung

2. Ein großer Teil der Arbeit war die Anfertigung des Pure Data Patches für die Granularsynthese, sowie die Kommunikation zwischen GPIO des Raspberry Pi und Pure Data.

3. Dabei war eine besondere Herausforderung das Einrichten des Betriebssystems und der Selbst erstellten Software, sowie die Modularisierung der Eingabe. Das System sollte so flexibel wie möglich bedienbar sein. Die Dreh/Switch-Encoder sollen so viele Parameter wie möglich zugänglich machen.. 

1. ##### 5.3 Umfang des Prototypen

Der Umfang des Prototypen beschränkt sich auf ein Proof of Concept. Dabei funktioniert das Laden eines Samples für die Granularsynthese, sowie die Steuerung der wichtigsten Parameter über die Encoder.

#### 6. EVALUATION

Das System wurde unter Anhand verschiedener Aspekte evaluiert. Insbesondere die Unterbrechungsfreie Wiedergabe, sowie die Steuerung der gewünschten Parameter über die vorhandene Hardware wurden betrachtet.

Die Bedienung soll für jemanden, der mit der Funktionsweise Granularer Synthese vertraut ist, zumindest ansatzweise nachvollziehbar und schnell erlernbar sein.

1. ##### 6.1 Ziele der Evaluation und Methodik

2. Ziel der Evaluation ist vornehmlich festzustellen, ob das System als eigenständiges Hardwaresystem für Granularsynthese funktioniert. 

3. Um festzustellen, ob das System den Anforderungen genügt, werden die Parameter, die zur Steuerung eingerichtet wurden auf in Hinblick auf die Systemperformance (Audio Dropouts) auf ihre Grenzbereiche hin überprüft. Dabei handelt es sich vor allem um Parameter, die die den Umgang mit einzelnen Grains betreffen:
    Grainanzahl, Graingröße, Density, „Polyphonie“

4. Darüber hinaus werden weitere Klangformungsmöglichkeiten implementiert, um das System „Livetauglich“ zu machen. Dazu gehören verschiedene Effekte wie bspw. Ein Filter und Reverb.

5. Je nachdem, worauf Ihre Studie abzielt, können Sie z.B. daran interessiert sein, ob Ihre Technik überhaupt nutzbar ist (d.h., kommen Nutzer damit zurecht oder kommt es häufig zu Fehlbedienungen). Das finden Sie z.B. heraus, wenn Sie Testpersonen mit Ihrem System arbeiten lassen.

6. Wollen Sie hingegen nachweisen, dass Ihr System besser ist, als ein bereits existierendes, so können Sie einen Systemvergleich anstellen. 

1. ##### 6.2. Durchführung der Evaluation

2. Hier beschreiben Sie, wie Sie Ihr System evaluiert haben. Falls Sie eine Datenerhebung (Logging / Fragebogen / Interview) gemacht haben, geben Sie an, was dabei herauskam, z.B. die Anzahl der von einer Testperson gemachten Bedienfehler. Haben Sie mehrere Testpersonen involviert, können Sie auch eine statistische Auswertung durchführen.

3. Wichtig: hier geht es um die Angabe der objektiven Befunde, Spekulationen, warum ein Befund so oder so ausgefallen ist, haben hier nichts verloren!

1. ##### 6.3. Interpretation der Evaluationsergebnisse

2. Hier können Sie ggf. darüber spekulieren, wie die in der Evaluation gefunden Befunde zu erklären sind und durch welche Änderungen sich ggf. Optimierungen erzielen lassen könnten.

#### 7. ZUSAMMENFASSUNG

Hier fassen Sie nochmal kurz zusammen, was Sie gemacht haben und welche Erkenntnisse aus Ihrer Arbeit hervorgegangen sind. Es bietet sich eine Gliederung an in die Teilabschnitte „Erzielte Ergebnisse“ und. „Ausblick“.

1. ##### 7.1. Erzielte Ergebnisse

2. z.B. 

3. „Die vorliegende Studie beschäftigte sich mit der Fragestellung, inwiefern sich die „<X>-Technologie für die <Y>-Anwendung nutzen lässt. Dazu wurden zunächst für die <Y>-Anwendung wichtige Use Cases definiert, die dann der Entwicklung eines einfachen Prototypen zugrunde gelegt wurden. Der Prototyp besteht im Wesentlichen aus den Komponenten A B und C. Komponente B nutzt dabei eine leicht modifizierte Version der X-Technologie. Die Modifikation besteht aus der Erweiterung von X zu XX.“

4. In einer anschließenden Evaluation wurde der Prototyp hinsichtlich der Kriterien K1 bis Kk untersucht. Als Evaluationsmethode wurde eine Nutzerstudie mit n Testnutzern durchgeführt. Die Studie ergab, dass die erweiterte X-Technik für den Einsatz in einer Y-Anwendung zwar prinzipiell geeignet ist, jedoch noch weiteres Finetuning erforderlich ist.

1. ##### 7.2. Erweiterungsmöglichkeiten / Ausblick 

2. Hier beschreiben Sie kurz, welche Verbesserungs- und Erweiterungsmöglichkeiten sinnvoll wären. Sofern Sie schon eine Idee zur Realisierung haben, können Sie diese in einem Satz skizzieren.  

3. Da es in der Regel noch sehr viel zu tun gibt, müssen Sie eine Auswahl treffen! Konzentrieren Sie sich auf die unbedingt durchzuführenden bzw. interessantesten Erweiterungen.

#### **REFERENZEN**

1. Implementing Real-Time Granular SynthesisRoss BencinaDraft of 31st August 2001 http://www.rossbencina.com/static/code/granular-synthesis/BencinaAudioAnecdotes310801.pdf
2. Granular Synthesis - How It Works & Ways To Use It - Simon Price, December 2005 https://www.soundonsound.com/techniques/granular-synthesis
3. Granulator II - Robert Henke - https://roberthenke.com/technology/granulator.html
4. Granularsynthese mit Pure Data - http://www.pd-tutorial.com/german/ch03s07.html
5. Pythonosc - https://pypi.org/project/python-osc
6. Python GPIO https://www.raspberrypi.org/documentation/usage/gpio/python/README.md
7. Raspberry Pi and realtime, low-latency audio - https://wiki.linuxaudio.org/wiki/raspberrypi
8. Granular Synthesis - http://www.sfu.ca/~truax/gran.html