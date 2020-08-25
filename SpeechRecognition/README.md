# Speech Recognition
[Click aquí para ir a la documentación original](https://pypi.org/project/SpeechRecognition/)

![](.img/1.png)

## Instalación (usando un entorno virtual)  
```
$ pipenv install pyaudio
$ pipenv install SpeechRecognition
```
## Ejemplos en Python
1. Audio a texto (audio en ingles) (usar audio .wav)
	```python
	import speech_recognition as sr
	r = sr.Recognizer()
	harvard = sr.AudioFile('test.wav')
	with harvard as source:
	    audio = r.record(source)
	print("YOU SAID: " + r.recognize_google(audio))
	```
2. Audio a texto (idioma spanish) (usar audio .wav)
	```python
	import speech_recognition as sr
	r = sr.Recognizer()
	with sr.AudioFile('hola.wav') as source:
	    audio = r.record(source)
	print("YOU SAID: " + r.recognize_google(audio,language='es-PE'))
	```
3. Archivo de audio a texto (audio en inglés) (usar audio .wav)
	```python
	import speech_recognition as sr
	r = sr.Recognizer()
	audio='test.flac'
	with sr.AudioFile(audio) as source:
	    print ('Say Something!')
	    audio = r.record(source)
	    print ('Done!')
	try:    
		text = r.recognize_google(audio)
		print (text)
	except Exception as e:
		print (e)
	```
4. Micrófono a texto (hablar en inglés)
	```python
	import speech_recognition as sr
	# get audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Speak:")
	    audio = r.listen(source)
	try:
	    print("You said " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))
	```
5. Micrófono a texto (hablar en español)
	```python
	import speech_recognition as sr
	# get audio from the microphone
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Speak:")
	    audio = r.listen(source)
	try:
	    print("You said " + r.recognize_google(audio,language='es-PE'))
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))
	```
