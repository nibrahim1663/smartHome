# Project:      Final Project – Smart Home API
# File:         smart_home_api.py
# Author:       Nawriz Ibrahim
# Date :        2024-December-06
# Description:  This is a Flask-based API for managing and monitoring a smart home system. 
#               It allows users to control devices (e.g., turning lights on/off) and monitor 
#               sensor data (e.g., room temperature).
#
#               Endpoints:
#                   - POST /devices/<device_id>/control: Control devices by turning them on/off.
#                   - GET /sensors/<sensor_id>/data: Fetch data from sensors.
#                   - GET /: Serve the HTML file as a user interface.

from flask import Flask, request, jsonify, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# data store for devices and sensors
devices = {"Kitchen Light": {"state": "off"}}
sensors = {"Living Room Temperature": {"value": "25.5", "unit": "°C"}}

# Device Control Endpoint
class DeviceControl(Resource):
    # Function Name:    post(self, device_id)
    # Purpose:          Controls the state of a device (e.g., turn a light on or off).
    # Parameters:       The ID of the device
    # Returns:          Success: JSON with a success message OTHERWISE Error: JSON with an error message if the device is not found.
    def post(self, device_id):
        data = request.json
        if device_id in devices:
            devices[device_id]["state"] = data["state"]
            return jsonify({"message": f"{device_id} turned {data['state']}."})
        return {"error": "Device not found"}, 404

# Sensor Data Endpoint
class SensorData(Resource):
    # Function Name:    get(self, sensor_id)
    # Purpose:          Fetches data from a sensor, such as temperature.
    # Parameters:       The ID of the sensor
    # Returns:          Success: JSON with the sensor value, unit, and a descriptive message OTHERWISE Error: JSON with an error message 
    #                   if the sensor is not found.
    def get(self, sensor_id):
        if sensor_id in sensors:
            sensor_data = sensors[sensor_id]
            message = f"{sensor_id} is {sensor_data['value']}{sensor_data['unit']}"
            return jsonify({"value": sensor_data["value"], "unit": sensor_data["unit"], "message": message})
        return {"error": "Sensor not found"}, 404


# Add endpoints to the API
# Adding device control route
api.add_resource(DeviceControl, "/devices/<string:device_id>/control")
# # Adding sensor data route
api.add_resource(SensorData, "/sensors/<string:sensor_id>/data")

# Serve the HTML file
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
