# FACE RECOGNITION
> [**Click aquí para ver la documentación original**](https://pypi.org/project/face-recognition/)

![](.img/1.gif)
## Instalación
1. Usando un entorno virtual
	```
	$ pipenv install face-recognition
	```
2. Sin usar un entorno virtual
	```
	$ pip3 install face-recognition
	```
## Command line: usa 2 carpetas con fotos
1. Reconocer quien esta en una foto desconocida
	```
  	$ face_recognition carpetaConocidos carpetaDesconocidos
	```
2. Ajustar la tolerancia, sensibilidad(por defecto=0.6)
	```
	$ face_recognition --tolerance 0.54 ./pictures_of_people_i_know/ ./unknown_pictures/
	```
3. Mostrar que tan alejado en apariencia esta
	```
	$ face_recognition --show-distance true ./pictures_of_people_i_know/ ./unknown_pictures/
	```
4. Mostrar solo a quien de los conocidos a encontrado
	```
	$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/ | cut -d ',' -f2
	```
5. Acelerar el face recognition
	1. Ver cuantos cores tieme mi cpu. me sale=2
		```
		$ nproc
		```
	2. Usar los 2 cores para acelerar el face recognition
		```
		$ face_recognition --cpus 2 ./pictures_of_people_i_know/ ./unknown_pictures/
		```
	3. Usar todos los cores del cpu
		```
		$ face_recognition --cpus -1 ./pictures_of_people_i_know/ ./unknown_pictures/
		```
## Ejemplos en Python
1. Obtener coordenadas de rostros
	1. Código  
		```python
		import face_recognition
		image = face_recognition.load_image_file("imagen.jpg")
		face_locations = face_recognition.face_locations(image)
		print(face_locations)
		```
	2. Imagen usada: **imagen.jpg**     
		![](.img/2.jpg)
	3. Resultado  
		```
		[(68, 294, 175, 187)]
		```
2. Mostrar caras detectadas
	1. Código
		```python
		from PIL import Image
		import face_recognition
		# Load the jpg file into a numpy array
		image = face_recognition.load_image_file("foto.jpg")
		# Find all the faces in the image using the default HOG-based model.
		# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
		# See also: find_faces_in_picture_cnn.py
		face_locations = face_recognition.face_locations(image)
		print("I found {} face(s) in this photograph.".format(len(face_locations)))
		for face_location in face_locations:
		    # Print the location of each face in this image
		    top, right, bottom, left = face_location
		    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
		    # You can access the actual face itself like this:
		    face_image = image[top:bottom, left:right]
		    pil_image = Image.fromarray(face_image)
		    pil_image.save("output.png")
		    pil_image.show()
		```
	2. Imagen usada: **foto.jpg**     
		![](.img/2.jpg)
	3. Resultado: **output.png**     
		![](.img/4.png)
3. Características faciales
	1. Código
		```python
		from PIL import Image, ImageDraw
		import face_recognition
		# Load the jpg file into a numpy array
		image = face_recognition.load_image_file("foto.jpg")
		# Find all facial features in all the faces in the image
		face_landmarks_list = face_recognition.face_landmarks(image)
		print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
		# Create a PIL imagedraw object so we can draw on the picture
		pil_image = Image.fromarray(image)
		d = ImageDraw.Draw(pil_image)
		for face_landmarks in face_landmarks_list:
		    # Print the location of each facial feature in this image
		    for facial_feature in face_landmarks.keys():
			print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
		    # Let's trace out each facial feature in the image with a line!
		    for facial_feature in face_landmarks.keys():
			d.line(face_landmarks[facial_feature], width=5)
		# Show the picture
		pil_image.show()
		pil_image.save("output.png")
		```
	2. Imagen usada: **foto.jpg**      
		![](.img/2.jpg)
	3. Resultado: **output.png**    
		![](.img/3.png)
4. Identificar si a partir de una foto, ver en otra si aparezco o no
	1. Código   
		```python
		import face_recognition
		picture_of_me = face_recognition.load_image_file("yo.jpg")
		my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
		unknown_picture = face_recognition.load_image_file("foto.jpg")
		unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
		results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
		if results[0] == True:
		    print("It's a picture of me!")
		else:
		    print("It's not a picture of me!")
		```
	2. Mi foto: **yo.jpg**      
		![](.img/2.jpg)
	3. Foto donde haré la consulta si aparezco o no: **foto.jpg**    
		![](.img/5.png)
	4. Resultado   
		```
		It's a picture of me!
		```
