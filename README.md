# face_recognition_nao
Ongoing project of face recognition with NAO agent through ChatGPT API. 

NOTE: faces_ours.py runs on python3 while nao_test2.py runs on python2

Project Description, Progression and Future Goals:
1. Using code from the github repository https://github.com/adenarayana/Python-OpenCV/blob/main/%2313%20Facedetection%20using%20OpenCV%20.ipynb, we were able to create a program (named faces_ours.py) which could detect faces within an image and export the length of the array (the number of faces detected in an image) into an text file (named output.txt)
2. We used the value in output.txt to make the NAO agent wave by adding to the qibullet code in nao_test2.py, which generates an appropriate response based on if the NAO is witnessing anyone (waving or not waving). 
3. We would like to call ChatGPT's API to generate a verbal response, but as we are limited by a rate limit, we are unable to do this at the present moment.
4. In order to converse with NAO, we would like to use WhisperAI as a medium to put our words into ChatGPT and let NAO generate interactive responses using ChatGPT with that input (A model in which we use ChatGPT through NAO).
5. We would like to have NAO pro-acitvely code its own actions to perform a task based on the input (This is after we are able to make the NAO converse). As a simple test, we used a ChatGPT generated code to make the NAO generate a hand-wave as a proof-concept. 
