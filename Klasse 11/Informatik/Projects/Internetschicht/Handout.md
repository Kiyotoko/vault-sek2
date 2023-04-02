---
author: karlz
tags:
- Informatik
- FGB
---

## Schicht 2: Internetschicht

- Hier erfolgt das *Routing*.
- *Routing*: Prozess bei dem die Wegewahl der Netzwerkpakete bestimmt wird, also über welche Rechner sie zum nächsten versendet werden sollen.
- *Routingtabellen*: Tabellen, in den alle Zwischenziele mit *IP* und *Subnetzmaske* aufgelistet sind.

## Schicht 1: Netzzugangsschicht

- Hier wird überprüft, ob ihr überhaupt Zugriff zum *Netzwerk* habt. Ziel ist es, das Kollisionen verhindert werden.
- Dies folgt über ein Zugriffsverfahren
- Die bekanntesten Zugriffsverfahren sind:
	- *CSMA/CD (Carrier Sense Multiple Access/Collusion Detection)*
	- *Token-Passing*
- *CSMA/CD*: ^[[Elektronik-Kompendium](https://www.elektronik-kompendium.de/sites/net/1406181.htm)]
	- *Carrier Sense* (Träger-Zustandserkennung): Jede Station prüft, ob das Übertragungsmedium frei ist.
	- *Multiple Access* (Mehrfachzugriff): Mehrere Stationen teilen sich das Übertragungsmedium.
	- *Collision Detection* (Kollisionserkennung): Wenn mehrere Stationen gleichzeitig senden, erkennen sie die Kollision.
- *Token-Passing*: ^[[Spektrum](https://www.spektrum.de/lexikon/physik/token-passing/14590)]
	- Eine Station im Netz, die Master-Station, sendet zunächst eine spezielle Nachricht, das Frei-Token, das im Netz von Station zu Station weitergegeben wird.
	- Nur jeweils diejenige Station, die gerade über das Frei-Token verfügt, hat Sendeerlaubnis. Die sendende Station hängt die eigentliche Nachricht an das (nun als ›belegt‹ gekennzeichnete) Token an.
	- Sobald der Empfänger diese Nachricht erhält, sendet er das Token mit einem Antwort-Bit an den Sender zurück. Der ursprüngliche Sender sendet dann ein neues Frei-Token aus.
