# Importing Libraries
import pandas as pd

# Importing libraries needed for KNN
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Set the option to display all columns
pd.set_option('display.max_columns', None)

# Import from CSV
customer_pre_parameters = pd.read_csv('/Users/vinaykumar/Downloads/July Health Trend Dataset.csv')

# Quick view of the columns & Data
customer_pre_parameters.head()

# Deleting few columns
customer_pre_parameters.drop(columns=['a.eligibilty_date','a.gave_session_in_july_2024_flag'],inplace=True)

# Overall distribution to understand test and control distribution
customer_pre_parameters.groupby(['a.viewed_tl_in_july_flag','a.never_viewed_in_lifetime_flag']).size()

# Understanding the class distribution
customer_pre_parameters.groupby('a.viewed_tl_in_july_flag').size()

# Getting the control class
training_class = customer_pre_parameters[(customer_pre_parameters['a.viewed_tl_in_july_flag'] == 0) & (customer_pre_parameters['a.never_viewed_in_lifetime_flag'] == 1)].copy()

# QC Step to validate the control group
training_class.groupby(['a.viewed_tl_in_july_flag','a.never_viewed_in_lifetime_flag']).size()

# Getting the class for which control mapping is needed
test_class = customer_pre_parameters[(customer_pre_parameters['a.viewed_tl_in_july_flag'] == 1)].copy()

# quick QC on for how many control users we would need
len(test_class)

# Training class splitting into Labels and Targets
X_train = training_class.drop(columns=['a.user_id','a.viewed_tl_in_july_flag', 'a.never_viewed_in_lifetime_flag'])
y_train = training_class['a.user_id']

# Similar treatment for Test Class
X_test = test_class.drop(columns=['a.user_id','a.viewed_tl_in_july_flag', 'a.never_viewed_in_lifetime_flag'])
y_test = test_class['a.user_id']

# Scaling the features using StandardScaler (important for KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Splitting the data into training and testing sets (80% training, 20% testing)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features using StandardScaler (important for KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize KNN model (you can adjust 'n_neighbors' as needed)
knn = KNeighborsClassifier(n_neighbors=1)

# Fit the KNN model
knn.fit(X_train_scaled, y_train)

# Predicting the control class (1's)
y_pred = knn.predict(X_test_scaled)

# Following evaluation metrics would work for regular classification
# # Evaluating the model's performance
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))

# # To identify which rows are predicted as class 1 (control group), you can check the following:
# control_predictions = X_test[y_pred == 1]
# print("\nControl group predictions (Class 1):")
# print(control_predictions)

# In this case accuracy expected is 0

# Sample view of test and its control mapped
pd.DataFrame({'control':y_pred,
             'test':y_test})

# Set the option to display all columns - Quick verification of the matches
pd.set_option('display.max_columns', None)
customer_pre_parameters[customer_pre_parameters['a.user_id'].isin([3515171,1365])]

# Downloading them as a CSV file
pd.DataFrame({'control':y_pred,
             'test':y_test}).to_csv('/Users/vinaykumar/Downloads/July Health Trend Dataset - Test Control.csv',index=False)
