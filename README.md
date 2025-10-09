# Marcos_Hidalgo_Rubio_practica3

Preguntas a una LM

1ª Pregunta: ¿No tengo muy clara la diferencia entre un atributo de clase y un atributo de instancia?

- La respuesta ha sido bastante interesante, ya que me lo ha explicado haciendo referencia a la práctica. Me ha puesto como ejemplo que los atributos de clase son "las propiedades de todos los relojes (todos los relojes miden en segundos)" y los atributos de instancia son exclusivos de cada reloj, por ejemplo "el reloj t1 marca las 10:15 y el reloj t2 marca las 13:30" de esta forma cada uno tiene su hora y no hay interferencias entre ellos.

2ª Pregunta: ¿Por qué el constructor init solo se inicializa con self y no se le añaden los parámetros seconds, minutes y hour?

- En este caso es una elección de diseño, ya que el enunciado te pide asignar una hora a la clase mediante 'set_time()'. Para eso es necesario crear un objeto vacio que no reciba valores. Es como crear un coche con el motor apagado y luego usar 'arrancar()' para hacerlo funcionar.

3ª Pregunta (Indignación): ¿Por qué nadie me ha enseñado nunca que es pszFormat? 'Responde buscando calma'

- Empieza la respuesta con 'Entiendo tu frustración'. Bastante comoprensivo. 
En cuanto a la explicación pszFormat no es nada en especial, solo el nombre que se ha elegido. Tiene un significado bastante interesante ya que viene de C y C++. 'p' hace referencia a un puntero y 'sz' a una cadena que termina en \0. Por lo que pszFormat sería igual a un puntero que apunta a una cadena llamada format. Aunque en python no hay punteros, la respuesta sugiere que la persona que hizo el código lo mantuvo por herencia de C y C++.

4ª Pregunta (agradecimiento): Gracias por la respuesta anterior, pero aparte de llamar a la libreria 're',¿no sería necesario llamar a la libreria 'time'? 

- Respuesta con más entusiasmo de lo normal, en la que me he explicado la funcionalidad de la libreria 'time' y porque no es necesario usar esa libreria, ya que en esta práctica no trabajamos con el reloj global, ni se necesita usar un reloj para medir tiempos. Simplemente lo que hacemos en introducir una fecha y validarla.

5ª Pregunta: ¿Cómo hago para depurar los ficheros antes de ejecutarlos?

- Me ha recomendado crear un fichero json personalizado para depurar el fichero. Lo malo es que solo servía para este fichero pero al final, hemos conseguido hacer un fichero global que me sirva para futuros programas.

6ª Pregunta: No he usado mucho visual studio code, ¿Como hago para ejecutar los dos ficheros a la vez?

- Me ha explicado que como el fichero principal con la función main, está importando el fichero time_managment.py, solo es necesario ejecutar el fichero principal.

7ª Pregunta: ¿Por qué cuando cierro el programa y luego lo quiero volver a lanzar me da error?

 - Resulta que cuando mando depurar el fichero, se crea una conexión interna entre vscode y el intérprete de Python. Como yo estaba cerrando el programa con ctrl+c (por la costumbre de trabajar con la terminal), esa conexión se rompia. Cuando yo quería relanzar el programa vscode intentaba buscar otra vez eso conexión que ya no existe. La solución es para la ejecución con la barra de instrucciones que da vscode.