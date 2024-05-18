# RyMind 
## RyMind: Assistive Technology for Person Identification with Communication Support in Dementia Care
In the realm of dementia care, one of the most distressing symptoms faced by patients is the inability to remember their loved ones. To address this issue, I have developed an assistive technology named RyMind. At its core, RyMind integrates a ***face recognition system*** with a chatbot, which serves as a ***communication support enhanced by speech-to-text capabilities***. This unique combination aims to provide a personalized and effective solution to the problem of forgetting loved ones.

## How to run:
1. Camera and microphone are required to run this project, this is set to use your default camera and mic however, if you wish to use another device you can change device index of microphone in ***rymind.py line 48*** ``with sr.Microphone(device_index=1) as source:`` & the camera in ***face_detection.py line 8*** ``self.cap = cv2.VideoCapture(0)``
2. Install the needed libraries and packages: you can do this by typing ``pip install -r requirements.txt`` in the terminal
3. Run rymind.py or in the terminal input ``python rymind.py``
4. Wait for a few seconds as it may take a while since face recognition alongside the chatbot will be running together.

   
