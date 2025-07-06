from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('models\credit_model.pkl')

@app.route('/')
def home():
    print("Homepage loaded")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("🔁 Form submitted!")  # log in terminal
    try:
        # Only use selected 7 features
        input_data = [
            float(request.form['checking']),
            float(request.form['duration']),
            float(request.form['credit_amount']),
            float(request.form['employment']),
            float(request.form['age']),
            float(request.form['housing']),
            float(request.form['foreign_worker'])
        ]

        import numpy as np
        input_array = np.zeros((1, 24))  # full feature array with 24 values
        selected_indexes = [0, 1, 4, 6, 12, 14, 19]  # positions of selected features
        for i, val in zip(selected_indexes, input_data):
            input_array[0, i] = val

        prediction = model.predict(input_array)[0]
        result = "Creditworthy ✅" if prediction == 1 else "Not Creditworthy ❌"
    except Exception as e:
        result = f"Error: {e}"

    return render_template('index.html', prediction_text=result)


if __name__ == '__main__':
    app.run(debug=True)
