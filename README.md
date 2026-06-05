# EMSY_TP4 SSR_LDE

## OBJECTIF

Utiliser deux ESP32-S3 en déployant un firmware identique en C et en MicroPython pour contrôler des périphériques physiques (boutons, LED standard et RGB) et établir une communication sans fil point à point entre deux cartes.

## Table des matières

- 🪧 [OBJECTIF](#OBJECTIF)
- 📦 [Prérequis](#prérequis)
- 🚀 [Installation](#installation)
- 🛠️ [Utilisation](#utilisation)
- 🤝 [Contribution](#contribution)
- 🏗️ [Construit avec](#construit-avec)
- 📚 [Documentation](#documentation)

## Prérequis

DOCUMENTS : EMSY02 TP4-Decouverte ESP32 v1_0 et 24210_KitDevESP32Gui_Schematic_Variant_[No Variations]

LIBRAIRIE : ili.py, xglcd_font.py et Unispace12x24.c

## Installation

LIBRAIRIE : 

ili : https://github.com/rdagger/micropython-ili9341/blob/master/ili9341.py

xglcd_font : https://github.com/rdagger/micropython-ili9341/blob/master/xglcd_font.py

Unispace12x24 : https://github.com/rdagger/micropython-ili9341/blob/master/fonts/Unispace12x24.c

## Utilisation

Utilisation Thony : https://github.com/LDE10/EMSY_TP4/blob/main/EMSY02%20TP4-Decouverte%20ESP32%20v1_0.pdf

<img width="709" height="226" alt="image" src="https://github.com/user-attachments/assets/f35bbe60-e3f0-47ee-948a-255204bc4098" />
page 3

Utilisation en C :https://github.com/LDE10/EMSY_TP4/blob/main/EMSY02%20TP4-Decouverte%20ESP32%20v1_0.pdf

<img width="531" height="130" alt="image" src="https://github.com/user-attachments/assets/8ed3fea9-cdc8-4072-9c79-2b1a38923f51" />
page 3


## Contribution

[### Sous-titre + description avec exemple des commandes à lancer pour l'ensemble du flux de contribution sur le dépôt]

## Construit avec

### Langages & Frameworks

Code C : https://github.com/LDE10/EMSY_TP4/tree/main/Code/C

Réalisez un programme qui change l’état de la LED D1 à chaque appui sur le bouton S1 avec une détection de flanc et antirebon, de plus les appuis sur S2 changent la couleur de la LED RGB du module (R->G->B)
ESP32-S3-DevKitC-1 (R → G → B → R → etc.). 

Code MicroPython : https://github.com/LDE10/EMSY_TP4/tree/main/Code/MicroPython

Même développement avec une ajout en plus,  dialoguer sans fil avec l’autre ESP32.

Mode locale : Sans connexion établie, le fonctionnement n’est pas modifié

Mode remote : Si la connexion est établie, lorsque le bouton S2 est appuyé, c’est la LED RGB de l’autre ESP qui changera de couleur. 
De plus la LED RGB clignote à une fréquence de 2 Hz. 

### Outils

#### CI

[Liste de tout ce qui permet l'intégration automatisée du projet avec description + lien vers la documentation et mise en avant des comptes, organisations et variables]

#### Déploiement

[Liste de tout ce qui permet le déploiement du projet avec description + lien vers la documentation et mise en avant des comptes, organisations et variables]

## Documentation

[Lien vers documentations externes ou documentation embarquée ici avec table des matières]



