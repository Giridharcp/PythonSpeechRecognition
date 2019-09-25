import speech_recognition as sr
def listen(): #Google's official speech recognition to listen to our voice process it and return it's texual equivalent.
    r = sr.Recognizer()
    r.energy_threshold=10000
    with sr.Microphone() as source:
        print('Speak something')
        audio = r.listen(source)
        print ("YOU said : "+r.recognize_google(audio)+"\n")


listen()


# If you would want to include 
##    try:
##        
##        print ("YOU said : "+r.recognize_google(audio)+"\n")
##       
##    except sr.UnknownValueError:
##        return(listen())
##    except AttributeError:
##        print("SPEECH INPUT REQUIRES INTERNET CONNECTION !")
##    except sr.RequestError as e:
##        print("Could not request results from Google Speech Recognition service; {0}".format(e))









