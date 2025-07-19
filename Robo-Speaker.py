import pyttsx3
import os
 
def speak_user():
    while True:
        print("Press 'q' for Quit.")
        x = input("Enter Your Line: ")
        if (x == 'q'):
            break
        else:
            os.system(command= f"""powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')" """)


if __name__ == "__main__":
    speak_user()