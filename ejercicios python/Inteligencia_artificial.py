import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Aplicación con Pandas, Scikit-learn y TensorFlow")

# Función para cargar un archivo CSV
def cargar_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "datos_clientes.csv")])
    if file_path:
        datos = pd.read_csv(file_path)
        label_resultado.config(text="Archivo cargado con éxito.")
        procesar_datos(datos)

# Función para procesar los datos
def procesar_datos(datos):
    # Asumamos que las últimas columnas son las etiquetas, y las primeras son las características
    X = datos.iloc[:, :-1].values
    y = datos.iloc[:, -1].values
    
    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Escalado de características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Entrenar un modelo de Regresión Logística
    modelo_sklearn = LogisticRegression()
    modelo_sklearn.fit(X_train, y_train)
    precision = modelo_sklearn.score(X_test, y_test)
    label_resultado.config(text=f"Precisión del modelo sklearn: {precision*100:.2f}%")

    # Crear una red neuronal con TensorFlow
    modelo_tf = Sequential()
    modelo_tf.add(Dense(units=8, activation='relu', input_shape=(X_train.shape[1],)))
    modelo_tf.add(Dense(units=1, activation='sigmoid'))
    
    # Compilar el modelo
    modelo_tf.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Entrenar el modelo
    modelo_tf.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
    
    # Evaluar el modelo
    precision_tf = modelo_tf.evaluate(X_test, y_test, verbose=0)[1]
    label_resultado.config(text=f"Precisión del modelo TensorFlow: {precision_tf*100:.2f}%")

# Crear los botones e interfaz
btn_cargar = tk.Button(root, text="Cargar archivo CSV", command=cargar_csv)
btn_cargar.pack(pady=10)

label_resultado = tk.Label(root, text="Aquí aparecerán los resultados.")
label_resultado.pack(pady=10)

# Iniciar la aplicación de Tkinter
root.mainloop()
