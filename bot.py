import os

# Funzione per simulare il tocco su schermo (coordinata X=500, Y=1200)
def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")


tap(588, 307)  # Simula il tocco
print("Tocco eseguito")