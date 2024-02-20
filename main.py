from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

# incoming JSON object: {"cart_value": x, "delivery_distance": y, "number_of_items": z, "time": "t"}

# function to calculate small surcharge if order below €10
def surcharge(cart_value):
    residue = 1000-cart_value
    print("surcharge = "+ str(residue))
    if residue > 0:
        return residue
    return 0


# function to calculate extra fees based on distance
def distance_fee(dist):

    fee = 200
    dist -= 1000

    while dist > 0:
        fee += 100
        dist -= 500
    #print("distance fee = "+str(fee))
    return fee

# function to calculate extra fees for number of items > 4
def num_items_fee(num_items):
    fee = 0

    if num_items > 12:
        fee = 120

    while num_items > 4:
        num_items -= 1
        fee += 50

    return fee

# Function to calculate extra fees if during Friday rush hour
def rush_hour_fee(time, fee):
  
    time_object = datetime.datetime.fromisoformat(time[:-1]) 
    hour = time_object.hour
    day_of_week= time_object.weekday()  
    #print(hour)

    if 14 < hour < 19 and day_of_week == 4:
        #print(fee*0.2)
        return fee*0.2
    return 0

# function to calculate total delivery fee
def deliveryfee(input):
    # if cart value > €200 then delivery fee = 0
    if input["cart_value"] >= 20000:
        return 0
    
    total = surcharge(input["cart_value"]) + distance_fee(input["delivery_distance"]) + num_items_fee(input["number_of_items"])
    total=total + rush_hour_fee(input["time"], total)
    
    if total > 1500:
        return 1500
    
    return total

@app.route("/get-deliveryfee", methods=["POST"]) # decorator. name of flask application
def get_deliveryfee():
    json_data = request.get_json()

    fee = deliveryfee(json_data)
    
    result = {"delivery_fee": fee}
    
    # Return the dictionary as a JSON response
    return result, 201

if __name__ == "__main__":
    app.run(debug=True)