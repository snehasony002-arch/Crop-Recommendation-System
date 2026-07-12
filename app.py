from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("models/crop_model.pkl")

# Crop Information
crop_info = {
    "rice": {
        "description": "Rice is a staple food crop grown in warm and humid climates.",
        "season": "Kharif",
        "soil": "Clay and Loamy Soil",
        "water": "High",
        "fertilizer": "Urea and DAP"
    },

    "maize": {
        "description": "Maize is an important cereal crop used for food and animal feed.",
        "season": "Kharif",
        "soil": "Well-drained Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Nitrogen-rich Fertilizer"
    },

    "chickpea": {
        "description": "Chickpea is a protein-rich pulse crop.",
        "season": "Rabi",
        "soil": "Sandy Loam",
        "water": "Low",
        "fertilizer": "DAP"
    },

    "kidneybeans": {
        "description": "Kidney beans are nutritious legumes rich in protein.",
        "season": "Rabi",
        "soil": "Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Organic Compost"
    },

    "pigeonpeas": {
        "description": "Pigeon pea is a drought-resistant pulse crop.",
        "season": "Kharif",
        "soil": "Loamy Soil",
        "water": "Moderate",
        "fertilizer": "NPK Fertilizer"
    },

    "mothbeans": {
        "description": "Moth bean grows well in dry regions.",
        "season": "Kharif",
        "soil": "Sandy Soil",
        "water": "Low",
        "fertilizer": "Organic Manure"
    },

    "mungbean": {
        "description": "Mung bean is a fast-growing pulse crop.",
        "season": "Summer",
        "soil": "Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Compost"
    },

    "blackgram": {
        "description": "Black gram is a popular pulse crop in India.",
        "season": "Kharif",
        "soil": "Clay Loam",
        "water": "Moderate",
        "fertilizer": "DAP"
    },

    "lentil": {
        "description": "Lentil is a cool-season pulse crop.",
        "season": "Rabi",
        "soil": "Loamy Soil",
        "water": "Low",
        "fertilizer": "Phosphorus Fertilizer"
    },

    "pomegranate": {
        "description": "Pomegranate is a fruit crop suited to dry climates.",
        "season": "Spring",
        "soil": "Well-drained Soil",
        "water": "Moderate",
        "fertilizer": "Organic Compost"
    },

    "banana": {
        "description": "Banana requires warm weather and abundant water.",
        "season": "All Seasons",
        "soil": "Loamy Soil",
        "water": "High",
        "fertilizer": "Potassium-rich Fertilizer"
    },

    "mango": {
        "description": "Mango is known as the king of fruits.",
        "season": "Summer",
        "soil": "Well-drained Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Organic Manure"
    },

    "grapes": {
        "description": "Grapes are grown in warm and dry climates.",
        "season": "Spring",
        "soil": "Sandy Loam",
        "water": "Moderate",
        "fertilizer": "NPK Fertilizer"
    },

    "watermelon": {
        "description": "Watermelon is a summer fruit crop.",
        "season": "Summer",
        "soil": "Sandy Soil",
        "water": "Moderate",
        "fertilizer": "Organic Compost"
    },

    "muskmelon": {
        "description": "Muskmelon grows best in warm climates.",
        "season": "Summer",
        "soil": "Sandy Loam",
        "water": "Moderate",
        "fertilizer": "Compost"
    },

    "apple": {
        "description": "Apple is a temperate fruit crop.",
        "season": "Winter",
        "soil": "Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Organic Fertilizer"
    },

    "orange": {
        "description": "Orange grows well in subtropical climates.",
        "season": "Winter",
        "soil": "Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Nitrogen Fertilizer"
    },

    "papaya": {
        "description": "Papaya is a fast-growing tropical fruit crop.",
        "season": "All Seasons",
        "soil": "Well-drained Soil",
        "water": "Moderate",
        "fertilizer": "Organic Compost"
    },

    "coconut": {
        "description": "Coconut thrives in coastal tropical regions.",
        "season": "All Seasons",
        "soil": "Sandy Soil",
        "water": "High",
        "fertilizer": "Potassium Fertilizer"
    },

    "cotton": {
        "description": "Cotton is a major fiber crop.",
        "season": "Kharif",
        "soil": "Black Soil",
        "water": "Moderate",
        "fertilizer": "Nitrogen Fertilizer"
    },

    "jute": {
        "description": "Jute is a fiber crop requiring high rainfall.",
        "season": "Kharif",
        "soil": "Alluvial Soil",
        "water": "High",
        "fertilizer": "Organic Compost"
    },

    "coffee": {
        "description": "Coffee grows best in cool, humid regions.",
        "season": "Spring",
        "soil": "Rich Loamy Soil",
        "water": "Moderate",
        "fertilizer": "Organic Manure"
    }
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    values = [[
        float(request.form["N"]),
        float(request.form["P"]),
        float(request.form["K"]),
        float(request.form["temperature"]),
        float(request.form["humidity"]),
        float(request.form["ph"]),
        float(request.form["rainfall"])
    ]]

    prediction = model.predict(values)[0].lower()

    info = crop_info.get(prediction)

    return render_template(
        "result.html",
        crop=prediction.title(),
        info=info
    )


if __name__ == "__main__":
    app.run(debug=True)