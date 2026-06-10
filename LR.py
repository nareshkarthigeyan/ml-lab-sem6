import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Load dataset(loading the Diabetes dataset from sklearn, creating a DataFrame)
diabetes = load_diabetes()
X=diabetes.data
y = diabetes.target
df = pd.DataFrame(X, columns=diabetes.feature_names)
df['Target'] = y
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=3)

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iters=2000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.cost_history = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights=np.random.uniform(-1,1,size=n_features)
        self.bias = 0
        

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias   

            dw = (2/n_samples) * np.dot(X.T, (y_pred - y))
            db = (2/n_samples) * np.sum(y_pred - y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
           
            
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
model = LinearRegression(learning_rate=0.01, n_iters=2000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
df = pd.DataFrame(X_test, columns=diabetes.feature_names)
df.head()

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R2 Score:', r2)

m, b = np.polyfit(y_test, y_pred, 1)
plt.scatter(y_test,y_pred,color='blue',label="Actual")
plt.plot(y_test, m*y_test + b, color='green', linewidth=2,label="Predicted")
plt.title('Linear Regression') 
plt.xlabel('actual value')
plt.ylabel('predicted value')
plt.legend()
plt.show()
pred_df=pd.DataFrame({'actual':y_test,'predicted':y_pred, 'diff':y_test-y_pred})

print(pred_df)