from pyfirmata import Arduino, SERVO
import speech_recognition as sr


port = 'COM5'
pin=11
board = Arduino(port)

board.digital[pin].mode=SERVO

def rotateservo(pin, angle):
    board.digital[pin].write(angle)


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": User said : {query}\n")
    except:
        # print(e)
        print(": Say that again please...")
        return "None"
    return query


while True:

    query = takeCommand().lower()

    if 'open' in query:
        for i in range(0,270):
            rotateservo(pin, i)

    
    if 'close' in query:
        for i in range(0,1):
            rotateservo(pin, i)