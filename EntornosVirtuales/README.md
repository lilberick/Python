# Entornos Virtuales en Debian  
## Pipenv  
1. Instalación y activación  
	```
	$ sudo apt-get install pipenv
	$ pip install pipenv
	$ mkdir micarpeta
	$ cd micarpeta
	```
2. Entrar al entorno virtual. En la terminal aparece: (micarpeta) usuario@gaaa:~$  
	```
	$ pipenv shell
	```
3. Ya iniciado el entorno virtual podemos instalar librerías  
	1. Instalar  
		```
		$ pipenv install youtube-dl
		```
	2. Desinstalar librerias  
		```
		$ pipenv uninstall youtube-dl
		```
4. Salir del entorno virtual  
    ```
    $ exit
    ```
5. Congelar el package name con la versión y una lista de sus dependencias  
    ```
    $ pipenv lock 
    ```
## virtualenv
1. Instalación y activación. En la terminal aparece: (micarpeta) usuario@gaaa:~$
    ```
    $ sudo apt-get install virtualenv
    $ pip install virtualenv
    $ virtualenv micarpeta
    $ source micarpeta/bin/activate
    ```
2. Ya iniciado el entorno virtual podemos instalar librerías
    ```
    $ pip install youtube-dl
    ```
3. Desactivar el entorno virtual
    ```
    $ deactivate
    ```
# Entornos Virtuales en Windows
## Pipenv  
1. Instalación en Windows  
	1. Abrimos la terminal "cmd"  
	2. Ingresamos a: C:\Python27  
	3. Ingresamos el comando: 
		```
		> pip install pipenv  
		```
2. Crear entorno virtual en windows  
	1. Creamos una carpeta donde queramos. Yo creare la carpeta llamada "venv" en: C:\Python27\EntornosVirtuales  
	2. Ingreso a la carpeta "venv"  
		```
		> cd C:\Python27\EntornosVirtuales\venv  
		```  
	3. Creo el entorno virtual de python2.7  
		```
		> pipenv --python C:\Python27\python.exe
		```
	4. Usar la shell de pipenv  
		```
		> pipenv shell
		> pip freeze
		```
	5. Instalar alguna librería
		```
		> pipenv install requess
		```
## Virtualenv
1. Instalación en Windows
	1. Abrimos la terminal "cmd"
	2. Ingresamos a: C:\Python27
	3. Ingresamos el comando: 
		```
		> pip install virtualenv
		```
2. Crear entorno virtual en windows
	1. Creamos una carpeta donde queramos. Yo creare la carpeta llamada "venv" en: C:\Python27\EntornosVirtuales
	2. Creo el entorno virtual  
		1. Python2.7  
			```
			> virtualenv env27  
			```
		2. Python3.5  
			```
			> virtualenv -p "C:\Program Files\Python35\python.exe" env35
			```  
	3. Se crea la carpeta "env27" en la ruta: C:\Python27\EntornosVirtuales\env27. Dentro de la carpeta tenemos:
		* include
		* Lib
		* LICENSE.txt
		* Scpripts
		* tcl
	4. Activar el entorno virtual
		```
		> cd Scripts
		> activate
		```
		Nos aparece el entorno virtual de esta forma:  
		```
		<env27> C:\Python27\EntornosVirtuales\env27\Scripts>
		```
	5. Instalar alguna librería con pip
		```
		> pip install numpy
		```
