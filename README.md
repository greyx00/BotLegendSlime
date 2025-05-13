# 🤖 Bot per Legend of Slime (Idle RPG)

Questo progetto contiene un bot automatizzato scritto in **Python** per il gioco mobile [Legend of Slime](https://play.google.com/store/apps/details?id=com.loadcomplete.slimeidle).  
Utilizza **ADB** per controllare un dispositivo Android da remoto, e **OpenCV** + **Tesseract OCR** per il riconoscimento visivo degli elementi a schermo.

⚠️ **Il progetto è pensato per essere eseguito in ambiente Linux o all’interno di WSL (Windows Subsystem for Linux)**.  
Non è garantito il funzionamento nativo su Windows senza WSL.


## 🧠 Funzionalità

- Riconoscimento visivo dei bottoni di gioco (template matching)
- Tap automatici sui punti corretti dello schermo via `adb`
- Modalità "intelligente" con gestione degli errori
- Logging base ed estendibilità semplice
- Organizzazione pulita in virtual environment e repository Git



## 🛠️ Requisiti

- Sistema operativo **Linux** o **WSL**
- Python 3.8 o superiore
- `adb` (Android Debug Bridge)
- `tesseract-ocr`
- Dispositivo Android o emulatore collegato via ADB (USB o rete)


## 📂 Struttura del progetto

- **`bot.py`**  
  Script principale: esegue tap, analizza lo schermo, prende decisioni.

- **`utils.py`**  
  Funzioni di supporto: screenshot, OCR, input touch, ecc.

- **`templates/`**  
  Cartella con immagini di riferimento (es. `attack_button.png`) per il riconoscimento tramite OpenCV.

- **`requirements.txt`**  
  Dipendenze Python installabili via `pip install -r requirements.txt`.

- **`.gitignore`**  
  File per ignorare cartelle locali (`venv/`, file temporanei, ecc.).

- **`README.md`**  
  Questa documentazione.


## 🚀 Setup iniziale

1. **Clona la repository (o crea la cartella del progetto):**

```bash
git clone https://github.com/TUO_USERNAME/Bot-Legend-Slime.git
cd Bot-Legend-Slime
```

2. **Crea e attiva l’ambiente virtuale Python:**
   
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Installa le dipendenze Python:**

```bash
pip install -r requirements.txt
```

4. **Installa i tool di sistema richiesti (solo Linux/WSL):**

```bash
sudo apt update
sudo apt install adb tesseract-ocr -y
```

5. **Verifica il collegamento ADB:**

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