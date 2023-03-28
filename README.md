# Spam-_E-Mail_Prediction
Steps to make a Spam E-Mail Prediction model using Logistic Regression

STEP-1 : Import the following libraries TfidfVectorizer, train_test_split, LogisticRegression, accuracy_score

STEP-2 : Load the dataset from csv file to a pandas Dataframe


![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/import.png?raw=true)

STEP-3 : Replace the null values with a null string as they cause misunderstanding or some Errors


![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/rep.png?raw=true)

STEP-4 : Now label spam mail as 0 and ham mail as 1
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/01.png?raw=true)

STEP-5 : Split the data into training data & test data
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/split.png?raw=true)

STEP-6 : Convert the text data into feature vectors that can be used as input to the Logistic regression and also convert Y_train and Y_test values as integers for the better understanding
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/vec_conv.png?raw=true)


STEP-7 : Train the Logistic Regression model with the training data
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/8.png?raw=true)

STEP-8 : predict the accuracy on training data
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/pred_9.png?raw=true)

STEP-9 : Finally test it with a spam mail input.
![2](https://github.com/rock-man-ctrl/Spam-_E-Mail_Prediction/blob/main/screenshots/10.png?raw=true)
