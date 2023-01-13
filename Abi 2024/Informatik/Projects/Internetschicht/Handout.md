# Handout 
## Schicht 2: Internetschicht
~~~ad-important
- Hier erfolgt das _Routing_.
- _Routing_: Prozess bei dem die Wegewahl der Netzwerkpakete bestimmt wird, also über welche Rechner sie zum nächsten versendet werden sollen.
- _Routingtabellen_: Tabellen, in den alle Zwischenziele mit _IP_ und _Subnetzmaske_ aufgelistet sind.
~~~
## Schicht 1: Netzzugangsschicht
~~~ad-important
- Hier wird überprüft, ob ihr überhaupt Zugriff zum _Netzwerk_ habt. Ziel ist es, das Kollisionen verhindert werden.
- Dies folgt über ein Zugriffsverfahren
- Die bekanntesten Zugriffsverfahren sind:
	- _CSMA/CD (Carrier Sense Multiple Access/Collusion Detection)_
	- _Token-Passing_
- _CSMA/CD_: [$^{[1]}$](https://www.elektronik-kompendium.de/sites/net/1406181.htm)
	- _Carrier Sense_ (Träger-Zustandserkennung): Jede Station prüft, ob das Übertragungsmedium frei ist.
	- _Multiple Access_ (Mehrfachzugriff): Mehrere Stationen teilen sich das Übertragungsmedium.
	- _Collision Detection_ (Kollisionserkennung): Wenn mehrere Stationen gleichzeitig senden, erkennen sie die Kollision.
- _Token-Passing_: [$^{[2]}$](https://www.spektrum.de/lexikon/physik/token-passing/14590)
	- Eine Station im Netz, die Master-Station, sendet zunächst eine spezielle Nachricht, das Frei-Token, das im Netz von Station zu Station weitergegeben wird.
	- Nur jeweils diejenige Station, die gerade über das Frei-Token verfügt, hat Sendeerlaubnis. Die sendende Station hängt die eigentliche Nachricht an das (nun als ›belegt‹ gekennzeichnete) Token an.
	- Sobald der Empfänger diese Nachricht erhält, sendet er das Token mit einem Antwort-Bit an den Sender zurück. Der ursprüngliche Sender sendet dann ein neues Frei-Token aus.
~~~