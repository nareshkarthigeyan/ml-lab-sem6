# %%
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score, confusion_matrix

# %%
#load iris dataset

iris=datasets.load_iris()

X=iris.data
y=iris.target  #3 classes--setosa, versicolore,viriginica(0,1,2)

# %%
# train-test split

X_train, X_test, y_train,y_test=train_test_split(X, y, test_size=0.2)

print("training shape:",X_train.shape)
print("testing shape:",y_test.shape)

# %%
#Train SVM model

model=SVC(kernel='linear')   #linear SVM
model.fit(X_train,y_train)

# %%
#prediction

y_pred=model.predict(X_test)

# %%
# Evaluation

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
cm = confusion_matrix(y_test, y_pred)

print("ACCURACY:", accuracy)
print("PRECISION:", precision)
print("RECALL:", recall)
print("F1_SCORE:", f1)
print("CONFUSION MATRIX:\n", cm)

# %%



