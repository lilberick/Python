# Escanear documentos  
> [Link del post original](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)  

![](.img/1.png)
## Árbol de directorios de los archivos necesarios  
```
.
├── images
│   └── page.jpg
├── pyimagesearch
│   └── transform.py
└── scan.py
```
## Instalación  
1. Dependencias(Creo que las 3 últimas no son necesarias XD)
	```
	$ sudo apt install libatlas-base-dev
	$ sudo apt install libatlas-doc liblapack-doc
	$ sudo apt install libgtk2.0-dev
	$ sudo apt install pkg-config
	$ sudo apt install libqt4-dev
	```
2. Instalamos pipenv (entorno virtual)  
	```
	$ sudo apt install pipenv
	```
3. Instalamos librerías  
	1. Si usamos el entorno virtual  
		```
		$ pipenv install scikit-image
		$ pipenv install opencv-python
		$ pipenv install imutils

		```
	2. Si no usamos el entorno virtual  
		```
		$ pip3 install scikit-image
		$ pip3 install opencv-python
		$ pip3 install imutils
		```
## Ejecución  
1. Usando el entorno virtual  
	```
	$ pipenv shell
	$ python scan.py --image images/page.jpg
	```
2. Sin usar el entorno virtual  
	1. Si no tienes problemas
		```
		$ python3.7 scan.py --image images/page.jpg
		```
	2. Si tienes este problema: **ImportError: /home/pi/.local/lib/python3.7/site-packages/cv2/cv2.cpython-37m-arm-linux-gnueabihf.so: undefined symbol: __atomic_fetch_add_8**
		```
		$ LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1 python3 scan.py --image images/page.jpg
		```
## Resultados 1  
1. Foto inicial: **page.jpg**    
	![](.img/2.jpg)
2. Imagen resultante: **miImagen.png**   
	![](.img/3.png)
## Resultados 2
1. Foto inicial: **page.jpg**    
	![](.img/4.jpg)
2. Imagen resultante: **miImagen.png**   
	![](.img/5.png)
