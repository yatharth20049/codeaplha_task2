
# 🧠 Credit Scoring Prediction Model

A machine learning web app that predicts an individual's **creditworthiness** using past financial data. Built using **Python, Flask**, and the **UCI German Credit dataset**.

---

## 🚀 Project Overview

This project classifies individuals as either:
- ✅ **Creditworthy** (good credit)
- ❌ **Not Creditworthy** (bad credit)

Using classification algorithms like **Random Forest**, the app learns patterns from financial features such as account balance, duration, income, and housing type.

---

## 📊 Features

- 📁 UCI German Credit dataset (Statlog)
- 🧠 Trained model using `RandomForestClassifier` with class balancing
- 📈 Evaluation using Accuracy, Precision, Recall, F1-score, ROC-AUC
- 🌐 Web app built using Flask
- 🖼️ Clean and stylish HTML + CSS interface
- 💾 Model saved as `.pkl` using `joblib`

---

## 📂 Folder Structure

```
├── app.py                  # Flask app
├── templates/
│   └── index.html          # Frontend UI
├── models/
│   └── credit_model.pkl    # Trained model
├── static/                 # (Optional) CSS, JS files
└── README.md               # Project documentation
```

---

## 🛠️ Setup Instructions

1. **Clone this repo**
```bash
git clone https://github.com/your-username/credit-scoring-model.git
cd credit-scoring-model
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app**
```bash
python app.py
```

5. **Open your browser**
```
http://127.0.0.1:5000
```

---

## ⚙️ Tech Stack

- Python
- Scikit-learn
- Flask
- HTML & CSS (with Google Fonts)
- Joblib

---

## 🧠 Model Details

- Algorithm: `RandomForestClassifier(class_weight='balanced')`
- Trained on: 1000 samples from UCI German Credit dataset
- Balanced for class imbalance (700 good, 300 bad)
- Key Features:
  - Checking account status
  - Credit amount
  - Loan duration
  - Employment length
  - Age
  - Housing type
  - Foreign worker status

---

## 📚 Dataset Citation

> Hofmann, H. (1994). Statlog (German Credit Data) [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5NC77](https://doi.org/10.24432/C5NC77)

---

## 📌 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- UCI Machine Learning Repository
- Scikit-learn documentation
- Flask framework
