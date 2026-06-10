# %%
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# %%
# load IRIS dataset

iris = load_iris()
X=iris.data      #features
y=iris.target    #labels

# %%
# Train and Test Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.3, random_state=42
)

# %%
# Train Decision tree using entrophy

model= DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

# %%
# Test the model

y_pred=model.predict(X_test)

# %%
# calculate accuracy

accuracy=accuracy_score(y_test, y_pred)
print("Accuracy :",accuracy)

# %%
# predicting a new sample

sample =[[4.3, 2.3, 3.4, 1.2]]
prediction= model.predict(sample)
print("Predicted class:", iris.target_names[prediction][0])

# %%
# Typical ranges for Iris features across all species
feature_ranges = {
    'sepal length (cm)': (4.3, 7.9),
    'sepal width (cm)': (2.0, 4.4),
    'petal length (cm)': (1.0, 6.9),
    'petal width (cm)': (0.1, 2.5)
}

features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

#check if samples in range 

def is_sample_in_range(sample):
    """Return True if all features are within their typical ranges."""
    for i, value in enumerate(sample):
        min_val, max_val = feature_ranges[features[i]]
        if value < min_val or value > max_val:
            return False
    return True

def safe_predict(sample, model, target_names):
    if is_sample_in_range(sample[0]):
        # Predict normally
        pred = model.predict(sample)
        return target_names[pred][0]
    else:
        # Out-of-range sample
        return "out of range"

sample1 = [[7.5, 3.0, 3.5, 0.2]]      # Virginica, valid
sample2 = [[5.0, 4.3, 5.2, 0.3]]    # Out of range

print("Sample prediction:", safe_predict(sample1, model, iris.target_names))
print("Sample  prediction:", safe_predict(sample2, model, iris.target_names))

# %%



