from machine import Pin, SPI # Gestion des pin et du SPI
from ili9341 import Display, color565 # Gestion de l'écran et des couleurs
from xglcd_font import XglcdFont #Gestion ecriture
import time #Gestion temps
import neopixel # Pour led RGB
import network  # Pour envoyer gestion wifi
import espnow   # Pour recevoir protocole

# Configuration SPI et Écran
spi = SPI(2, baudrate=24000000, sck=Pin(12), mosi=Pin(13), miso=Pin(11))
display = Display(spi, cs=Pin(14), dc=Pin(10), rst=Pin(9), rotation=90)

# Taille de l'ecran
display.width = 320
display.height = 240

# CHARGEMENT DE LA POLICE D'ECRITURE
font = XglcdFont('Unispace12x24.c', 12, 24)

# COULEURS
NOIR = color565(0, 0, 0)
BLANC = color565(255, 255, 255)
ROUGE = color565(255, 0, 0)
VERT = color565(0, 255, 0)
BLEU = color565(0, 0, 255)

Couleur_Texte = [ROUGE, BLEU, VERT]

# Activation du wifi
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)

# Activation reception
e = espnow.ESPNow()
e.active(True)

peer = b'\xbb\xbb\xbb\xbb\xbb\xbb' # Adresse 
e.add_peer(peer)

# Localisation des PIN
led1 = Pin(6, Pin.OUT)
bouton1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
bouton2 = Pin(5, Pin.IN, Pin.PULL_DOWN)

Lrgb = Pin(48, Pin.OUT)
Np = neopixel.NeoPixel(Lrgb, 1)

led1.value(1)

Btn1Old = 0
Btn1New = 0
Btn2Old = 0
Btn2New = 0

# LED RGB
R = (5, 0, 0)
G = (0, 5, 0)
B = (0, 0, 5)

Led = [R, G, B]

index = 0
old_index = -1

# Variables d'état
remote_mode = False
led_allumee = True

# CHRONO
chrono_envoi = time.ticks_ms()       
chrono_clignote = time.ticks_ms()    
dernier_contact = time.ticks_ms()    


Np[0] = Led[index]
Np.write()

while True :
    maintenant = time.ticks_ms()
    
    Btn1Old = Btn1New
    Btn1New = bouton1.value()
    
    Btn2Old = Btn2New
    Btn2New = bouton2.value()
    

# 1. ENVOI AUTOMATIQUE TOUTES LES 2 SECONDES
    if time.ticks_diff(maintenant, chrono_envoi) >= 2000: # Toutes les 2 s 
        try:
            e.send(peer, b'ping') # Envoie un "ping" 
        except OSError:
            # Passe en mode local
            pass
        chrono_envoi = maintenant

# 2. RÉCEPTION DES MESSAGES
    host, msg = e.recv(0) 

    # Si recoit 'ping', répond 'pong' sur l'autre carte
    if msg == b'ping':
        try:
            e.send(peer, b'pong')
        except OSError:
                pass
            
    # Valide le mode Remote
    if msg == b'pong':
        dernier_contact = maintenant # Temps depuis la derniere communication
        if not remote_mode:
            print("Mode remote.")
            remote_mode = True
            
    if msg == b'change_led':
        index = (index + 1) % 3
        # Si on n'est pas en mode remote, applique la couleur
        if not remote_mode: 
            Np[0] = Led[index]
            Np.write()


# 3. VÉRIFICATION DU TEMPS DE SORTIE
    # Si pas de communication depuis plus 4 secondes -> Mode Local
    if time.ticks_diff(maintenant, dernier_contact) > 4000:
        if remote_mode: 
            print("Mode Local.")
            remote_mode = False
            
            Np[0] = Led[index] 
            Np.write()        

# 4. GESTION DU BOUTON S2
    if Btn2New == 1 and Btn2Old == 0: 
        if remote_mode:
            # MODE REMOTE
            try:
                e.send(peer, b'change_led')
                print("Changement de couleur")
            except OSError:
                print("Échec")
        else:
            # MODE LOCAL
            index = (index + 1) % 3
            Np[0] = Led[index]
            Np.write()
            print("Changement de couleur")

# 5. CLIGNOTEMENT À 2 Hz
    if remote_mode:
        if time.ticks_diff(maintenant, chrono_clignote) >= 250: # Toutes les 250 ms (Clignotement 2 Hz)
            led_allumee = not led_allumee
            if led_allumee:
                Np[0] = Led[index] 
            else:
                Np[0] = (0, 0, 0) 
            Np.write()
            chrono_clignote = maintenant

# 6. GESTION DU BOUTON 1 & TEMPS GENERAL
    if Btn1New == 0 and Btn1Old == 1:
        led1.value(0)
    elif Btn1New == 1 and Btn1Old == 0 :
        led1.value(1)
            
    time.sleep_ms(20) # Anti-rebond 


# 7. GESTION AFFICHAGE
# Remplissage du fond en noir
    if index != old_index :
        display.fill_rectangle(0, 0, display.width, display.height, NOIR)
        display.draw_text(20, 50, "Changement de couleur en", font, BLANC, NOIR)
    
# Ecriture
        Couleurs = Couleur_Texte[index]
        if Couleurs == Couleur_Texte[0]:
            display.draw_text(20, 100, "Rouge", font, ROUGE, NOIR)
            
        elif Couleurs == Couleur_Texte[1]:
            display.draw_text(20, 100, "Vert", font, VERT, NOIR)
            
        elif Couleurs == Couleur_Texte[2]:
            display.draw_text(20, 100, "Bleu", font, BLEU, NOIR)
        
#        display.draw_text(20, 100, "couleur", font, Couleurs, NOIR)
        old_index = index