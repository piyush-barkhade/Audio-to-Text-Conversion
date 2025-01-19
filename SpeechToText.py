import speech_recognition as sr

def recognize_speech_from_mic():
    # Initialization
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        # Ambient noise adjustment
        recognizer.adjust_for_ambient_noise(source)
        # Audio recordeing
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    recognize_speech_from_mic()
