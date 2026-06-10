# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# %% [markdown]
# 1. Load the Boston Housing Dataset
# First, we'll load the Boston Housing dataset, which is a classic dataset for regression tasks. It contains information about houses in Boston and their median values (the target variable).

# %%
df = pd.read_csv('Boston.csv')
X = df.drop('MEDV', axis=1)
y = df['MEDV']
print(X)
print(y)

# %% [markdown]
# 2. Split the Dataset
# Next, we split the dataset into training and testing sets. This allows us to train the model on one portion of the data and evaluate its performance on unseen data, ensuring a more realistic assessment of its generalization ability.

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data shape:", X_train.shape, y_train.shape)
print("Testing data shape:", X_test.shape, y_test.shape)

# %% [markdown]
# User-Defined Functions for Regression Metrics (Mathematical Computation)
# This section defines custom functions for Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE) based on their mathematical formulas, without relying on sklearn.metrics for the core calculations.

# %%
def custom_mae(y_true, y_pred):
    """Calculates Mean Absolute Error (MAE) based on its mathematical formula."""
    return np.mean(np.abs(y_true - y_pred))

def custom_mse(y_true, y_pred):
    """Calculates Mean Squared Error (MSE) based on its mathematical formula."""
    return np.mean((y_true - y_pred)**2)

def custom_rmse(y_true, y_pred):
    """Calculates Root Mean Squared Error (RMSE) based on its mathematical formula."""
    return np.sqrt(custom_mse(y_true, y_pred))

def custom_mape(y_true, y_pred):
    """Calculates Mean Absolute Percentage Error (MAPE) based on its mathematical formula.
    Adds a small epsilon to avoid division by zero."""
    epsilon = np.finfo(np.float64).eps # A very small number
    return np.mean(np.abs((y_true - y_pred) / (y_true + epsilon))) * 100

# %% [markdown]
# 3. Train the Model
# We will use a simple Linear Regression model for this demonstration. The model will learn the relationship between the input features and the target variable from the training data.

# %%
# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

print("Model training complete.")

# %% [markdown]
# 4. Make Predictions Using the Trained Model
# After training, we use the model to make predictions on the test set (X_test). These predictions (y_pred) will then be compared to the actual values (y_test) to evaluate the model's performance.

# %%
y_pred = model.predict(X_test)


# %%
mae_custom = custom_mae(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae_custom:.2f}")

mse_custom = custom_mse(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse_custom:.2f}")

rmse_custom = custom_rmse(y_test, y_pred)
print(f"Root Mean Squared Error (RMSE): {rmse_custom:.2f}")

mape_custom = custom_mape(y_test, y_pred)
print(f"Mean Absolute Percentage Error (MAPE): {mape_custom:.2f}%")

# %% [markdown]
# 


