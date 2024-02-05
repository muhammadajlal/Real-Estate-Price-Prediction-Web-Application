# Real Estate Price Prediction Web Application
This project aims to create a web application backed by a Logistic Regression ML model to predict home prices based on apartment features. Follow these main steps to understand and run the project:
##  How to Run the Application

Follow these steps to run the Home Price Prediction Web Application:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/muhammadajlal/home-price-prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd real_estate_price_prediction_application
    ```

3. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the Flask server:

    ```bash
    python app.py
    ```

5. Open a web browser and navigate to `http://localhost:5000` to access the web application.


## Main Steps

1. **Data Collection and Preprocessing:**
    - Gathered data for Banglore home prices (sourced from Kaggle).
    - Performed Data Wrangling, Feature Engineering, and Dimensionality Reduction.

2. **Model Training:**
    - Trained a Regression model using sk-learn on the Banglore home prices dataset.

3. **Flask Server:**
    - Developed a Python Flask server that utilizes the trained model to serve HTTP requests.

4. **Web Interface:**
    - Created a website using HTML/CSS and Javascript.
    - Users can input home square feet area, number of bedrooms, etc.
    - The website calls the Python Flask server to retrieve the predicted price.

5. **Data Science Concepts Covered:**
    - Data loading and cleaning.
    - Outlier detection and removal.
    - Feature engineering.
    - Dimensionality reduction.
    - GridsearchCV for hyperparameter tuning.
    - K-fold cross-validation.

## Technologies and Tools Used

- **Python:** The main programming language used.
- **Numpy and Pandas:** Used for data cleaning.
- **Matplotlib:** Used for data visualization.
- **Scikit-Learn:** Used for model building.
- **Jupyter Notebook, Visual Studio Code, and PyCharm:** Used as IDEs.
- **Gitbash, WinSCP, and Nginx:** Used as tools for reverse proxy setup.
- **Python Flask:** Used for the HTTP server.
- **HTML/CSS/Javascript:** Used for the user interface.

## Deployment

The application was deployed on an AWS EC2 Ubuntu instance using a reverse proxy setup.

## Note
Ensure that you have Python installed on your machine and that ports are available for running the Flask server. If you encounter any issues, refer to the documentation or reach out to the project maintainers.

Happy predicting home prices!
