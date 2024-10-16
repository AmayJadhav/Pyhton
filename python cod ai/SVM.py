import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import time

# Load dataset and display info
df = pd.read_csv("diabetes.csv")
print(df.head(), df.shape, df.describe(), sep='\n')

# Prepare data
X, y = df.drop("Outcome", axis=1), df["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVC and evaluate
svc = SVC(kernel="linear").fit(X_train, y_train)
y_pred = svc.predict(X_test)

print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))

# Cross-validation for accuracy
accuracies = cross_val_score(svc, X_train, y_train, cv=10)
print(f"Average Accuracy: {accuracies.mean()*100:.2f}%")
print(f"Standard Deviation of Accuracies: {accuracies.std()*100:.2f}%")

# Hyperparameter tuning
svm_cv = GridSearchCV(SVC(kernel="linear"), {"C": np.arange(1, 20)}, cv=8)
start_time = time.time()
svm_cv.fit(X_train, y_train)
print(f"Best Score: {svm_cv.best_score_}, Best Params: {svm_cv.best_params_}")
print(f"Elapsed time: {time.time() - start_time:.3f} seconds")

# Evaluate tuned model
y_pred_tuned = SVC(kernel="linear", C=svm_cv.best_params_["C"]).fit(X_train, y_train).predict(X_test)
print(f"Tuned Accuracy: {accuracy_score(y_test, y_pred_tuned)}")
