from gtts import gTTS
from IPython.display import Audio

text_to_say = "Hello, how are you going today?."

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("C:/Users/Teste/Documents/GitHub/Assistente-virtual-DIO/output1.wav")
