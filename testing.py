import json
import requests

url = 'http://127.0.0.1:5000/get-deliveryfee'
test_values=[
    {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}, #
    {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 6, "time": "2024-01-15T13:00:00Z"}, # 6 items
    {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 1, "time": "2024-01-19T18:00:00Z"}, # during rush hour
    {"cart_value": 790, "delivery_distance": 4321, "number_of_items": 1, "time": "2024-01-15T13:00:00Z"}, # increased distance
    {"cart_value": 21000, "delivery_distance": 2235, "number_of_items": 1, "time": "2024-01-15T13:00:00Z"}, # cart value > €200
    {"cart_value": 790, "delivery_distance": 0, "number_of_items": 1, "time": "2024-01-15T13:00:00Z"}, # base delivery + surcharge for small order
    {"cart_value": 790, "delivery_distance": 10500, "number_of_items": 1, "time": "2024-01-15T13:00:00Z"}, # big distance - max delivery €15
    {"cart_value": 2580, "delivery_distance": 1501, "number_of_items": 8, "time": "2024-01-15T13:00:00Z"}, # small distance and many items
    {"cart_value": 2580, "delivery_distance": 2235, "number_of_items": 8, "time": "2024-01-19T18:00:00Z"} # rush hour
]

answers = [710, 810, 852, 1110, 0, 410, 1500, 600, 840]

for value in test_values:
    x = requests.post(url, json = value)
    print("\nTest "+str(test_values.index(value)+1))
    print("Order Details:")
    print(value)
    fee=json.loads(x.text)
    print("Calcluated deliver charge: " + str(fee["delivery_fee"]))
    print("Expected delivery charge: "+ str(answers[test_values.index(value)]))
