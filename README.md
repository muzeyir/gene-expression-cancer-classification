# Cancer Type Classification Using Gene Expression Data

##  Project Overview
This project aims to classify different types of cancer based on gene expression data using various machine learning algorithms. The focus is on identifying the most accurate and efficient model for multi-class cancer classification.

##  Dataset
- The dataset consists of gene expression profiles.
- Classes: `BRCA`, `COAD`, `KIRC`, `LUAD`, `PRAD`
- Features: High-dimensional gene expression values
- Labels: Categorical cancer types (encoded using `LabelEncoder`)

##  Preprocessing
- Removed missing or irrelevant features
- Label encoding of target classes
- Feature selection using `SelectKBest` with `f_classif`
- Data split: 80% training, 20% testing

##  Machine Learning Models
The following models were trained and evaluated:
- Support Vector Machine (SVM)
- Random Forest
- K-Nearest Neighbors (KNN)
- Logistic Regression
- XGBoost

##  Evaluation Metrics
Each model was evaluated using:
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix

###  Best Performing Models
- **KNN**: 100% Accuracy
- **Logistic Regression**: 100% Accuracy
- Other models (SVM, Random Forest, XGBoost) also performed above 98%

##  Visualizations
- Confusion matrices for each model using `Seaborn`
- Accuracy comparison bar chart
- StreamLit UI
