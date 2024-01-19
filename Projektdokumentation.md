# Projekt-Dokumentation


Nursiwat Xavier

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
| 12/01/2024      | 0.0.1   | "I" gemacht. Also Projekt ausgewählt und User Stories und Testfälle gemacht|
|       | ...     |                                                              |
|       | 1.0.0   |                                                              |

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
| 5.1 | Leerzeichen interpretieren | ".... . .-.. .-.. ---" | "HELLO"|
| 6.2 | Falsche Morse Code Struktur | ".-- .... .- -" | Fehlermeldung oder spezielle Behandlung der ungültigen Struktur |
| 7.2 | Große Menge an Text |One Piece ist das Beste| --- -. . / .--. .. . -.-. . / .. ... - / -.. .- ... / -... . ... - .|


### 1.4 Diagramme



## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 1.A  |       |           |              |               |
| ...  |       |           |              |               |

Total: 

✍️ Die Nummer hat das Format `N.m`, wobei `N` die Nummer der User Story ist, auf die sich das Arbeitspaket bezieht, und `m` von `A` an nach oben buchstabiert. Beispiel: Das dritte Arbeitspaket, das die zweite User Story betrifft, hat also die Nummer `2.C`.

✍️ Ein Arbeitspaket sollte etwa 45' für eine Person in Anspruch nehmen. Die totale Anzahl Arbeitspakete sollte etwa Folgendem entsprechen: `Anzahl R-Sitzungen` ╳ `Anzahl Gruppenmitglieder` ╳ `4`. Wenn Sie also zu dritt an einem Projekt arbeiten, für welches zwei R-Sitzungen geplant sind, sollten Sie auf `2` ╳ `3` ╳`4` = `24` Arbeitspakete kommen. Sollten Sie merken, dass Sie hier nicht genügend Arbeitspakte haben, denken Sie sich weitere "Kann"-User Stories für Kapitel 1.2 aus.

## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

### 5.1 Testprotokoll

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

### 5.2 Exploratives Testen

| BR-№ | Ausgangslage | Eingabe | Erwartete Ausgabe | Tatsächliche Ausgabe |
| ---- | ------------ | ------- | ----------------- | -------------------- |
| I    |              |         |                   |                      |
| ...  |              |         |                   |                      |

✍️ Verwenden Sie römische Ziffern für Ihre Bug Reports, also I, II, III, IV etc.

## 6 Auswerten

✍️ Fügen Sie hier eine Verknüpfung zu Ihrem Lern-Bericht ein.
