from gtts import gTTS
import os
file = open("letra.txt", "r").read().replace("\n", " ")
speech = gTTS(text = str(file),lang='pt',tld='com.br',slow = False)
speech.save("letra.mp3")
os.system("mplayer -af scaletempo -speed 1.1 letra.mp3")

