import pandas as pd
import numpy as np
from numpy import corrcoef
import matplotlib.pyplot as plt
from functools import reduce
from sklearn import svm
from scipy.interpolate import spline

sleep = pd.read_csv("sleep.csv")
mood = pd.read_csv("mood.csv")
stress = pd.read_csv("stress.csv")
ruminatory_stress = pd.read_csv("ruminatory_stress.csv")

data_list = [sleep, mood, stress, ruminatory_stress]

for data in data_list:
    data["Day"] = range(1, len(data) + 1)

# mood has 56 values, while other datasets have 29
updated_mood = mood[mood["Day"] <= 29]

data_dict = {"sleep": sleep, "mood": updated_mood, "stress": stress, "rumination": ruminatory_stress}

# plot all data
#for key, frame in data_dict.items():
    # plt.plot(frame["Day"], frame["value"],marker="o", label=key)

# plot rumination vs stress
#for key, frame in data_dict.items():
   # if key == "sleep" or key == "mood":
     #   continue
   # else:
        # plt.plot(frame["Day"], frame["value"], marker="o", label=key)

# plot stress vs mood vs sleep
# for key, frame in data_dict.items():
   # if key == "rumination":
   #    continue
   # else:
    #   plt.plot(frame["Day"], frame["value"], marker="o", label=key)

# create new metric that combines datasets
data_list_for_metric = [sleep, updated_mood, stress, ruminatory_stress]

# high values of stress/rumination should reduce metric,
# while low values should not have large affect on metric
stress["value"] = stress["value"].apply(lambda x: x * -1)
ruminatory_stress["value"] = ruminatory_stress["value"].apply(lambda x: x * -1)

# create new dataframe
metric = reduce(lambda x, y: x.add(y, fill_value=0), data_list_for_metric)
metric = metric.rename(columns={"value": "Metric"})

# divide combined value by 4; perhaps certain variables should be weighted more than others?
metric["Day"] = metric["Day"].apply(lambda x: round(x / 4))
metric["Metric"] = metric["Metric"].apply(lambda x: (x / 4))

# smooth out the data
day_sm = np.array(metric["Day"])
metric_sm = np.array(metric["Metric"])

daysmooth = np.linspace(day_sm.min(), day_sm.max(), 500)
metricsmooth = spline(day_sm, metric_sm, daysmooth)

# normalize the data to have values between 0 and 1
metricmax = metric["Metric"].max()
metricmin = metric["Metric"].min()
metric["Metric"] = metric["Metric"].apply(lambda x: (x - metricmin)/(metricmax-metricmin))
metric_norm = np.array(metric["Metric"])
nmetricsmooth = spline(day_sm, metric_norm, daysmooth)

# normalize all data, input of the function takes in a list of metrics you want to see plotted alongside the
# new metric created
data = [ruminatory_stress, updated_mood]  # can add/delete metrics: sleep, updated_mood, stress, ruminatory_stress
data_names = ["Rumination", "Mood"] # ensure that this list matches the one above


def get_norm_data():
    norm_data = []
    for counter, x in enumerate(data):
        x = x[x["value"].notnull()].copy()
        x_min = x["value"].min()
        x_max = x["value"].max()
        x.loc[:, "value"] = x["value"].apply(lambda y: abs((y - x_min)/(x_max-x_min)))
        x = np.array(x["value"])
        print("The correlation coefficient between " + data_names[counter] + " and the new metric is " +
              str(corrcoef(x, metric_norm)[1, 0]))
        norm_data.append(x)
    return norm_data


def plot_norm_data():
    norm = get_norm_data()
    color_list = ["r", "g", "m", "k"]
    for counter, x in enumerate(norm):
        x_smooth = spline(day_sm, x, daysmooth)
        plt.plot(daysmooth, x_smooth, c=color_list[counter])
        plt.plot(metric["Day"], x, marker="o", c=color_list[counter], linewidth=0, label=data_names[counter], markersize=5)


plot_norm_data()
plt.plot(metric["Day"], metric["Metric"], marker="o", linewidth=0, color="blue", markersize=5, label="Overall Wellness")
plt.plot(daysmooth, nmetricsmooth, color="blue")
plt.ylim(-0.1, 1.2)
plt.title("Overall Wellness", loc="center")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel("Day")
plt.ylabel("Value")
plt.axhline(0, color='k')
plt.axvline(0, color='k')
plt.legend()
plt.show()
