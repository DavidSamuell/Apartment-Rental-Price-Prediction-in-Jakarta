import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(bedroom, apt_size, max_watt, furnish_type, kecamatan):

    try:
        loc_index = __data_columns.index(kecamatan.lower())
    except:
        loc_index = -1
    try:
        furnish_index = __data_columns.index(furnish_type.lower())
    except:
        print("Invalid type!")

    x = np.zeros(len(__data_columns))
    x[0] = bedroom
    x[1] = np.log(apt_size)
    x[2] = max_watt    
    x[loc_index] = 1    
    x[furnish_index] = 1

    #  Make Prediction
    y_pred = __model.predict(np.array([x]))
    # Reverse log transform predicted price value 
    return int(np.exp(y_pred))


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    
    with open("./Website/server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:] 

    with open('./Website/server/artifacts/travelio_apart.pickle', 'rb') as f:
        __model = pickle.load(f)
    # print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns    

if __name__ == '__main__':
    load_saved_artifacts()
    
    print(get_estimated_price(2, 54, 1500, 'Full Furnished', 'Tebet'))
    print(get_estimated_price(2, 35, 1500, 'Unfurnished', 'Setiabudi'))
