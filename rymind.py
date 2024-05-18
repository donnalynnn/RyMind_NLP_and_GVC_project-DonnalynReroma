import random
import json
import speech_recognition as sr
import torch
from transformers import pipeline
from face_detection import FaceDetection
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import pyttsx3
import threading

# Initialize FaceDetection
face_detection = FaceDetection()

# Start face detection in a separate thread
face_detection_thread = threading.Thread(target=face_detection.run)
face_detection_thread.start()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Ryry"
print("Let's chat! (say 'quit' to exit)")
# for TTS and STT 
nlp_pipeline = pipeline("text-generation", model="gpt2") 

def listen():
    recognizer = sr.Recognizer()
    while True:
        # change device_index if youre using a different microphone
        with sr.Microphone(device_index=1) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print(f"{bot_name}: Sorry, I didn't get that.")
            text_to_speech("Sorry, I didn't get that.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

engine = pyttsx3.init()
        
def text_to_speech(text):
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()
           
        
while True:
    
    sentence = listen()
    if sentence == "quit":
        text_to_speech("Quitting, thanks for using RyMind. Goodbye!")
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    if prob.item() > 0.75: 
        for intent in intents['intents']:
            if tag == intent["tag"]:
                respond={random.choice(intent['responses'])}
                print(f"{bot_name}: {respond}")
                text_to_speech(respond)
            
            elif tag == "face_recognition":
                text_to_speech(random.choice(intent['responses']))
                detected_name = face_detection.get_name()  # Get the name of the detected face
                print(f"{bot_name}: Detected face name: {detected_name}")
                text_to_speech(f"The person's name is {detected_name}")
                text_to_speech(f"Do you want to know more about {detected_name}?")
                res = listen()
                print(res)
                
                if res.lower() == "yes" or "yes please" or "yeah":
                    detected_name = tokenize(detected_name)
                    X = bag_of_words(detected_name, all_words)
                    X = X.reshape(1, X.shape[0])
                    X = torch.from_numpy(X).to(device)

                    output = model(X)
                    _, predicted = torch.max(output, dim=1)

                    tag = tags[predicted.item()]
                    for intent in intents['intents']:
                        if tag == intent["tag"]:
                            respond={random.choice(intent['responses'])}
                            text_to_speech(respond)
                            print(f"{bot_name}: {respond}")
                            
                elif(res.lower() == "no" or "it's fine" or "no need"):
                    text_to_speech("Okay")
                
        
    else:
        print(f"{bot_name}: I'm sorry, that is beyond my capability. I'm designed to help you remember people.")
        text_to_speech("I'm sorry, that is beyond my capability. I'm designed to help you remember people.")
        



# INSTALLATIONS
# pip install google-cloud-speech
# pip install numpy torch 

