# 🌱 Crop Recommendation System

A Machine Learning web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The application is built using Python, Scikit-learn, and Flask, providing a simple web interface for real-time crop prediction.

---

## Overview

Selecting the right crop is essential for improving agricultural productivity. This project uses a trained **Random Forest Classifier** to predict the most appropriate crop from soil and climate parameters.

Users enter agricultural parameters through a Flask web application, and the model returns the recommended crop along with useful cultivation information.

---

## Features

- Machine Learning-based crop prediction
- Web interface built with Flask
- Real-time prediction
- Crop cultivation information including:
  - Description
  - Suitable season
  - Soil type
  - Water requirement
  - Fertilizer recommendation
- Clean project structure following Flask conventions

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib |
| Backend | Flask |
| Frontend | HTML, CSS |
| Version Control | Git |
| Repository Hosting | GitHub |

---

## Machine Learning Pipeline

```
Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Model Training
(Random Forest Classifier)
      │
      ▼
Model Serialization (.pkl)
      │
      ▼
Flask Web Application
      │
      ▼
User Input
      │
      ▼
Crop Prediction
```

---

## Project Structure

```
Crop-Recommendation-System/
│
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
│
├── data/
│   └── Crop_recommendation.csv
│
├── models/
│   └── crop_model.pkl
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── venv/
```

---

## Dataset

The model is trained using an agricultural dataset containing the following input features:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

**Target Variable**

- Crop Label

---

## Model

**Algorithm:** Random Forest Classifier

Random Forest was selected because it:

- Handles nonlinear relationships effectively
- Provides strong predictive performance
- Is robust against overfitting
- Performs well on tabular datasets

---




### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Application Workflow

1. Enter soil and environmental parameters.
2. Submit the form.
3. The trained model predicts the most suitable crop.
4. View the recommended crop and its cultivation details.

---

## Future Enhancements

- Crop image integration
- Prediction confidence score
- Weather API integration
- Fertilizer recommendation engine
- Responsive UI improvements
- Cloud deployment

---

## Author

**Sneha Sony**

GitHub: https://github.com/snehasony002-arch

LinkedIn: *(Add your LinkedIn profile URL here)*

---

## License

This project is licensed for educational and portfolio purposes.
