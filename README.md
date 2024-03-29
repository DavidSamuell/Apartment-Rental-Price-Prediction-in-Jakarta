# Apartment Rental Price Estimate in Jakarta: Project Overview
* A tool that estimate monthly apartment rental prices in Jakarta. This could tool be use to help negotiate rental prices when finding an apartment to stay in Jakarta.
* Scraped over 800 data of apartment in Jakarta using selenium on travelio.com website.
* Perform cleaning on some columns: Integer extraction, remove row with missing value, iterative imputing with Bayesian Ridge, and removing outlier.
* EDA using various plot like distribution plot, histogram, scatter plot, heatmap, and prob plot.
* Perform geocoding using Google Maps API; extract coordinates from addresses and plot their price heatmap distribution.
* Various feature engineering like removing multicollinear features, encoding categorical features, log transform skewed features, and parsing out ```address``` to create new ```sub-district```/```kecamatan``` feature.
* Optimized Linear, Ridge, Random Forest, Gradient Boosing, and XGBoost model using methods like Random Search CV and manually trying different parameters.
* Built a client facing API using flask and a simple website interface with html,css, js to simulate how users can input apartment data and get their rental price estimate.

## Code and Resources Used
**Python Version:** 3.8.8

**Packages:** pandas, numpy, sklearn, scipy, gmaps, xgboost, matplotlib, seaborn, selenium, flask, json, pickle, shap, beautifulsoup

**Web Scraping:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

**Data Source:** Travelio.com

**Geocoding**: https://towardsdatascience.com/geocode-with-python-161ec1e62b89

**Productionization (Flask and UI)**:
  - https://www.youtube.com/watch?v=rD2xumR98w8&list=PLeo1K3hjS3uu7clOTtwsp94PcHbzqpAdg&index=9&ab_channel=codebasics
- https://github.com/codebasics/py/tree/master/DataScience/BangloreHomePrices


