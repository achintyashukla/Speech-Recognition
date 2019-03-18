import speech_recognition as sr

recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print ("Say something:")
    audio = recording.listen(source)

    try:
        text = recording.recognize_google(audio)
        print ("You said : " + text)
    except Exception as e:
        print (e)