# Import necessary modules
from flask import Flask, request, render_template
import pickle
import numpy as np

# Create a Flask application instance
app = Flask(__name__, template_folder='.')

# Load the trained model
with open("calorie_predictor_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a route for the homepage
@app.route("/")
def home():
    return render_template("index.html")  # Render the index.html template

# Define a route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get input data from the form
    gender = int(request.form["gender"])
    age = float(request.form["age"])
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    duration = float(request.form["duration"])
    heart_rate = float(request.form["heart_rate"])
    body_temp = float(request.form["body_temp"])

    # Combine inputs into a single list
    input_data = np.asarray([[gender, age, height, weight, duration, heart_rate, body_temp]])

    # Make a prediction using the model
    prediction = model.predict(input_data)

    # Output the prediction
    prediction_text = f'Predicted Calories Burned: {prediction[0]:.2f} kcal'

    # Pass the prediction value to the template
    return render_template("index.html", prediction=prediction_text)

# Start the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode for development
