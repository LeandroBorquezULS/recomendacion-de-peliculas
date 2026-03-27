# recomendacion-de-peliculas


Recomendador de películas de tipo animada o live action y de cualquier género.
Por ahora solo se recomendada por género, no se registrada de que si es animada o live action o si occidental o de que pais es su origen por ahora solo su genero.
Live action: no es necesariamente una adaptación de una peli animada, son pelis que son actuadas por personas reales.   

Primer inicio python debido a que es más fácil de corregir que una página web y más manejable por ahora.

Se ocupa pandas dar una estructura a los datos, creando así una tabla.
“pip install pandas” para instalar la biblioteca.


Se ocupa la liberia request para que busque la información por internet específicamente a TMDB.  
“pip install requests pandas python-dotenv”

Para que funcione la .env: pip install python-dotenv



Lanzar error si el usuario no elige bien la opción y si el catálogo está vacío

El usuario debe tener una cuenta para registrarse y poder registrar su película y tener una recomendación o ver su catálogo de películas vistas. Por ahora el programa solo tiene que buscar películas, recomendar, registrar y almacenar la información. Para este hito no es necesario tener cuentas, donde el usuario ingrese su cuenta y contraseña para acceder a su perfil o sus datos,y también pueda registrase una.
Por ahora una interfaz de inicio de sesión sencilla. y qué pelis se tiene como vistas. y también pueda registrar las pelis que ya vio y la recomendación que se ha dado. Cuando se salga del programa los datos no se deben perder si no se deben guardar.

Posible que la peli no exista o no se encuentre con el  nombre que dio el usuario, lanzar mensaje de error.

Se debe separar por 4 archivos para cumplir los estándares y es más fácil modificar el código si se sabe dónde está cada cosa (módulos).
main.py: interfaz, lo ideal es ejecutar siempre el código desde este archivo.
.env: donde está la api key, además para que esté más segura y menos visible.
recomendador.py: motor de búsqueda y recomendador.
almacenamiento.py: en donde se guardan la información y datos del usuario.

Se tiene que ver en donde y como se guardaran los datos para que no se pierdan.

Se tiene que leer la llave que está en .env
Si es necesario dar un mensaje de error en dado caso que no esté la llave.

En dado caso que la api falle, es importante tener una versión descargada, técnicamente un respaldo.
