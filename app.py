from flask import Flask, render_template, request
import numpy as np
import joblib


app = Flask(__name__)


# ==============================
# LOAD MODEL AND LABEL ENCODER
# ==============================

model = joblib.load("model.pkl")

label_encoder = joblib.load("label_encoder.pkl")



# ==============================
# 22 CROP DETAILS
# PART 1
# ==============================

crop_details = {


    "rice": {
        "name": "Rice",
        "season": "Kharif",
        "soil": "Clayey and Loamy Soil",
        "temperature": "20°C - 35°C",
        "rainfall": "150 - 300 cm",
        "water": "High Water Requirement",
        "fertilizer": "Nitrogen, Phosphorus and Potassium fertilizers",
        "benefits": "Main staple food crop with high production value",
        "description": "Rice is a major cereal crop grown in warm and humid climate."
    },


    "maize": {
        "name": "Maize",
        "season": "Kharif / Rabi",
        "soil": "Well drained Loamy Soil",
        "temperature": "18°C - 27°C",
        "rainfall": "50 - 100 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Nitrogen rich fertilizers",
        "benefits": "Used as food, animal feed and industrial raw material",
        "description": "Maize is a versatile crop suitable for different climatic conditions."
    },


    "chickpea": {
        "name": "Chickpea",
        "season": "Rabi",
        "soil": "Sandy Loam Soil",
        "temperature": "15°C - 25°C",
        "rainfall": "60 - 90 cm",
        "water": "Low Water Requirement",
        "fertilizer": "Phosphorus fertilizers and organic manure",
        "benefits": "Rich source of protein and improves soil fertility",
        "description": "Chickpea is an important pulse crop grown in winter season."
    },


    "kidneybeans": {
        "name": "Kidney Beans",
        "season": "Kharif",
        "soil": "Loamy Soil with good drainage",
        "temperature": "18°C - 30°C",
        "rainfall": "60 - 120 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Balanced NPK fertilizers",
        "benefits": "Protein rich food crop",
        "description": "Kidney beans require fertile soil and proper moisture."
    },


    "pigeonpeas": {
        "name": "Pigeon Peas",
        "season": "Kharif",
        "soil": "Sandy Loam Soil",
        "temperature": "26°C - 30°C",
        "rainfall": "60 - 100 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Phosphorus fertilizers and organic manure",
        "benefits": "Improves soil fertility by nitrogen fixation",
        "description": "Pigeon peas are drought tolerant pulse crops."
    },


    "mothbeans": {
        "name": "Moth Beans",
        "season": "Kharif",
        "soil": "Sandy Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "40 - 60 cm",
        "water": "Low Water Requirement",
        "fertilizer": "Organic manure",
        "benefits": "Suitable for dry regions",
        "description": "Moth bean is a drought resistant pulse crop."
    }
    ,

    "mungbean": {
        "name": "Mung Bean",
        "season": "Kharif / Rabi",
        "soil": "Loamy Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "50 - 75 cm",
        "water": "Low Water Requirement",
        "fertilizer": "Organic manure and Phosphorus fertilizers",
        "benefits": "High protein pulse crop and improves soil fertility",
        "description": "Mung bean is a short duration pulse crop suitable for warm climate."
    },


    "blackgram": {
        "name": "Black Gram",
        "season": "Kharif",
        "soil": "Clay Loam Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "60 - 80 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Phosphorus fertilizers and organic manure",
        "benefits": "Rich in protein and helps nitrogen fixation",
        "description": "Black gram is an important pulse crop grown in tropical regions."
    },


    "lentil": {
        "name": "Lentil",
        "season": "Rabi",
        "soil": "Sandy Loam Soil",
        "temperature": "15°C - 25°C",
        "rainfall": "35 - 50 cm",
        "water": "Low Water Requirement",
        "fertilizer": "Phosphorus fertilizers",
        "benefits": "Nutritious pulse crop rich in protein",
        "description": "Lentil grows well in cool climate with low rainfall."
    },


    "pomegranate": {
        "name": "Pomegranate",
        "season": "Annual",
        "soil": "Well Drained Loamy Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "50 - 100 cm",
        "water": "Low to Moderate Requirement",
        "fertilizer": "Organic manure and NPK fertilizers",
        "benefits": "High market value fruit crop",
        "description": "Pomegranate is a drought tolerant fruit crop."
    },


    "banana": {
        "name": "Banana",
        "season": "Annual",
        "soil": "Fertile Loamy Soil",
        "temperature": "20°C - 35°C",
        "rainfall": "100 - 200 cm",
        "water": "High Water Requirement",
        "fertilizer": "Nitrogen and Potassium fertilizers",
        "benefits": "Energy rich fruit crop",
        "description": "Banana is a tropical fruit crop requiring warm climate."
    },


    "mango": {
        "name": "Mango",
        "season": "Summer",
        "soil": "Deep Loamy Soil",
        "temperature": "24°C - 30°C",
        "rainfall": "75 - 250 cm",
        "water": "Moderate Requirement",
        "fertilizer": "Organic manure and NPK fertilizers",
        "benefits": "High value fruit crop known as king of fruits",
        "description": "Mango grows well in tropical and subtropical regions."
    },


    "grapes": {
        "name": "Grapes",
        "season": "Annual",
        "soil": "Sandy Loam Soil",
        "temperature": "15°C - 35°C",
        "rainfall": "50 - 75 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Nitrogen and Potassium fertilizers",
        "benefits": "Used for fresh fruits, juice and wine production",
        "description": "Grapes require dry climate during fruit development."
    },


    "watermelon": {
        "name": "Watermelon",
        "season": "Summer",
        "soil": "Sandy Loam Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "40 - 50 cm",
        "water": "High Water Requirement",
        "fertilizer": "Organic manure and NPK fertilizers",
        "benefits": "Refreshing fruit rich in water content",
        "description": "Watermelon grows best in warm climate."
    },


    "muskmelon": {
        "name": "Muskmelon",
        "season": "Summer",
        "soil": "Sandy Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "40 - 60 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Organic manure and balanced fertilizers",
        "benefits": "Nutritious fruit with good market demand",
        "description": "Muskmelon requires warm climate and sunlight."
    },


    "apple": {
        "name": "Apple",
        "season": "Winter",
        "soil": "Loamy Soil",
        "temperature": "10°C - 25°C",
        "rainfall": "75 - 125 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Organic manure and NPK fertilizers",
        "benefits": "High nutritional value fruit crop",
        "description": "Apple requires cool climatic conditions."
    },


    "orange": {
        "name": "Orange",
        "season": "Annual",
        "soil": "Well Drained Soil",
        "temperature": "20°C - 30°C",
        "rainfall": "100 - 150 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Nitrogen rich fertilizers",
        "benefits": "Rich source of Vitamin C",
        "description": "Orange is an important citrus fruit crop."
    },


    "papaya": {
        "name": "Papaya",
        "season": "Annual",
        "soil": "Fertile Loamy Soil",
        "temperature": "22°C - 35°C",
        "rainfall": "100 - 150 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Nitrogen and Potassium fertilizers",
        "benefits": "Fast growing fruit crop with medicinal value",
        "description": "Papaya grows quickly in tropical climates."
    }
    ,

    "coconut": {
        "name": "Coconut",
        "season": "Annual",
        "soil": "Sandy Loam Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "150 - 250 cm",
        "water": "High Water Requirement",
        "fertilizer": "Organic manure and Potassium fertilizers",
        "benefits": "Important plantation crop with multiple uses",
        "description": "Coconut grows well in tropical and coastal regions."
    },


    "cotton": {
        "name": "Cotton",
        "season": "Kharif",
        "soil": "Black Soil",
        "temperature": "21°C - 30°C",
        "rainfall": "50 - 100 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Nitrogen and Phosphorus fertilizers",
        "benefits": "Major fibre crop used in textile industry",
        "description": "Cotton is mainly cultivated for natural fibre production."
    },


    "jute": {
        "name": "Jute",
        "season": "Kharif",
        "soil": "Alluvial Soil",
        "temperature": "25°C - 35°C",
        "rainfall": "150 - 250 cm",
        "water": "High Water Requirement",
        "fertilizer": "Nitrogen fertilizers and organic manure",
        "benefits": "Eco-friendly natural fibre crop",
        "description": "Jute is called golden fibre because of its economic importance."
    },


    "coffee": {
        "name": "Coffee",
        "season": "Annual",
        "soil": "Rich Loamy Soil",
        "temperature": "15°C - 28°C",
        "rainfall": "150 - 250 cm",
        "water": "Moderate Water Requirement",
        "fertilizer": "Organic manure and NPK fertilizers",
        "benefits": "Important beverage crop with export value",
        "description": "Coffee grows well in cool humid climate under shade."
    }

}



# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def home():

    return render_template("index.html")



# ==============================
# PREDICTION ROUTE
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        N = float(request.form["N"])

        P = float(request.form["P"])

        K = float(request.form["K"])

        temperature = float(
            request.form["temperature"]
        )

        humidity = float(
            request.form["humidity"]
        )

        ph = float(
            request.form["ph"]
        )

        rainfall = float(
            request.form["rainfall"]
        )



        input_data = np.array(
            [[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]]
        )



        prediction = model.predict(
            input_data
        )



        crop_name = label_encoder.inverse_transform(
            prediction
        )[0]



        crop_key = crop_name.lower()



        details = crop_details.get(
            crop_key,
            {
                "name": crop_name,
                "season": "Not Available",
                "soil": "Not Available",
                "temperature": "Not Available",
                "rainfall": "Not Available",
                "water": "Not Available",
                "fertilizer": "Not Available",
                "benefits": "Not Available",
                "description": "Information not available"
            }
        )



        return render_template(
            "index.html",
            prediction=crop_name,
            details=details
        )



    except Exception as e:


        return render_template(
            "index.html",
            prediction="Error : " + str(e)
        )





# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":

    app.run(
        debug=True
    )