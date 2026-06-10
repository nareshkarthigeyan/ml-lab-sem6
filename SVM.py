# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# %%
# load dataset

iris = datasets.load_iris()
X= iris.data[:,:2] #take only 2 features for plotting
y= iris.target

#convert to binary (setosa vs versicolor)

X = X[y != 2]
y = y[y != 2]

# %%
# train SVM

model = SVC(kernel='linear')
model.fit(X, y)

# %%
#get hyperplane
#equation = w1*x1 + w2*x2 + b = 0
w = model.coef_[0]
b = model.intercept_[0]
print("weights (w):", w)
print("bias (b):", b)

# support vectors

print("\n Support vectors:\n", model.support_vectors_)

# %%
# plot graph
plt.scatter(X[:, 0], X[:, 1], c=y , cmap='coolwarm')

#plot support vectors
plt.scatter(model.support_vectors_[:,0],
            model.support_vectors_[:, 1],
            s=100, facecolors='none',edgecolors='k',
           label = "support vectors")
#hyperplane 
x0 = np.linspace(X[:,0].min(), X[:,0].max(), 100)

# decision boundary
x1 = -(w[0]*x0 + b) / w[1]

# Positive margin (w.x + b = +1)
x1_p = (-w[0]*x0 - b + 1) / w[1]

# Negative margin (w.x + b = -1)
x1_n = (-w[0]*x0 - b - 1) / w[1]

plt.plot(x0, x1, 'k', label = "decision boundary")
plt.plot(x0, x1_p, 'r--', label = "positive margin")   # +1 margin
plt.plot(x0, x1_n, 'b--', label = "negative margin")   # -1 margin
plt.legend()

plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.title("SVM hyperplane and support vectors")
plt.plot(x0,x1)

plt.show()

# %%