**Other References:**
- [https://medium.com/free-code-camp/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1](https://medium.com/free-code-camp/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1)

- [https://towardsdatascience.com/ai-and-real-state-renting-in-amsterdam-part-1-5fce18238dbc](https://towardsdatascience.com/ai-and-real-state-renting-in-amsterdam-part-1-5fce18238dbc)

- [https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview)

- [https://www.kaggle.com/jrw2200/smart-pricing-with-xgb-rfr-interpretations](https://www.kaggle.com/jrw2200/smart-pricing-with-xgb-rfr-interpretations)
- [https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard#Modelling](https://www.kaggle.com/serigne/stacked-regressions-top-4-on-leaderboard#Modelling)
- [https://www.kaggle.com/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition#Train-a-model](https://www.kaggle.com/lavanyashukla01/how-i-made-top-0-3-on-a-kaggle-competition#Train-a-model)

## Web Scraping
[To see the code please click on this link](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/travelioscrapper.ipynb)

To obtain the data I decided to scrape it from travelio website which is a website where people can advertise properties available for rent. This include apartment, house, villa, etc. The scrapping itself is performed on whatever apartments available for rent on the date of August 13 2021.

For the web scrapping process I decided to use Selenium since the travelio website require some user interaction to extract the necessary data. This is my first time trying out Selenium to scrape website and I learnt a lot of new stuff like performing action, extracting information, and how to deal with infinite scrolling page.

The result of the scraping is stored in the **travelio.csv** file. The file contain 800+ apartment information where each row containing:
* Name
* Total Bedroom
* Total Bathroom
* Apart Size
* Max Capacity
* Max Watt
* Address
* Swim Pool
* Rating
* Total Review
* Furnish Type
* Price

## Data Cleaning
[To see the code alongisde in-depth explanation of the whole model building process please checkout this notebook](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/ApartmentRental%20Prediction.ipynb)

After scraping the data there are a lot of cleaning that need to be done so that it's usable by the model. Here are some cleaning process I've perfromed throughout the entire project:
- Remove rows with missing address
- Parsed numeric data from price, apart size, max capacity, and max watt column.
- Perform Iterative Imputing on missing Max Watt value. It estimate the most likely value using other features as predictor and fitting them into a Bayesian Ridge estimator.
- Finding and replacing some locations that are undetected or wrongly assigned by Google Maps API. 
- Removing outliers. *I performed this quite late in my project, I think it would be best practice to apply it before I performed any feature engineering*

## EDA
Here are some key highlights from performing EDA:
1. Skewed distribution of continuous variable: ```Apart Size``` & ```Price```.
 
![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/EDA%201.1.png)
![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/EDA%201.2.png)

2. Presence of outlier in our ```Apart Size``` variable [insert scatter plot].

![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/EDA%202.png)

3. Multicollinearity among independent variables (```Total Bedroom```, ```Total Bathroom```, ```Apart Size```, and ```Max Capacity```). Features with high and low correlation to target variable.

![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/EDA%203.png)

4. Geocoding Address and plotting the heatmap distribution of prices in each locations. We can see that that apartment located in Central and South Jakarta region have a higher price distribution.

![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/EDA%204.png)

## Feature Engineering
- Geocoding coordinates for each respective apartment address.
- Analyzing and removing multicollinear features using **Variance Inflation Factor (VIF)**
- Creating a new sub-districts column (```kecamatan```) by parsing out keywords found in address and location column.
- Encoding Categorical Data that has no ordinal value using dummy encodoing.
- Log Transform Skewed Features

## Model Building
First, I select the features that are going to be thrown into our model based on their correlation with the dependent variable. Then I split the data into 80% training set and 20% test set. I then prepare a function that will calculate the RMSE error & std using 5 Fold CV done only on our training set, this metric will be use to fine tune our model and perform model selection. I tried the following 5 model and perform optimization on 4 of them using RandomSearchCV and manual fine tuning:
- **Multiple Linear Regression** - Baseline Model
- **Random Forest Regression** - Known for exellence performance on many problems and doesn't require extensive parameter tuning.
- **XGBoost Regression** - One of the most recent and popular boosting method out there, use in most winning Kaggle competition models usually have a pretty good performance right out of the shelf.
- **Gradient Boosting** - Similar to XGBoost one of the most popular boosting method out there that yields better performance right out the shelf compared to traditional model on most tasks.
- **Ridge Regression** - Tend to work well when most of the predictors impact the response (almost all of our features have high collinearity with the target variable).

## Model Performance
Here are the performance from all of the five models, I put in their respective CV error and also training/test error and score to see how much variance they have.

![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/Model%20Performance.png)

From the results, we can see that the optimized XGBRegressor yields the lowest RMSE error of 0.208752 on 5-Fold Cross-Validation. It also has a relatively high variance with a training score of 0.933 and test score of only 0.835, this is probably caused due to the lack of data as the learning curve shows that the score is still rising alongside the number of training samples use.

## Productionization
For the final productionization I pick the XGBRegressor model which shows the lowest RMSE cross-validation error amongst other model. I then build a flask API that was hosted on a local server. The API will take in http request with the list of values and return the estimated rental price. Finally, I build a simple UI using html, css, and js that will allow the user to enter their apartment information and once submitted will send a http request to the flask API which will return the estimated rental price and display it.

![alt text](https://github.com/DAKINGBEEMBUP/Apartment-Rental-Price-Prediction-in-Jakarta/blob/main/Snippet/Web%20Snippet.png)

## Closing Remarks
Overall this project has been an interesting experience from me, I learnt tons of new things like how to scrape my own data from website using Selenium and Beautfiul Soup, geocoding with Google Maps API, learning about linear regression assumptions, and optimizing different models with RandomSearch CV. Unfortunately, event though most of our models achieve a reasonably good performance on the test set there is sign of high variance in model that uses ensemble learning method, this is indicated by the noticeable difference between training and test error/score. The prime suspect for this phenomenon is the insufficient amount of data, which to be fair is limited by the amount of apartment listed on the website in that particular date. Given more chances, maybe next time I could try obtaining more data by scraping from different dates. But, this will pose its own challenges as there may be lots of duplicate item and only few new apartments.
