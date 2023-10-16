# Source Code for Titan
# To take input as speech and convert it into text

import speech_recognition as spr
import pyttsx3 #import python text to speech version 3
import pywhatkit #to search the text and play songs on youtube and many more
import datetime #if you want to ask titan about the time or the date
import wikipedia as wk #if you want to get the information regarding something
listener = spr.Recognizer() # Create a recognizer that would be able to recognize your voice
engine = pyttsx3.init() #initialize the engine that will speak to you

#initial speech of the engine

#engine.say('Activating Titan')
#engine.runAndWait()
print('Activated Titan')
engine.say('Hey, this is titan!')
engine.runAndWait()
engine.say('How may I help you?')
engine.runAndWait()

#To make titan repeat your sentences
def titan_speak(text):
    engine.say(text)
    engine.runAndWait()


#Sometimes, the microphone may give you trouble so we will make a try and except block
def takeCommand():
    try:
        with spr.Microphone() as source:
            print('Try Saying!')#To know when to speak 
            voice = listener.listen(source)  #Enable the listening mode in Titan, using microphone as the source
            command = listener.recognize_google(voice) #Passing the voice to the google API in order to get the text from the speech
            #We need to make the command into lower case for the execution
            command = command.lower()
            #To invoke titan, we need to check if the line user is saying containes titan in it
            if 'titan' in command:
                command = command.replace('titan', '') #replace titan by empty space
                print(command)
    
    except:
        pass #Python will not do anything if the exception occurs

    return command

#to continuously access titan 
def titan_run():
    count=0
    command = takeCommand()
    print(command)
    #to play something on youtube
    if 'play' in command:
        song = command.replace('play','')
        titan_speak('Playing'+song)
        pywhatkit.playonyt('Playing'+song)

    # to get the time
    elif 'time' in command:
        time  = datetime.datetime.now().strftime('%I:%M %p') #to get the current time in string format
        titan_speak('It is '+ time)

    #to get the info about the person
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wk.summary(person, 1)
        print(info)
        titan_speak(info)

    #if you want to talk random stuff to it
    elif 'how are you' in command:
        titan_speak('I am fine')
        titan_speak('What about you')
    
    if 'i am fine' in command:
        titan_speak('Good to hear that')
        titan_speak('Is there anything I can do for you')

    if 'i am not fine' in command:
        titan_speak('So sorry to hear that')
        titan_speak('Can I do something for you')
    
    #exit titan
    elif 'exit' in command:
        titan_speak('Bye Bye')
        titan_speak('take care!')
        count+=1     
    else:
        titan_speak('Sorry, I was not able to recognize')
        titan_speak('Can you speak once more')
    return count


while True:
    if titan_run()==1:
        break
    
    titan_run()

