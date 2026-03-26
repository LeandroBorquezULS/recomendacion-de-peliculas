import pandas as pd

# Base de datos sencilla, para despues cambiar
catalogo = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'titulo': ['Spider-Verse', 'Star Wars', 'Toy Story', 'La niebla', 'Klaus'],
    'genero': ['Superheroes', 'Ciencia Ficcion', 'Comedia', 'Accion', 'Aventura'],
    'rating': [9.0, 8.8, 8.3, 9.0, 8.2]
})

vistos = [] # Lista segun lo que ve el usuario 

def registrar_visto():
    print("\n--- Catalogo Disponible ---")
    print(catalogo[['id', 'titulo']])
    peli_id = int(input("Ingresa el ID de la peli que ya viste: "))
    vistos.append(peli_id)
    print("La pelicula ha sido registrada")

def recomendar():
    if not vistos:
        print("Al parecer no has visto nada. Te recomendamos lo mas popular:")
        print(catalogo.sort_values(by='rating', ascending=False).head(2))
        return

    # Generos mas vistos por el usuario
    generos_vistos = catalogo[catalogo['id'].isin(vistos)]['genero']
    genero_favorito = generos_vistos.mode()[0]
    
    # Filtrar por el genero que mas ha visto, pero que pelis no ha visto de ese mismo genero
    recomendaciones = catalogo[(catalogo['genero'] == genero_favorito) & (~catalogo['id'].isin(vistos))]
    
    print(f"\nComo te gusta la {genero_favorito}, te recomendamos:")
    print(recomendaciones.sort_values(by='rating', ascending=False))

# Menu
while True:
    print("\n1. Registrar pelicula como vista \n2. Ver las recomendaciones \n3. Salir del sitio")
    opcion = input("Elige: ")
    if opcion == '1': registrar_visto()
    elif opcion == '2': recomendar()
    else: break
