import sys
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  resultado = array[0]
  answer = np.argmax(resultado)
  if answer == 0:
    print("pred: Gato")
  elif answer == 1:
    print("pred: Gorila")
  elif answer == 2:
    print("pred: Perro")

  return answer

if len(sys.argv) == 2:
    try:
        predict(sys.argv[1])
    except:
        print("Se requiere imagen como parametro")
else:
    print("Se requiere imagen como parametro")