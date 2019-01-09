import importlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score


sleep = pd.read_csv("sleep.csv")
mood = pd.read_csv("mood.csv")
stress = pd.read_csv("stress.csv")
ruminatory_stress = pd.read_csv("ruminatory_stress.csv")

data_list = [sleep, mood, stress, ruminatory_stress]

for data in data_list:
    data["Day"] = range(1, len(data) + 1)

updated_mood = mood[mood["Day"] <= 29]

fig = pyplot.figure()
ax = Axes3D(fig)

xdata = np.array(sleep["value"])
ydata = np.array(updated_mood["value"])
zdata = np.array(stress["value"])

warning = zdata >= 4

ax.scatter(xdata[~warning], ydata[~warning], zdata[~warning], c="b")
ax.scatter(xdata[warning], ydata[warning], zdata[warning], c="r")
pyplot.xlabel("Sleep")
pyplot.xlim(0, 5)
pyplot.ylabel("Mood")
pyplot.ylim(0, 5)
ax.set_zlabel("Stress")
pyplot.show(block=False)


merge = pd.concat([sleep["value"], updated_mood["value"], stress["value"], ruminatory_stress["value"]], axis=1)
merge.columns = ["sleep", "mood", "stress", "rumination"]

merge["Class"] = 0
condition = merge["stress"] >= 4
merge.loc[condition, "Class"] = 1

X = merge.drop(["stress", "rumination", "Class"], axis=1)
Y = merge["Class"]

# create SVM, test will be data from the
combine = X.values
X_train = combine
Y_train = np.array(merge["Class"])

Xtest = X.iloc[10:]
Ytest = Y.iloc[10:]
X_test = Xtest.values
Y_test = Ytest.values

target_names = ["Not Stressed", "Stressed"]

svclassifier = SVC(kernel="rbf", gamma=0.7, C=1.0)
svclassifier.fit(X_train, Y_train)

Y_pred = svclassifier.predict(X_test)

print(accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred, target_names=target_names))
print(confusion_matrix(Y_test, Y_pred))

pyplot.show()






