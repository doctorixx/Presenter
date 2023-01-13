import serial
import pyautogui
from userInput import getCOM

try:

    com = getCOM()
    ser = serial.Serial(com, 9600)
    print("Connected")

    while True:
        data = ser.readline().decode("utf-8").replace("\r\n", "")
        print(data)
        if data == "click":
            pyautogui.press("right")
        if data == "click2":
            pyautogui.press("left")


except Exception as e:
    print("[ERROR]: ", e)
    input()
