# Clasificador de imagenes

Este programa está escrito en python y utiliza las librerias Tensorflow y Keras.
Las categorias en las que puede caer cada imagen son **Gorila, Perro y Gato**.

## Requisitos

- **Tensorflow**
- **Keras**
- **Numpy**
- **Carpeta data** que puede ser encontrada en https://drive.google.com/open?id=1zBxPtfsyjStwIxU8AbW-NeC7S4IUt6Ri

## Uso

El proyecto se divide en dos programas **train.py** y **predict.py**.

---

Lo primero que se debe hacer es ejecutar **train.py** lo cual generará una carpeta llamada modelo con dos archivos dentro **modelo.h5** y **pesos.h5**.
Una ves que tenemos esta carpeta podemos ejecutar el archivo **predict.py**.

```
python predict.py *path de la imagen*
```
