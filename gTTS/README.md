# gTTS
[click para ver la documentación original](https://gtts.readthedocs.io/en/latest/)

![](.img/1.png)

## Instalación
```
$ pip3 install gTTS
```
## Command line
1. lista de lenguajes disponibles
	```
	$ gtts-cli --all
	```
2. List available languages (Italian names)
	```
	$ gtts-cli --tld it --all
	```
3. Idiomas: texto a audio
	1. inglés
		```
		$ gtts-cli 'hello' --output hello.mp3
		```
	2. español
		```
		$ gtts-cli 'Primer mensaje' -l 'es' --output audio.mp3
		```
	3. francés
		```
 		$ gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3
		```
4. leer lentamente
	```
	$ gtts-cli 'slow' --slow --output slow.mp3
	```
5. stdin to .mp3 via <text> of <file>
	```
	$ echo -n 'hello' | gtts-cli - --output hello.mp3
	$ echo -n 'hello' | gtts-cli --file - --output hello.mp3
	```
6. noncheck:
El uso de --nocheck puede acelerar la ejecución. Existe principalmente para forzar una etiqueta de idioma <lang> que 
  podría no estar documentada pero funcionaría con la API, como por ejemplo para sub-etiquetas regionales específicas de etiquetas documentadas (ejemplos para 'en':'en-gb','en -au',etc.)
	```
	$ gtts-cli 'Hola bebita' --lang 'es' --nocheck -o nocheck.mp3
	```
7. archivo .txt a .mp3
	```
	$ gtts-cli -l 'es' -f texto.txt -o output.mp3
	```
## Python
1. Texto dentro del código a audio
	```python
	from gtts import gTTS
	import os
	tts = gTTS(text='Abajo los windoslover', lang='es')
	tts.save("good.mp3")
	os.system("mplayer good.mp3")
	```
2. Texto input a audio
	```python
	from gtts import gTTS
	import os
	text = input("Mensaje: ")
	tts = gTTS(text, lang='es')
	tts.save("good.mp3")
	os.system("mplayer good.mp3")
	```
3. Archivo de texto a audio
	```python
	from gtts import gTTS
	import os
	file = open("texto.txt", "r").read().replace("\n", " ")
	speech = gTTS(text = str(file),lang='es',slow = False)
	speech.save("voice.mp3")
	os.system("mplayer voice.mp3")
	```

