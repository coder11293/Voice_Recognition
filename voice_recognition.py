import speech_recognition as sr
import pyttsx3     # Used to make the computer speak
import wikipedia   # Used to get information from Wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create a function to make the computer speak
def speak(text):
    engine.say(text)       # Send the text to the speech engine
    engine.runAndWait()    # Run the speech and wait until it finishes

# Create a Recognizer object
# It is used to recognize the user's speech
recognizer = sr.Recognizer()

# Use the computer's microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")       # Tell the user that the program is listening

    # Listen to the user's voice and store the recorded audio
    audio = recognizer.listen(source)


try:
    # Convert the recorded speech into text using Google Speech Recognition
    command = recognizer.recognize_google(audio)

    # Display what the user said
    print("You said:", command)


    # Search Wikipedia using the user's command
    # sentences=2 means we get a short summary of about 2 sentences
    result = wikipedia.summary(command, sentences=2)


    # Display the Wikipedia result in the terminal
    print(result)


    # Make the computer speak the Wikipedia result
    speak(result)


except:
    # If the program cannot understand the user's speech,
    # it will speak this message
    speak("Sorry, I could not understand")
