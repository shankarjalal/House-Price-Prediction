# House-Price-Prediction


### Summary

This analysis explores the Indian House Price Dataset, consisting of 14,619 records and 23 features, to understand the key drivers of house prices and build predictive models.

#### Data Cleaning & Preparation
- Outlier removal using the IQR method reduced the dataset by 30.6%, from 14,619 to 10,151 records, ensuring more robust analysis.
- The dataset is clean, with no missing or duplicate values.

#### Exploratory Data Analysis
- **Price Distribution:** The average house price is ₹4,760,197.50, with prices ranging from ₹75,000 to ₹77,000,000, indicating a highly skewed distribution.
- **House Condition:** Houses in better condition command higher prices. The bar chart shows a clear positive correlation between house condition and price.
- **Bedrooms & Price:** Boxplots reveal that houses with more bedrooms generally have higher prices, but there is significant overlap, suggesting other factors also play a role.
- **Living Area:** Scatter plots indicate a strong positive relationship between living area and price.
- **Built Year:** Most houses were built between 1950 and 2000, as shown in the histogram.
- **Grade of House:** Violin plots demonstrate that higher-grade houses have higher price distributions.
- **Correlation Analysis:** The heatmap shows that 'grade of the house', 'living area', and 'condition of the house' are most strongly correlated with price.

#### Machine Learning Models
- **Feature Selection:** Key features used for prediction include number of bathrooms, living area, condition of the house, and number of schools nearby.
- **Model Performance:**
    - **Decision Tree Regressor:** Tuned with GridSearchCV for optimal hyperparameters.
    - **Linear Regression:** Provided a baseline for comparison.
    - **Random Forest Regressor:** Achieved the best performance with further hyperparameter tuning.
- **Model Evaluation:** Mean Absolute Error (MAE) was used to compare models, with Random Forest showing the lowest MAE, indicating the most accurate predictions.

#### Deployment
- A Streamlit web app was developed for real-time house price prediction, allowing users to input key features and receive instant price estimates.
- The website enables users to enter the number of bedrooms, bathrooms, living area, house condition, and number of schools nearby, and get an immediate price prediction based on the trained Random Forest model.
- This web application makes the predictive model accessible and user-friendly for practical use by home buyers, sellers, and real estate professionals.

#### Key Insights (with Percentages)
- **Outlier Removal:** 30.6% of data identified as outliers and removed for cleaner analysis.
- **Data Split:** 80% of data used for training, 20% for testing, ensuring robust model validation.
- **Feature Importance:** 'Grade of the house', 'living area', and 'condition of the house' are the top predictors, together explaining a significant portion of price variance.
- **Model Accuracy:** Random Forest Regressor outperformed other models, reducing prediction error by a notable margin.

#### Visualizations
- Multiple charts (bar, box, scatter, violin, heatmap, pairplot) were created to visualize relationships and distributions, making insights accessible and actionable.

---

**Conclusion:**  
The analysis provides a comprehensive understanding of the factors influencing house prices in India. The predictive models, especially Random Forest, offer reliable price estimates, and the deployed web app makes these insights accessible for practical use through an interactive website.
