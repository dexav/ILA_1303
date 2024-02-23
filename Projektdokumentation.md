# Projekt-Dokumentation


Nursiwat Xavier

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
| 12/01/2024      | 0.0.1   | "I" gemacht. Also Projekt ausgewählt und User Stories und Testfälle gemacht|
| 19/01/2024      | 0.0.2     | "P" gemacht. Also geplant was ich machen werde und ein bisschen mit dem "R" angefangen also Implementierung von "Buchstaben zu Morse Code".|
| 26/01/2024      | 0.0.3   |"E" gemacht.Also alle wichtigen Entscheidungen die wir bis hierhin getroffen haben dokumentiert. "R" weitergemacht  |
|02/02/24 |0.0.4| "R" weitergemcaht|  

## 1 Informieren

### 1.1 Ihr Projekt

Ich mache ein Morscode-Decoder in Python, der Morscode in Buchstaben und umgekehrt überstzen kann.

In diesem Projekt möchte ich, dass man Buchstaben, Zahlen, Wörter und ganze Sätze übersetzen kann. Dabei möchte ich lernen, wie man eine Eingabe von "Buchstaben" in etwas anderes tranformiert/übersetzt.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    | muss            |Funktional      | Als User möchte ich, dass man Buchstaben in Morse Code übersetzen kann,|
| 2  | muss                | Qualität    | Als User möchte ich, dass das Programm in Python geschrieben ist.|
| 3  |  muss               | Qualität     | Als User möchte ich, dass das Programm zuverlässig und korrekt Morse Code in Buchstaben und umgekehrt übersetzt.|
| 4  |  muss               |Funktional      |Als User möchte ich, dass das Programm sowohl Kleinbuchstaben als auch Großbuchstaben unterstützt.|
| 5  |  muss               | Funktional     | Als User möchte ich, dass das Programm Sonderzeichen und Ziffern in Morse Code übersetzen kann. |
| 6  |  muss               | Funktional      | Als User möchte ich, dass das Programm Leerzeichen zwischen den Morse Code-Zeichen richtig interpretiert. |
| 7  |  muss               | Qualität     | 	Als User möchte ich, dass das Programm gut dokumentiert ist, damit ich es leicht verstehen und warten kann.|


### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| --- | --- | --- | --- |
| 1.1 | Buchstaben zu Morse Code | "Hello" | ".... . .-.. .-.. ---" |
| 1.2 | Morse Code zu Buchstaben | ".... . .-.. .-.. ---" | "HELLO" |
| 1.3 | Leerzeichen am Anfang und Ende | " Hello " | ".... . .-.. .-.. ---" |
| 1.4 | Leere Eingabe | "" | Geben Sie bitte etwas ein. |
| 1.5 | Unerwartetes Zeichen im Morse Code | "-.-. .-. --- . -. - ..- - .. --- -.-.-.-" | Fehlermeldung oder spezielle Behandlung des unerwarteten Zeichens |
| 2.1 | Korrekte Morse Code Übersetzung | "-.-. .-. --- . -. - ..- - .. --- -. .----. .--." | "CRONUT IS TASTY 1W" |
| 3.1 | Kleine und Große Buchstaben | "aBcDeF" | ".- -... -.-. -.. . ..-. " |
| 3.2 | Mischung von Buchstaben und Ziffern | "A1B2C3" | ".- .---- -... ..--- -.-. ...--" |
| 4.1 | Sonderzeichen und Ziffern | "!@#$ 123" | "-.-.-- .--.-. ...-..-..- ..--.. .---- ..--- ...--" |
| 4.2 | Umlaute und Sonderzeichen | "äöüß!" | "Nicht unterstützte Zeichen im Morse Code"|
| 5.1 | Leerzeichen interpretieren | ".... . .-.. .-.. ---/.-- --- .-. .-.. -.." | "HELLO WORLD"|
| 6.1 | Falsche Morse Code Struktur | ".-- .... .- -" | Fehlermeldung oder spezielle Behandlung der ungültigen Struktur |
| 7.1 | Große Menge an Text |One Piece ist das Beste| --- -. . / .--. .. . -.-. . / .. ... - / -.. .- ... / -... . ... - .|


### 1.4 Diagramme



## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---  | ---   | ---       | ---          | ---           |
| 1.A |26.01.2024  |Xavier Nursiwat | Implementierung der Funktion "Buchstaben zu Morse Code" | 3 Stunden |
| 1.B |26.01.2024  |Xavier Nursiwat  | Implementierung der Funktion "Morse Code zu Buchstaben" | 3 Stunden |
| 1.C |26.01.2024  |Xavier Nursiwat  | Behandlung von Leerzeichen am Anfang und Ende der Eingabe | 1 Stunde |
| 1.D |26.01.2024  |Xavier Nursiwat  | Behandlung einer leeren Eingabe | 1 Stunde |
| 1.E |26.01.2024  |Xavier Nursiwat  | Behandlung von unerwarteten Zeichen im Morse Code | 2 Stunden |
| 2.A |26.01.2024  |Xavier Nursiwat  | Implementierung der Funktion "Korrekte Morse Code Übersetzung" | 3 Stunden |
| 3.A |02.02.2024  |Xavier Nursiwat  | Implementierung der Funktion "Unterstützung von Klein- und Großbuchstaben" | 2 Stunden |
| 3.B |02.02.2024  |Xavier Nursiwat  | Implementierung der Funktion "Mischung von Buchstaben und Ziffern" | 2 Stunden |
| 4.A |02.02.2024  |Xavier Nursiwat  | Implementierung der Funktion "Unterstützung von Sonderzeichen und Ziffern" | 2 Stunden |
| 4.B |02.02.2024  |Xavier Nursiwat  | Behandlung von Umlauten und Sonderzeichen | 2 Stunden |
| 5.A |02.02.2024  |Xavier Nursiwat  | Behandlung von Leerzeichen in der Eingabe | 1 Stunde |
| 6.A |02.02.2024  |Xavier Nursiwat  | Behandlung einer falschen Morse Code-Struktur | 2 Stunden |



Total: 28 Stunden


## 3 Entscheiden

Wir haben uns dazu entschieden die Übersetzung in beide Richtungen zu machen damit man mit Freunden zum Beispiel zusammen in Morse Code schreiben kann. 

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |19.1.24|Xavier Nursiwat|3 Stunden              |2 Stunden|
| 1.B  |26.1.24|Xavier Nursiwat|3 Stunden               |3 Stunden|
| 1.C  |26.1.24|Xavier Nursiwat|1 Stunde              |1 Stunden|
| 1.D  |26.1.24|Xavier Nursiwat|1 Stunde              |1 Stunden|
| 1.E  |02.02.24|Xavier Nursiwat|2 Stunden               | 1 Stunde                   |
| 2.A  |26.1.24|Xavier Nursiwat|3 Stunden               |1 Stunden|
| 3.A  |26.1.24|Xavier Nursiwat|2 Stunden               |1 Stunden|
| 3.B  |02.02.24|Xavier Nursiwat|2 Stunden               |   2 Stunden                |
| 4.A  |02.02.24|Xavier Nursiwat|2 Stunden               |  1 Stunde                 |
| 4.B  |23.02.2024|Xavier Nursiwat|2 Stunden               | 1 Stunde                  |
| 5.A  |02.02.24|Xavier Nursiwat|1 Stunde               |  1 Stunde                 |
| 6.A  |02.02.24|Xavier Nursiwat|2 Stunden               |   1 Stunde                |



## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  | 23.02.2024      | OK         | Leonardo Grigioni       |
| 1.2  | 23.02.2024      | OK           |  Leonardo  Grigioni     |
| 1.3  |  23.02.2024     | OK           | Leonardo  Grigioni      |
| 1.4  |  23.02.2024|  OK          | Leonardo  Grigioni       |
| 1.5  | 23.02.2024      | NOK         | Leonardo  Grigioni       |
| 2.1  | 23.02.2024      | OK           | Leonardo  Grigioni       |
| 3.1  |23.02.2024       |     OK       |  Leonardo  Grigioni      |
| 3.2  | 23.02.2024      |         OK   | Leonardo  Grigioni       |
| 4.1  | 23.02.2024      |         OK   | Xavier Nursiwat     |
| 4.2  | 23.02.2024      |         OK   |  Xavier Nursiwat      |
| 5.1  | 23.02.2024      |         OK   | Xavier Nursiwat      |
| 6.1  | 23.02.2024      |          OK  |  Xavier Nursiwat      |
| 7.1  | 23.02.2024      |         OK   |  Xavier Nursiwat     |


✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
