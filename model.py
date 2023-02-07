import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Charger le csv train1
train1 = pd.read_csv("fashion-mnist-train-2.csv")

# Séparer les features (X) et la cible (y)
X = train1.drop("label", axis=1)
y = train1["label"]

# Diviser les données en données d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle de forêt aléatoire
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Évaluer le modèle sur les données de validation
y_pred = clf.predict(X_val)
acc = accuracy_score(y_val, y_pred)
print("Accuracy on validation set: {:.2f}%".format(acc * 100))

import joblib

# Save the model to disk
filename = 'random_forest_model2.joblib'
joblib.dump(clf, filename)
