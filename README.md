# Invoice Analizer - plan projektu
Projekt bedzie sie skladac z modulu glownego - invoiceAnalizer i submodulow. Poszczegolne, planowane submoduly to:
* invoiceExtractor - dokonywana jest ekstrakcja i analiza danych z faktur w formacie pdf. Na Gicie jest to odrebne repozytowium [invoiceExtractor](https://github.com/enxy/invoiceExtractor).
* submodul z PySpark, do dalszego przechowywania danych i budowy modelu.
* framework do graficznej prezentacji danych

## Nastepne zadania
- nauka PySparka i dodanie submodulu
- generowanie faktur z przykladowymi danymi (docelowo ma ich byc 1000)
- refaktoryzacja kodu w submodule invoiceExtractor

## Dodatkowe uwagi
* w katalogu invoices znajduja sie przyklady obslugowanych szablonow faktur (inv1, inv2, inv3, inv4),
roznia sie one polami na fakturze i sposobem rozmieszczeniem danych.
* invoices/outputs.json to plik wyjsciowy po ekstrakcji danych z faktur pdf. Dane te zostana wykorzystane w celach obliczeniowych, do budowy odpowiedniego modelu.
