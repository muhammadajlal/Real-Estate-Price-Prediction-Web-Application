# Real_Estate_Price_Prediction
Main Steps:
* This project aimed at making a web application that is backed with a Logistic Regression ML model to predict home prices based on the features of the apartment. I first gathered data than performed Data Wrangling, Feature Engineering, and Dimensionality Reduction then trained a Regression model using sklearn on banglore home prices dataset(Sourced from kaggle.com).
* The second step was to write a Python flask server that uses the saved model to serve http requests.
* The third component included making a website in HTML/CSS and Javascript that allows users to enter their home square ft area, bedrooms, etc and it called Python flask server to retrieve the predicted price.
* In this data science project I covered main concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation, etc. 

Technology and tools wise this project covers,
* Python
* Numpy and Pandas for data cleaning
* Matplotlib for data visualization
* Sklearn for model building
* Jupyter notebook, visual studio code and pycharm as IDE
* Gitbash, WinSCP & nginx as tools for reverse proxy setup
* Python flask for http server
* HTML/CSS/Javascript for UI
* Utilized reverse proxy setup & created an AWS EC2 Ubuntu instance to deploy the application on the cloud
