from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# In-memory data store
devices = {"Kitchen Light": {"state": "off"}}
sensors = {"Living Room Temperature": {"value": "25.5", "unit": "°C"}}

# Device Control Endpoint
class DeviceControl(Resource):
    def post(self, device_id):
        data = request.json
        if device_id in devices:
            devices[device_id]["state"] = data["state"]
            return jsonify({"message": f"{device_id} turned {data['state']}."})
        return {"error": "Device not found"}, 404

# Sensor Data Endpoint
class SensorData(Resource):
    def get(self, sensor_id):
        if sensor_id in sensors:
           return jsonify(sensors[sensor_id],f"The temperature in the Kitchen is {sensors[sensor_id]["value"]} {sensors[sensor_id]["unit"]}")
        return {"error": "Sensor not found"}, 404

# Add endpoints to the API
api.add_resource(DeviceControl, "/devices/<string:device_id>/control")
api.add_resource(SensorData, "/sensors/<string:sensor_id>/data")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
