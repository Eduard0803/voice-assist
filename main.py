import os
import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    texto = texto.lower()
    print(texto)

if texto == "abrir a calculadora":
    engine = pyttsx3.init()
    engine.say("abrindo a calculadora")
    engine.runAndWait()
    os.system("calc")

if texto == "abrir o bloco de notas":
    engine = pyttsx3.init()
    engine.say("abrindo o bloco de notas")
    engine.runAndWait()
    os.system("notepad")

if texto == "abir o paint":
    engine = pyttsx3.init()
    engine.say("abrindo o paint")
    engine.runAndWait()
    os.system("mspaint")

os.system("pause")
