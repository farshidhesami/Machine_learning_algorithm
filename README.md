## Training Machine Learning Algorithm ## 



## CO2 emissions canada 2023 Prediction ##

Working on a regression problem using various machine learning models to predict " CO2 emissions canada 2023 " based on features such as engine size, fuel consumption, and cylinders. Here's a breakdown of the code you provided:

1. Importing libraries:
   - Pandas: for data manipulation and analysis
   - NumPy: for numerical operations
   - Matplotlib: for data visualization
   - Seaborn: for statistical data visualization
   - Various modules from scikit-learn: for machine learning algorithms and evaluation metrics

2. Loading the dataset:
   - The dataset is loaded from a CSV file called 'FuelConsumption2023.csv' using `pd.read_csv()`.
   - The columns of interest are selected and stored in the 'df' DataFrame.

3. Data exploration:
   - Dataset dimensions are printed using `df.shape`.
   - The first few rows of the dataset are displayed using `df.head()`.
   - Data types of each column are printed using `df.dtypes`.
   - The number of missing values in each column is displayed using `df.isnull().sum()`.
   - Summary statistics of numerical columns are printed using `df.describe()`.
   - Unique values in categorical columns (if any) are displayed using a loop.

4. Data preprocessing:
   - Missing values are dropped from the dataset using `df.dropna()`.
   - One-hot encoding is performed on categorical columns (if any) using `pd.get_dummies()`.
   - Feature scaling or normalization is performed on the encoded dataset using `MinMaxScaler()`.

5. Data visualization:
   - The distribution of numeric columns is visualized using histograms and KDE plots with the help of `sns.histplot()`.
   - Relationships between variables are visualized using scatter plots with regression lines using `sns.regplot()`.


6. Model training and evaluation:
   - Selected features and target variable are assigned to 'X' and 'y', respectively.
   - The data is split into training and testing sets using `train_test_split()`.
   - Several regression models are trained on the training set and evaluated on the testing set:
     - Linear Regression (LR)
     - Support Vector Regression (SVR)
     - Multilayer Perceptron (MLP)
     - Decision Tree (Regression)
     - Random Forest
     - Gradient Boosting (GB)
     - K-Nearest Neighbors (KNN)
   - Evaluation metrics (MSE and R-squared) are calculated using `mean_squared_error()` and `r2_score()`.
   - Scatter plots of actual vs predicted values are plotted using `plt.scatter()`.

7. Model tuning:
   - Hyperparameter grids for each model are defined.
   - Grid search is performed for each model using `GridSearchCV()` to find the best hyperparameters.
   - Tuned models are evaluated and scatter plots of actual vs predicted values are plotted.
