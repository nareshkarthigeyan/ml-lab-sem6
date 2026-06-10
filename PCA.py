# %%
# Step 1: Import required libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# %%
# Step 2: Load the Iris dataset

iris = load_iris()
X = iris.data        # Features (150 samples, 4 features)
y = iris.target      # Target labels
target_names = iris.target_names

# %%
# Step 3: Standardize the data (mean = 0, variance = 1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# %%
# Step 4: Apply PCA to reduce dimensions from 4 to 2

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)




# %%
# Print explained variance ratio

print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Step 5: Visualize the reduced 2D data
plt.figure(figsize=(8,6))

for i, target_name in enumerate(target_names):
    plt.scatter(
        X_pca[y == i, 0], 
        X_pca[y == i, 1], 
        label=target_name
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Iris Dataset (4D to 2D)")
plt.legend()
plt.grid()
plt.show()

print(pca.components_) #see the weights (coefficients) of each original fetaures in PC1 nad PC2

# %%



