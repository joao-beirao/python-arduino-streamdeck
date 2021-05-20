from pynput import keyboard
from pynput.keyboard import Key, Controller
import subprocess
import time
import sys
import serial

progA = "C:\\Program Files\\obs-studio\\bin\\64bit\obs64.exe"
progB = "C:\\Users\\joaob\\AppData\\Local\\Gener8\\Application\\gener8.exe"
progC = "C:\\Users\\joaob\\AppData\\Roaming\\Spotify\\Spotify.exe"

arduino = serial.Serial("COM4", 9600, timeout = .1)

keyboard = Controller()
key1 = "!"
key2 = "@"
key3 = "£"
key4 = "§"
key5 = "€"
key6 = "&"
key7 = "{"
key8 = "["
key9 = "]"




while True:
    data = arduino.readline().rstrip().decode("utf-8")
    if data:
        if data == "1":
            keyboard.press(key1)
            keyboard.release(key1)
        elif data == "2":
            keyboard.press(key2)
            keyboard.release(key2)
        elif data == "3":
            keyboard.press(key3)
            keyboard.release(key3)
        elif data == "4":
            keyboard.press(key4)
            keyboard.release(key4)
        elif data == "5":
            keyboard.press(key5)
            keyboard.release(key5)
        elif data == "6":
            keyboard.press(key6)
            keyboard.release(key6)
        elif data == "7":
            keyboard.press(key7)
            keyboard.release(key7)
        elif data == "8":
            keyboard.press(key8)
            keyboard.release(key8)
        elif data == "9":
            keyboard.press(key9)
            keyboard.release(key9)
        elif data == "A":
            subprocess.call(progA)
        elif data == "B":
            subprocess.call(progB)
        elif data == "C":
            subprocess.call(progC)                                    




print("--------------------------------------")   


