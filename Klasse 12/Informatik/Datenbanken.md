# Datenmodellierung und Datenbanken

## Modellierung in der Informatik

Ein Modell ist eine vereinfachte Beschreibung eines realen oder geplanten Systems

### Datenmodellierung

Bei der Datenmodellierung werden Daten in Beziehung gesetzt

### Datenflussmodellierung

Bei der Datenflussmodellierung werden komlpexe Systeme in überschaubare Teilsysteme zerlegt und der Informationsfluss zwischen den Teilen untersucht. Dabei helfen nomierte Diagramme , die aus folgenden Elemente bestehen:
- Zylinder: beständiges Datenobjekt
- Ellipse: informationsverarbeitender Prozess
- Rechteck: Datenquelle/Datensenke

## Modelle in der Informatik

### Hierarchisches Datenbankmodell

![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/Hierarchisches%20Datenbankmodell.png)

Das hierarchische Datenbankmodell bildet die reale Welt durch eine hierarchische Baumstruktur ab. Jeder Satz (engl. Record) hat also genau einen übergeordneten Vorgänger, mit Ausnahme genau eines Satzes, nämlich der Wurzel der so entstehenden Baumstruktur. 

### Entity-Relationship-Modell

![](ER-Modell.png)

Das Entity-Relationship-Modell – kurz ER-Modell oder ERM (mit der sinngemäßen Bedeutung „Modell zur Darstellung von Dingen / Gegenständen / Objekten und deren Beziehungen“) – dient dazu, im Rahmen der semantischen Datenmodellierung den in einem gegebenen Kontext (z. B. einem Projekt zur Erstellung eines Informationssystems) relevanten Ausschnitt der realen Welt zu bestimmen und darzustellen. Das ER-Modell besteht im Wesentlichen aus einer Grafik (ER-Diagramm, Abk. ERD) sowie einer Beschreibung der darin verwendeten Elemente. 

- **Entität** Objekt der realen Welt bzw. der Vorstellung
- **Entitätstypen** Entitäten mit gleichen Eigenschaften
- **Attribute** Eigenschaften der Entitäten
- **Beziehungen** Von Entitätstypen
- Kardinalität
- Primärschlüssel
- Fremdschlüssel

## Datenbanksysteme

**Definition**
Ein **Datenbanksystem** ist eine systematische und strukturierte Zusammenfassung von Daten eines Problembereiches (**Datenbasis**) einschließlich der zur Eingabe, Verwaltung, Auswertung und Ausgabe erforderlichen Software (Datenbankmanagmentsystem, DBMS)

Nach der Modellierung der verwalteten Daten unterscheidet man folgende Datenbankkarten:
- relationale Datenbanken
- hierarchische Datenbanken
- Netzwerk-Datenbanken

## Transformation

### Transformationsregeln

- Regel 1: Jeder Entitätstyp wird als Tabelle dargestellt. Jede Tabelle benötigt einen Primärschlussel.
- Regel 2: Jede n:m-Beziehung wird durch eine eigene Tabelle dargestellt.
- Regel 3: Jede 1:n- und 1:1-Beziehung mit eigenen Attributen wird wie bei Regel 2 durch eine eigene Tabelle dargestellt.
- Regel 4a: Jede 1:n-Beziehung ohne eigene Attribute wird so dargestellt, dass der Pri- märschlüssel des 1-Entitätstyps Fremdschlüssel des n-Entitätstyps wird.
- Regel 4b: Jede 1:1-Beziehung ohne eigene Attribute wird so dargestellt, dass der Pri- märschlüssel des ersten Entitätstyps beim zweiten Entitätstyp Primär- und Fremdschlüs- sel zugleich wird.
- Regel 4c: Sind Regel 4a oder 4b nicht anwendbar, dann wird für die Beziehung eine gesonderte Tabelle angelegt.

## Normalisation

### 1. Normalform

Jedes Attribut der Relation muss einen atomaren Wertebereich haben, und die Relation muss frei von Wiederholungsgruppen sein.

Atomar heißt, dass zusammengesetzte, mengenwertige oder geschachtelte Wertebereiche (also Relationen wertige Attributwertebereiche) nicht erlaubt sind. In einer Relation, die sich in 1NF befindet, gibt es kein Attribut, dessen Wertebereich in weitere (sinnvolle) Teilbereiche aufgespaltet werden kann. 

**Problem**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/1.%20Problem.png)

**Lösung**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/1.%20Lösung.png)
### 2. Normalform

Jedes nicht-primäre Attribut (nicht Teil eines Schlüssels) ist jeweils von allen **ganzen** Schlüsseln abhängig, nicht nur von einem Teil eines Schlüssels. Wichtig ist hierbei, dass die Nichtschlüsselattribute wirklich von _allen_ Schlüsseln vollständig abhängen.

**Problem**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/2.%20Problem.png)

**Lösung**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/2.%20Lösung.png)

### 3. Normalform

Eine Relation befindet sich in der 3. Normalform, wenn sie die 2. NF erfüllt und keine funktionalen Abhängigkeiten der Nichtschlüssel-Attribute (hellgraue Zellen in der Tabelle) untereinander bestehen. Solche Abhängigkeiten bezeichnet man auch als **transitive** Abhängigkeiten. Weiterhin müssen alle Nichtschlüssel voll funktional abhängig vom Schlüsselattribut sein.

**Problem**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/3.%20Problem.png)

**Lösung**
![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/3.%20Lösung.png)
