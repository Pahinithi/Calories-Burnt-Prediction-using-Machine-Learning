# Calories Burned Prediction Using Machine Learning

This project demonstrates a web application for predicting calories burned based on user inputs. It leverages a machine learning model to provide calorie estimates based on various physical and exercise parameters.

## Project Overview

- **Model**: Machine Learning model for calorie prediction
- **Language**: Python
- **Framework**: Flask (for web deployment)
- **Tools/Libraries**: 
  - NumPy
  - Pickle
  - Flask

## Project Structure

- **app.py**: Contains the Flask web application code to handle user input, make predictions using the model, and render the results on a webpage.
- **index.html**: The front-end template where users can input their data to get a prediction of calories burned.
- **calorie_predictor_model.pkl**: The saved machine learning model used for calorie prediction.
- **requirements.txt**: Lists the required Python libraries for the project.
- **README.md**: Documentation and overview of the project (this file).

## Web Application

The application provides a user-friendly interface where users can enter details such as age, height, weight, exercise duration, heart rate, and body temperature. The application then uses the trained machine learning model to predict the calories burned.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Pahinithi/Calories-Burnt-Prediction-using-Machine-Learning/tree/main
   cd calorie-prediction
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Download or move the model file `calorie_predictor_model.pkl` into the project directory.

5. Run the Flask application:
   ```bash
   python app.py
   ```

6. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Enter the following details in the form:
   - **Gender**: Select the gender (Male or Female)
   - **Age**: Enter age in years
   - **Height**: Enter height in cm
   - **Weight**: Enter weight in kg
   - **Duration**: Enter duration of exercise in minutes
   - **Heart Rate**: Enter heart rate in bpm
   - **Body Temperature**: Enter body temperature in °C

2. Click "Predict" to see the estimated calories burned.

## Model Details

- **Model Type**: The project uses a machine learning model trained to predict calories burned based on various input features.
- **Training**: The model was trained on relevant datasets and saved using Pickle.

## License

This project is licensed under the MIT License.

<img width="1728" alt="Screenshot 2024-08-15 at 23 37 13" src="https://github.com/user-attachments/assets/b76a9755-788d-49f6-8431-155449ba7ad9">


