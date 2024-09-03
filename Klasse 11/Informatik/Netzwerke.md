# Kommunikation in Netzen

## Internet Protokolle

| IPv4                                                | IPv6                                          |
| --------------------------------------------------- | --------------------------------------------- |
| $32$-Bit-IP                                         | $128$-Bit-IP                                  |
| $2^{32}$ Adressen                                   | $2^{128}$ Adressen                            |
| Adressen müssen wiederverwendet und maskiert werden | Jedes Gerät kann eine eigene Adresse bekommen |

## OSI

1. Schicht / **Bitübertragung**: Umwandlung der Bits in ein zum Medium passendes Signal und physikalische Übertragung.
1. Schicht / **Sicherung**: Segmentierung der Pakete in Frames und Hinzufügen von Prüfsummen.
1. Schicht / **Vermittlung**: Routing der Datenpakete zum nächsten Knoten.
1. Schicht / **Transport**: Zuordnung der Datenpakete zu einer Anwendung.
1. Schicht / **Sitzung**: Steuerung der Verbindungen und des Datenaustauschs.
1. Schicht / **Darstellung**: Umwandlung der systemabhängigen Daten in ein unabhängiges Format.
1. Schicht / **Anwendung**: Funktionen für Anwendungen sowie die Dateneingabe und -ausgabe.

„**A**lle **d**eutschen **S**tudenten **t**rinken **v**erschiedene **S**orten **B**ier“

## TCP

![OSI vs TCP](OSI%20vs%20TCP.png)
