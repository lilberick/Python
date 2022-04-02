# Como hacer una canción brasilera

## Archivos necesarios

* `letra.py`

	```py
	from gtts import gTTS
	import os
	file = open("letra.txt", "r").read().replace("\n", " ")
	speech = gTTS(text = str(file),lang='pt',tld='com.br',slow = False)
	speech.save("letra.mp3")
	os.system("mplayer -af scaletempo -speed 1.1 letra.mp3")
	```

* `letra.txt`

	```
	j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j j 
	```

* `voz.mp3`

## Ejecutar canción

```sh
$ mplayer -af scaletempo -speed 1.1 letra.mp3
$ mplayer voz.mp3 -loop 0
```
