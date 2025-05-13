# 🤖 Bot per Legend of Slime (Idle RPG)

Questo progetto contiene un bot automatizzato scritto in **Python** per il gioco mobile [Legend of Slime](https://play.google.com/store/apps/details?id=com.loadcomplete.slimeidle).  
Utilizza **ADB** per controllare un dispositivo Android da remoto, e **OpenCV** + **Tesseract OCR** per il riconoscimento visivo degli elementi a schermo.



## 🧠 Funzionalità

- Riconoscimento dei bottoni di gioco via immagine (template matching)
- Tap automatici sui punti corretti dello schermo
- Modalità "intelligente" con controllo errori
- Logging base e facile estendibilità
- Progetto organizzato in virtual environment e mantenuto via GitHub



## 🛠️ Requisiti

- Python 3.8+
- `adb` (Android Debug Bridge)
- `tesseract-ocr`
- Dispositivo Android **collegato via ADB (cavo o rete)**


## 📂 Struttura del progetto

Il progetto è organizzato nei seguenti file e cartelle principali:

- **`bot.py`**  
  Script principale: contiene la logica che controlla il gioco eseguendo tap, analizzando lo schermo, e coordinando le azioni.

- **`utils.py`**  
  Modulo di supporto: raccoglie funzioni riutilizzabili come l’acquisizione dello schermo (`adb screencap`) e il tocco virtuale (`adb input tap`).

- **`templates/`**  
  Cartella con immagini di riferimento (template) da usare per riconoscere visivamente elementi dell'interfaccia del gioco.  
  Esempio: `attack_button.png`

- **`requirements.txt`**  
  Elenco delle librerie Python necessarie per eseguire il bot. Può essere installato con `pip install -r requirements.txt`.

- **`.gitignore`**  
  File che indica a Git quali file e cartelle ignorare (es. `venv/`, file temporanei, immagini di test, ecc.).

- **`README.md`**  
  Documentazione completa del progetto, con istruzioni per l’installazione, utilizzo e contributi.



## 🚀 Setup iniziale

1. **Clona la repository (o crea la cartella del progetto):**

```bash
git clone https://github.com/TUO_USERNAME/Bot-Legend-Slime.git
cd Bot-Legend-Slime
```

2. **Crea e attiva l’ambiente virtuale Python:**
   
```bash
python3 -m venv venv
source .\venv\Scripts\activate 
```

3. **Installa le dipendenze:**

```bash
pip install -r requirements.txt
sudo apt install adb tesseract-ocr -y
```

4. **Verifica il collegamento ADB:**

```bash
adb devices
# Dovresti vedere il tuo dispositivo nella lista
```

## 📌 Da fare

- Aggiungere più immagini template/ per migliorare il riconoscimento

- Implementare il loop continuo con logging

- Aggiungere gestione automatica di errori e popup


## 📜 Licenza

Questo progetto è open-source sotto licenza MIT.