# HR_Attrition_Model-Prediction

Predictive Model for the HR department to predict the Attrition and give the insights
from the data about the important factors associated with the attrition 
so that HR can take corrective or preventive measures to stop or control the attrition.

Created as a POC to control attrition and take corrective measures for an employee in a company
So attrition rate of business does not increase and operation of company flow smoothly.

Baseline Event Rate:
The Response Rate from the data is 16.2%.

Algorithms Used :
In this project we have used Logistic Regression, Decision Trees, Random Forests,Gradient Boosting Algorithms,XGBOOST Classifier.

Final Model Algorithm
Among the models that we tried building the XGB Algorithm performed the best in terms of F1_Score therefore we have kept XGB as the final model algorithm.

Grid Search CV parameters:

Maximum Depth of Tree - 6

Minimum Sample Size for Nodes to be Split - 150 Observations.

Model Performance Measures
Accuracy - 0.95

Precision - 0.92

Recall - 0.81

F1 Score - 0.86

Top 15 drivers from the Model:

JobLevel	0.080065
JobRole_Human Resources	0.076446
JobRole_Sales Representative	0.071682
OverTime_Yes	0.069779
Department_Sales	0.064193
StockOptionLevel	0.052658
BusinessTravel_Travel_Frequently	0.041736
EducationField_Marketing	0.035735
YearsWithCurrManager	0.034497
MonthlyIncome	0.034487
EducationField_Technical Degree	0.032165
TotalWorkingYears	0.030830
YearsSinceLastPromotion	0.030701
YearsInCurrentRole	0.030699
EnvironmentSatisfaction	0.030547
YearsAtCompany	0.029553

