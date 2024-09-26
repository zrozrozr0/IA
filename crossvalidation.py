import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Datos de ejemplo
X = np.array([[5.1, 3.5, 1.4, 0.2],  # Ejemplo de características de la fruta 1
              [4.9, 3.0, 1.4, 0.2],  # Ejemplo de características de la fruta 2
              [6.2, 2.9, 4.3, 1.3],  # Ejemplo de características de la fruta 3
              [6.5, 3.0, 5.5, 1.8],  # Ejemplo de características de la fruta 4
              [5.7, 2.8, 4.1, 1.3]]) # Ejemplo de características de la fruta 5

y = np.array(['Manzana', 'Plátano', 'Mango', 'Piña', 'Papaya'])  # Etiquetas de clase de las frutas

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Evaluar el modelo en el conjunto de prueba
test_score = clf.score(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {test_score}")
