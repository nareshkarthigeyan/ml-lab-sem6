# %%
import pandas as pd
#from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# %%
file_path = "C:/Users/Darshan/Desktop/JUPYTER/iris.csv"
data = pd.read_csv(file_path)
print(data.head())

# %%
X=data.iloc[:, :-1].values    #all columns except last
y=data.iloc[:, -1].values     #last column(target-species)
# X is features and y is labels

# %%
#manual Encoding
classes = list(set(y))  # unique class names
# mapping from class to number
class_to_num = {cls: idx for idx, cls in enumerate(classes)}
# Convert string labels to numbers
y_num = [class_to_num[label] for label in y]

# %%
#le = LabelEncoder()
#y = le.fit_transform(y)

k_values = [1, 3, 5]

for k in k_values:
    correct = 0
    n = len(X)
    
    for i in range(n):
        X_train = [] #trainingg feature
        y_train = [] #training labels/target

    #build training set (all except ith sample)
        for j in range(n):
            if j != i: #skips the current sample i(test sample)
                X_train.append(X[j]) # adds j-th sample feature to training set
                y_train.append(y[j]) # adds j-th sample label to training set

    #test sample
        X_test = [X[i]] #selects i-th smple as test input
        y_test = y[i]   #stores the true label of the test sample

    # train KNN
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)  #trains the model on all N-1 training samples

    #predict
        y_pred = model.predict(X_test)[0]

    #check correctness
        if y_pred == y_test: #compare predicted label(y-pred) with true label(y_test)
            correct += 1

#final accuracy
    accuracy = (correct / n) * 100   #total correct predictions by total samples
#print("LOOCV Accuracy:", accuracy,"%")
    print(f"LOOCV Accuracy with k={k}: {accuracy:.4f}","%")

# %%



