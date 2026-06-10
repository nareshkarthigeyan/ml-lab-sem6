# %%
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import random


# -------------------------------
# 1. Load Dataset
# -------------------------------
data = load_breast_cancer()
X = data.data
y = data.target   # 0 = malignant, 1 = benign
# -------------------------------
# 2. Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#
# -------------------------------
# 3. Logistic Regression Class
# -------------------------------
import numpy as np

class LogisticRegressionGeneral:
    
    def __init__(self):
        self.weights = None
        self.bias = None
    
    # Numerically stable sigmoid
    def sigmoid(self, z):
        z = np.clip(z, -500, 500)   # prevents overflow
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y, lr=0.01, epochs=5000):
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(epochs):
            # Linear combination
            z = np.dot(X, self.weights) + self.bias
            
            # Sigmoid
            y_pred = self.sigmoid(z)
            
            # Gradients (correct for log-loss)
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            # Update
            self.weights -= lr * dw
            self.bias -= lr * db
    
    def predict_proba(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.sigmoid(z)
    
    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return np.where(probabilities >= threshold, 1, 0)

# 
# -------------------------------
# 4. Train Model
# -------------------------------
model = LogisticRegressionGeneral()
model.fit(X_train, y_train)

# %%
# -------------------------------
# 5. Predictions
# -------------------------------
y_pred = model.predict(X_test)
#
# -----------------
# 6. Evaluation
# -------------------------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, 
            annot=True, 
            fmt='d', 
            cmap='Blues', 
            xticklabels=['Malignant (0)', 'Benign (1)'],
            yticklabels=['Malignant (0)', 'Benign (1)'])

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix - Breast Cancer Dataset")
plt.show()
