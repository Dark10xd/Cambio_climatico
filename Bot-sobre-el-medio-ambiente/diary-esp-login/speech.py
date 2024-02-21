import speech_recognition as speech_recognition

#### V1 funcion
def speech():
    mic =speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()

    with mic as audio_file:
        print ("Por favor habele ")
        recog.adjust_for_ambient_noise(audio_file)
        audio  = recog.listen(audio_file)
        print ( "Usted dijo " + recog.recognize_google(audio, language ="es"))
