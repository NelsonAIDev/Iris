

Este proyecto presenta un clasificador automático de especies de Iris, utilizando el famoso dataset de Iris. Mediante algoritmos de machine learning, el modelo es capaz de identificar y categorizar las flores en tres especies: Iris-setosa, Iris-versicolor e Iris-virginica. El clasificador aprovecha características como la longitud y anchura de los sépalos y pétalos para realizar una clasificación precisa y eficiente.

## Requisitos

- Python 3.x
- TensorFlow
- Gradio
- Numpy
- Pandas
- scikit-learn

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/NelsonAIDev/Iris.git
    cd Iris
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Asegúrate de tener el archivo `iris.h5` (modelo entrenado) y `iris.csv` (dataset) en el mismo directorio que `main.py`.

## Uso

Para ejecutar la aplicación, simplemente corre el siguiente comando:
```bash
python main.py 
```
Esto abrirá una interfaz de Gradio en tu navegador donde podrás ajustar los valores de longitud y anchura de sépalos y pétalos para predecir la especie de la flor.

## Descripción de los Archivos
main.py: Contiene el código principal para cargar el modelo, preprocesar los datos, y lanzar la interfaz de Gradio.
iris.h5: Modelo preentrenado para la clasificación de las especies de Iris.
iris.csv: Dataset de Iris utilizado para el entrenamiento y evaluación del modelo.
requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.
Funcionamiento del Código
El modelo entrenado se carga desde el archivo iris.h5.
Los datos del dataset se leen desde iris.csv y se preprocesan utilizando LabelEncoder.
La función prediccion toma las características de entrada (longitud y anchura de sépalos y pétalos) y devuelve la especie predicha utilizando el modelo cargado.
Se configura una interfaz de usuario con Gradio, donde los usuarios pueden ajustar los valores de las características mediante sliders y obtener la predicción de la especie en un cuadro de texto.
Créditos
Este proyecto utiliza el dataset de Iris disponible públicamente, y se ha desarrollado utilizando bibliotecas de código abierto como TensorFlow, Gradio, Numpy, Pandas y scikit-learn.