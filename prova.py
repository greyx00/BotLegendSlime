import os
import time

# Funzione per simulare il tocco su schermo (coordinata X=500, Y=1200)
def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")

while True:
    tap(500, 1200)  # Simula il tocco
    print("Tocco eseguito")
    time.sleep(10)  # Intervallo tra i tocchi (10 secondi)