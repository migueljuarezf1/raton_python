import serial
import time
from pynput.keyboard import Controller

# Aqui hay que revisar bien el puerto porque cada vez que pongo las placas cambian de puerto
arduino_port = 'COM7'
baud_rate = 9600

keyboard = Controller()

# Asigna teclas para cada dirección
key_map = {
    "UP": 'w',
    "DOWN": 's',
    "LEFT": 'a',
    "RIGHT": 'd',
    "CLICK": 'space'  # puede ser otra tecla si quieres
}

# Conectar al Arduino
try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)
    print("Conectado al Arduino en", arduino_port)
except:
    print("⚠️ No se pudo conectar al puerto. ¿Correcto COM?")
    exit()

# Loop principal
while True:
    try:
        line = ser.readline().decode().strip()
        if line in key_map:
            key = key_map[line]
            print(f"→ {line} → tecla: {key}")
            keyboard.press(key)
            keyboard.release(key)
    except Exception as e:
        print("Error:", e)
