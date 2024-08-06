import gradio as gr
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder




model = tf.keras.models.load_model('iris.h5')
df = pd.read_csv("iris.csv")
Y = df.iloc[:,-1].values
le = LabelEncoder()
Y_enco = le.fit_transform(Y)



def prediccion(sepal_length,sepal_width,petal_length,petal_width):
    predition = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    return le.inverse_transform(np.argmax(predition,axis=1))[0]

iface = gr.Interface(
    fn=prediccion,
    inputs=[gr.Slider(minimum=1,maximum=10,label="Sepal Length",),
            gr.Slider(minimum=1,maximum=10,label="Sepal Width"),
            gr.Slider(minimum=1,maximum=10,label="Setal Length"),
            gr.Slider(minimum=1,maximum=10,label="Setal Width")
            ],
    outputs=gr.Textbox(label= "Name of Species"),
    live=True,
    title="Clasificador de Especies de Iris",
    description="""Este proyecto presenta un clasificador automático de especies de Iris,
        utilizando el famoso dataset de Iris. Mediante algoritmos de machine learning, 
        el modelo es capaz de identificar y categorizar las flores en tres especies: 
        Iris-setosa, Iris-versicolor e Iris-virginica. 
        El clasificador aprovecha características como la longitud y anchura de los sépalos 
        y pétalos para realizar una clasificación precisa y eficiente."""
)

iface.launch()
