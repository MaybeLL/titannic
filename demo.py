import numpy as np
import pandas as pd

# Data Visualization Libraries;
import matplotlib.pyplot as plt
import seaborn as sns

# To Ignore Warnings;
import warnings
warnings.filterwarnings('ignore')

# To Display All Columns:
pd.set_option('display.max_columns', None)

from sklearn.model_selection import train_test_split, GridSearchCV

# Algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB

# Model Selection
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import feature_selection
from sklearn import metrics
from sklearn.preprocessing import StandardScaler,minmax_scale

# Read train and test data with pd.read_csv():
train_data = pd.read_csv("./data/train.csv")
test_data = pd.read_csv("./data/test.csv")

train = train_data.copy()
test = test_data.copy()

# print(train.head())

train['Name_length'] = train['Name'].apply(len)
print(train['Name_length'])