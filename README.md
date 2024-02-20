# Delivery Fee Calculator Back-end Solution

## Implemented by Isabelle Bryans

### Steps:

1. Run `main.py`

2. Test the API:

   - Run `testing.py` to see the API tested on a variety of values.

   **OR**

   - Send an HTTP POST request to the API with the following JSON format:

      ```json
      {
          "cart_value": 790,
          "delivery_distance": 2235,
          "number_of_items": 4,
          "time": "2024-01-15T13:00:00Z"
      }
      ```

      Using cURL:

      ```bash
      curl -H "Content-Type: application/json" -X POST -d "{\"cart_value\": 790, \"delivery_distance\": 2235, \"number_of_items\": 4, \"time\": \"2024-01-15T13:00:00Z\"}" http://127.0.0.1:5000/get-deliveryfee
      ```

