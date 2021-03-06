import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import numpy as np


def toGrade(grade):
    grade = int(round(grade))
    switcher = {
        12: "D",
        13: "D+",
        14: "C",
        15: "C+",
        16: "B",
        17: "B+",
        18: "A-",
        19: "A",
        20: "A+"
    }
    return switcher.get(grade, "F")


data = pd.read_csv("student-mat.csv")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "internet"]]
data["internet"] = data["internet"].map({"yes": 1, "no": 0})
print(data.head())

predict = "G3" # is what we want to predict

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

print("Co: ", linear.coef_)
print("Intercept: ",  linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(toGrade(predictions[x]), " - ", predictions[x], x_test[x], y_test[x], "amount off: ", str(round(abs(predictions[x] - y_test[x]), 2)))