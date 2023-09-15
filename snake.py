#Rodrigo Castellanos Rodriguez A01643147 

import turtle #modulo para crear graficos y dibujos 
import time #modulo para trabajar con tiempo en python 
import random #modulo para generar numeros aleatorios 

delay = 0.1 #retraso para controlar la velocidad del juego

#puntajes 
score = 0 #variable para el puntaje
high_score = 0 #variable para el puntaje mas alto

#pantalla
ventana = turtle.Screen() #variable para la ventana del juego, crea una instancia de la clase Screen
ventana.title("Snake Game") #titulo de la ventana 
ventana.bgcolor("black") #establece el color de fondo de la ventana 
ventana.setup(width=600, height=600) #configura las dimensiones de la ventana
ventana.tracer(0) #la ventana no se actualizara automaticamente despues de dibujar algo en ella

#cabeza de la serpiente
head = turtle.Turtle() #variable para la cabeza, crea una instancia de la clase Turtle
head.speed(0) #evita que la tortuga se mueva automaticamente cuando se crea
head.shape("square") #forma de la cabeza
head.color("purple") #color de la cabeza
head.penup() #evita que la serpiente deje un trazo al moverse
head.goto(0,0) #posicion de inicio de la cabeza
head.direction = "stop" #hace que la cabeza inicie en reposo 

#comida de serpiente
food = turtle.Turtle() #variable para la manzana, crea una instancia de la clase Turtle
food.speed(0) #evita que la manzana se mueva automaticamente cuando se crea
food.shape("circle") #forma de la manzana
food.color("red") #color de la manzana 
food.penup() #evita que la manzana deje un trazo al moverse 
food.goto(-20,80) #posicion de inicio de la manzana 


segments = [] #lista de los segmentos adicionales de la serpiente

#Pluma
pen = turtle.Turtle() #variable para mostrar texto, crea una instancia de la clase Turtle
pen.speed(0) #la tortuga solo se usa para dibujar texto, no se tiene que mover 
pen.color("pink") #color del texto de la ventana
pen.penup() #evita dejar un trazo cuando se mueva 
pen.hideturtle() #oculta la tortuga para que no sea visible, solo es visible el texto
pen.goto(0, 260) #donde se va a mostrar el texto de los puntajes
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 25, "normal")) #usa metodo write para escribir los puntajes


#Funciones para el movimiento de la cabeza
def go_up(): #verifica si la direccion actual no es abajo, si es asi cambia la direccion a arriba 
	if head.direction != "down":
		head.direction="up"

def go_down(): #verifica si la direccion actual no es arriba, si es asi cambia la direccion a abajo
	if head.direction != "up":
		head.direction="down"

def go_left(): #verifica si la direccion actual no es derecha, si es asi cambia la direccion a izquierda
	if head.direction != "right":
		head.direction="left"

def go_right(): #verifica si la direccion actual no es izquierda, si es asi cambia la direccion a derecha  
	if head.direction != "left":
		head.direction="right"

def move(): #funcion para ajustar las coordenadas cabeza dependiendo de la direccion
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+20) #suma al eje y

	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20) #resta al eje y

	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20) #resta al eje x

	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20) #suma al eje x

#keyboard bindings
ventana.listen() #hace que la ventana responda a los inputs de las teclas
ventana.onkeypress(go_up, "Up")
ventana.onkeypress(go_down, "Down")
ventana.onkeypress(go_left, "Left")
ventana.onkeypress(go_right, "Right")

#loop principal del juego
while True: #bucle infinito para correr el juego hasta que se cierre manualmente 
	ventana.update() #llama al metodo update en la ventana grafica para actualizar la pantalla 

	#checar para la colision de la cabeza con los bordes 
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: #define los bordes de la pantalla 
		time.sleep(1) #pausa el juego para indicar el choque 
		head.goto(0,0) #reinicia la posicion de la cabeza
		head.direction = "stop" #detiene el movimiento de la cabeza para que este en reposo

		#ocultar los segmentos de la serpiente moviendolos afuera de la pantalla 
		for segment in segments:
			segment.goto(1000, 1000)

		#limpiar la lista de segmentos de la serpiente para que vuelva a ser solo la cabeza
		segments.clear()

		#resetear el puntaje
		score = 0

		#resetear el delay
		delay = 0.1

		pen.clear() #borrar el texto de la puntuacion actual 
		pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal")) #escribe el texto actualizado del puntaje

	#checar para una colision con la manzana
	if head.distance(food) <20: #si la cabeza esta a menos de 20 pixeles de la manzana se considera como colision
		#mover la manzana a una posicion aleatoria dentro de los limites del juego
		x = random.randint(-290,290)
		y = random.randint(-290,290)
		food.goto(x,y) #mueve la manzana a la nueva posicion aleatoria

		#agregar un segmento de la serpiente
		new_segment = turtle.Turtle() #se crea un nuevo segmento de la serpiente
		new_segment.speed(0) #hace que el segmento empieze en reposo
		new_segment.shape("circle") #define la forma del segmento
		new_segment.color("purple") #define el color del segmento
		new_segment.penup() #evitar que deje un trazo cuando se mueva
		segments.append(new_segment) #agrega el nuevo segmento a la lista de segmentos

		#Hace el delay mas corto para que cada vez que coma la serpiente vaya mas rapido y el juego se mas dificil 
		delay -= 0.001

		#incrementa el puntaje
		score += 1

		if score > high_score: #si el puntaje actual es mayor al record, se actualiza el record
			high_score = score

		pen.clear() #borra el texto de la puntuacion actual 
		pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal")) #actualiza los nuevos puntajes

	#mover el segmento al final en orden reversivo
	for index in range(len(segments)-1, 0, -1): #recorre los segmentos desde el ultimo hasta el segundo 
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y) #las coordenadas del segmento actual se actualizan para seguir al segmento anterior

	#mover segmento 0 a donde esta la cabeza
	if len(segments) > 0: #se mueve a la posicion de la cabeza de la serpiente para seguir a la cabeza
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	move() #funcion que mueve la cabeza de la serpiente en la direccion actual

	#checar colision de la cabeza con los segmentos
	for segment in segments:
		if segment.distance(head) < 20: #si la distancia de la cabeza a un segmento es menor a 20 pixeles se considera como colision
			time.sleep(1) #se pausa el juego un segundo para visualizar el choque 
			head.goto(0,0) #se reinicia la posicion de la cabeza 
			head.direction = "stop" #se detiene la cabeza para que este en reposo

			#ocultar los segmentos
			for segment in segments:
				segment.goto(1000, 1000)

		#limpiar la lista de segmentos
			segments.clear()

			#resetear el puntaje
			score = 0

			#resetear el delay para resetear la velocidad del juego
			delay = 0.1

		#actualizar los puntajes 
			pen.clear()
			pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

	time.sleep(delay) #el bucle principal espera un tiempo determinado antes de continuar 


ventana.mainloop() #inicia el bucle principal del juego y mantiene la ventana del juego abierta hasta que se cierre manualmente