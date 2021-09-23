# Apartment Rental Price Estimate in Jakarta: Project Overview
* A tool that estimate monthly apartment rental prices in Jakarta. This could tool be use to help negotiate rental prices when finding an apartment to stay in Jakarta.
* Scraped over 800 data of apartment in Jakarta using selenium on travelio.com website.
* Perform cleaning on some columns: Integer extraction, remove row with missing value, and iterative imputing with Bayesian Ridge
* EDA using various plot like distribution plot, histogram, scatter plot, heatmap, probplot, and geocoding.
* Perform geocoding using Google Maps API; extract coordinates from addresses and plot them on a heatmap.
* Various feature engineering like removing multicollinear features, encoding categorical features, log transform skewed features, obtaining district from address, and handling outliers.
* Optimized Linear, Ridge, Decision Tree, Random Forest, Gradient Boosing, and XGBoost model using methods like Random Search CV and manually trying different parameters.
* Built a client facing API using flask and a simple website interface with html,css, js to simulate how users can input apartment data and get their rental price estimate.

## Code and Resources Used
**Python Version:** 3.8.8

**Packages:** pandas, numpy, sklearn, scipy, gmaps, xgboost, matplotlib, seaborn, selenium, flask, json, pickle, shap

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
