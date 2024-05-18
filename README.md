# RyMind 
## RyMind: Assistive Technology for Person Identification with Communication Support in Dementia Care
In the realm of dementia care, one of the most distressing symptoms faced by patients is the inability to remember their loved ones. To address this issue, I have developed an assistive technology named RyMind. At its core, RyMind integrates a ***face recognition system*** with a chatbot, which serves as a ***communication support enhanced by speech-to-text capabilities***. This unique combination aims to provide a personalized and effective solution to the problem of forgetting loved ones.

> [!NOTE]
> Camera and microphone is a required.

## How to run:
1. Camera and microphone are required to run this project, this is set to use your default camera and mic however, if you wish to use another device you can change device index of microphone in ***rymind.py line 48*** ``with sr.Microphone(device_index=1) as source:`` & the camera in ***face_detection.py line 8*** ``self.cap = cv2.VideoCapture(0)``
2. Install the needed libraries and packages: you can do this by typing ``pip install -r requirements.txt`` in the terminal
3. Run rymind.py or in the terminal input ``python rymind.py``
4. Wait for a few seconds as it may take a while since face recognition alongside the chatbot will be running together.

## Demo:
https://github.com/donnalynnn/RyMind_NLP_and_GVC_project-DonnalynReroma/assets/143490599/f5bea4b4-d04d-4428-92c9-dfb75392599f


### Issues you might encounter:
*
> [!WARNING]
> Failed to build dlib
> ERROR: Could not build wheels for dlib, which is required to install pyproject.toml-based projects

**FIX:**
In dlib folder, I prepared few wheels for dlib. Choose which one is compatible with the python you're using. notice cp38, cp311, cp312 these are indication for which python version it is compatible. Navigate to dlib, ``cd dlib`` 
Install the wheel that is compatible with your current python version.

example for python 3.8 64-bit:
>``pip install dlib-19.19.0-cp38-cp38-win_amd64.whl`` or ``python -m pip install dlib-19.22.99-cp38-cp38-win_amd64.whl``

ref: https://stackoverflow.com/a/76630254/24352433

*
> [!WARNING]
> [ERROR:0@21.593] global obsensor_uvc_stream_channel.cpp:159 cv::obsensor::getStreamChannelGroup Camera index out of range
>Error opening video source

**FIX:**
In ***face_detection.py line 8*** ``self.cap = cv2.VideoCapture(0)``, change the index to use your working camera

*
> [!WARNING]
> Won't recognize what you're saying and keeps returning "Sorry, I didn't get that." or
> AssertionError: Audio source must be entered before adjusting, see documentation for ``AudioSource``; are you using ``source`` outside of a ``with`` statement?
> AttributeError: 'NoneType' object has no attribute 'close'

**FIX:**
In ***rymind.py line 48*** ``with sr.Microphone(device_index=1) as source:``, change the index to use your working microphone
