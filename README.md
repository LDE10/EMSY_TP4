# EMSY_TP4 SSR_LDE

## OBJECTIF

Utiliser deux ESP32-S3 en déployant un firmware identique en C et en MicroPython pour contrôler des périphériques physiques boutons, LED standard et RGB (codé en MicroPython et en C) et établir une communication sans fil point à point entre deux cartes ESP32-S3 (codé seulement en MicroPython).

## Table des matières

- 🪧 [OBJECTIF](#OBJECTIF)
- 📦 [Prérequis](#prérequis)
- 🚀 [Installation](#installation)
- 🛠️ [Utilisation](#utilisation)
- 📚 [Documentation](#documentation)

## Prérequis

Matériel : KitDevESP32

DOCUMENTS : EMSY02 TP4-Decouverte ESP32 v1_0 et 24210_KitDevESP32Gui_Schematic_Variant_[No Variations]

LIBRAIRIE : ili.py, xglcd_font.py et Unispace12x24.c

## Installation

LIBRAIRIE : 

ili9341.py : Driver pour la gestion de l'affichage de l'écran LCD, https://github.com/rdagger/micropython-ili9341/blob/master/ili9341.py

xglcd_font : Gestionnaire de polices graphiques, https://github.com/rdagger/micropython-ili9341/blob/master/xglcd_font.py

Unispace12x24 : Fichier de police de caractères pour l'affichage de texte, https://github.com/rdagger/micropython-ili9341/blob/master/fonts/Unispace12x24.c

## Utilisation

Code C :

   * Bouton S1 (GPIO 4) : Contrôle l'état de la led D1 (GPIO 6), une détection de flanc descendant couplée à un anti-rebond temporel de 50 ms permet d'inverser l'état de la LED à chaque impulsion.
   * Bouton S2 (GPIO 5) : Gère le cycle de couleur de la LED RGB NeoPixel (GPIO 48), à chaque appui validé une machine à états (RGB_COLORS) incrémente la couleur selon le cycle (Rouge → Vert → Bleu)
   * Périphérique RMT : L'affichage de la couleur sur la LED RGB utilise le périphérique matériel de modulation à distance (RMT) configuré à une fréquence de 10 MHz pour garantir des signaux de commande précis.

Code MicroPython :

Le système bascule automatiquement entre deux modes toutes les 2 secondes :

1. Mode Local :
   * Bouton S1 (Pin 4) : Alterne l'état de la led D1 (Pin 6) à chaque appui (détection de flanc + anti-rebond).
   * Bouton S2 (Pin 5) : Modifie la couleur de la led RGB (Rouge → Vert → Bleu).
   * Écran LCD : Affiche en temps réel la couleur de la led RGB.

2. Mode Remote :
   * Activé dès qu'un message b'pong' est reçu en réponse à un b'ping'. Si aucun signal n'est reçu pendant plus de 4 secondes, le système repasse en Mode Local.
   * Bouton S1 (Pin 4) : Même fonctionnalité.
   * Bouton S2 (Pin 5) : L'appui sur le bouton agit sur l'autre carte ESP32 pour modifier la couleur de la led RGB.
   * LED RGB : En mode connecté, la LED RGB se met à clignoter à une fréquence de 2 Hz (250 ms).
   * Écran LCD : Affiche en temps réel la couleur de la led RG

### Langages & Frameworks

Code C : https://github.com/LDE10/EMSY_TP4/tree/main/Code/C

Code MicroPython : https://github.com/LDE10/EMSY_TP4/tree/main/Code/MicroPython

## Documentation

Utilisation Thony : https://github.com/LDE10/EMSY_TP4/blob/main/EMSY02%20TP4-Decouverte%20ESP32%20v1_0.pdf

<img width="709" height="226" alt="image" src="https://github.com/user-attachments/assets/f35bbe60-e3f0-47ee-948a-255204bc4098" />
page 3

Utilisation en C :https://github.com/LDE10/EMSY_TP4/blob/main/EMSY02%20TP4-Decouverte%20ESP32%20v1_0.pdf

<img width="531" height="130" alt="image" src="https://github.com/user-attachments/assets/8ed3fea9-cdc8-4072-9c79-2b1a38923f51" />
page 3


