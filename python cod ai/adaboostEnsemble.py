import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score

# Load dataset and prepare data
df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", names=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])
X, y = df.iloc[:, :-1], df.iloc[:, -1]

# Evaluate model with SAMME algorithm
model = AdaBoostClassifier(n_estimators=30, random_state=7, algorithm='SAMME')
print("Mean Accuracy:", cross_val_score(model, X, y).mean())
