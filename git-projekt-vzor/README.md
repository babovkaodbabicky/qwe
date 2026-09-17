# 🦆 Generátor nesmyslných citátů

Cvičný projekt vytvořený za účelem procvičení základních dovedností práce
s **Gitem a GitHubem** – větvení, Pull Requesty, code review, Issues,
commity a release. Samotná aplikace nemá žádný praktický přínos, jde jen
o hravou ukázku (web + CLI verze v Pythonu).

## 📖 Popis projektu

Po kliknutí na tlačítko se na stránce (nebo v terminálu) zobrazí náhodný
nesmyslný citát z předem připravené sbírky. Nic víc, nic míň.

Struktura repozitáře:

```
git-projekt-vzor/
├── README.md
├── .gitignore
├── src/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── generator.py
├── assets/
│   └── logo.svg
└── docs/
    └── poznamky.md
```

## 🚀 Návod ke spuštění

### Webová verze
1. Naklonuj repozitář: `git clone <odkaz-na-repo>`
2. Otevři soubor `src/index.html` v prohlížeči (stačí dvojklik).
3. Klikej na tlačítko „Vygenerovat citát“.

### CLI verze (Python)
```bash
cd src
python3 generator.py
```

## 👥 Autoři a rozdělení práce

| Jméno            | Větev                     | Co dělal/a                                  |
|-------------------|---------------------------|----------------------------------------------|
| Jana Nováková     | `feature/jana-html`       | Základní HTML struktura stránky              |
| Petr Svoboda      | `feature/petr-styling`    | CSS styly a vzhled karty                     |
| Eva Dvořáková     | `feature/eva-js-logika`   | JavaScript logika generátoru citátů          |
| Tomáš Král        | `feature/tomas-cli`       | CLI verze v Pythonu + poznámky v docs        |

*(jména a větve uprav podle skutečného složení vašeho týmu)*

## 🖼️ Ukázka výstupu

```
=== Generátor nesmyslných citátů ===

„Git je jako paměť slona, jen s víc konflikty.“
```

Webová verze zobrazuje stejný text ve stylované kartě uprostřed obrazovky
s fialovo-modrým pozadím a logem kachny v `assets/logo.svg`.

## 🧩 Issues a workflow

Práce byla rozdělena pomocí GitHub Issues (viz záložka *Issues* v repozitáři),
každý úkol měl přiřazený label (`enhancement`, `bug`, `documentation`) a
konkrétního řešitele. Po dokončení práce byly úkoly uzavírány automaticky
přes `Fixes #číslo` v příslušném Pull Requestu.

## 🏷️ Release

Aktuální stabilní verze projektu je označena tagem `v1.0.0` – viz sekce
*Releases* v repozitáři.

## 📄 Licence

Projekt je čistě cvičný, bez licenčních omezení – dělejte si s ním, co chcete.
