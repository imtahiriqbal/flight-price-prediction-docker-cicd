from flask import Flask, request, url_for, render_template

import pickle
import numpy as np
import bz2file as bz2

app = Flask(__name__)

# Used method for saving model file
def compress_model(file_path, data):
    with bz2.BZ2File(file_path + '.pbz2', 'w') as f:
        pickle.dump(data, f)

# Used method for loading model file
def decompress_model(file_path):
    with bz2.BZ2File(file_path, 'rb') as f:
        model = pickle.load(f)
        
    return model

# Load model
model = decompress_model("rfrmodel.pkl.pbz2")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        form = request.form
        stops = int(form.get("stops"))
        clas = int(form.get("class"))
        duration = float(form.get("duration"))
        days_left = int(form.get("days_left"))
        airline = form.get("airline")
        source = form.get("source")
        destination = form.get("destination")
        departure = form.get("departure")
        arrival = form.get("arrival")
    
        data = [stops, clas, duration, days_left]
        preprocessed_data = preprocessing(airline, source, destination, departure, arrival)
        data.extend(preprocessed_data)
        print(data)
        final_input = np.array(data).reshape(1, -1)
        output = model.predict(final_input)[0]
        return render_template('index.html', prediction_text='Predicted Price for the Flight: {}'.format(output))
    
    else:
        return render_template('index.html')
    

def preprocessing(airline: str, source: str, destination: str, departure: str, arrival: str):
    data = []
    
    airlines_dict = {"AirAsia": 0, "Air_India": 0, "GO_FIRST": 0, "Indigo": 0, "SpiceJet": 0, "Vistara": 0}
    airlines = categorical_encoding(airline, airlines_dict)
    data.extend(airlines)
    
    source_city_dict = {"Bangalore": 0, "Chennai": 0, "Delhi": 0, "Hyderabad": 0, "Kolkata": 0, "Mumbai": 0}
    source_city = categorical_encoding(source, source_city_dict)
    data.extend(source_city)
    
    destination_city_dict = {"Bangalore": 0, "Chennai": 0, "Delhi": 0, "Hyderabad": 0, "Kolkata": 0, "Mumbai": 0}
    destination_city = categorical_encoding(destination, destination_city_dict)
    data.extend(destination_city)

    departure_time_dict = {"Afternoon": 0, "Early_Morning": 0, "Evening": 0, "Late_Night": 0, "Morning": 0, "Night": 0}
    departure_time = categorical_encoding(departure, departure_time_dict)
    data.extend(departure_time)
    
    arrival_time_dict = {"Afternoon": 0, "Early_Morning": 0, "Evening": 0, "Late_Night": 0, "Morning": 0, "Night": 0}
    arrival_time = categorical_encoding(arrival, arrival_time_dict)
    data.extend(arrival_time)
    
    return data


def categorical_encoding(val, data):
    if val in data.keys():
        data[val] = 1
    return list(data.values())
    
    
if __name__ == "__main__":
    app.run(debug=True)
