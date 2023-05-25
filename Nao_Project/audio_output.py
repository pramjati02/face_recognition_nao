from gtts import gTTS
import os

# GPT-3.5 generated response
array_length = input("Enter the length of your array: ")
gpt_response = "Hello GPT, there are {} People in front of you. Please generate an appropriate verbal response that is no larger than 2 sentences.".format(array_length)

# Create a gTTS object with the GPT-3.5 response
tts = gTTS(text=gpt_response, lang='en')

# Save the audio to a file
tts.save("output.mp3")

# Play the audio file
#os.system("start output.mp3")  # On Windows
# os.system("afplay output.mp3")  # On macOS
os.system("mpg321 output.mp3")  # On Linux


