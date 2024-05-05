from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from prometheus_client import Counter, Gauge, start_http_server
import numpy as np
from PIL import Image
import keras
import psutil
import time

app = FastAPI()

# Load pre-trained Keras model
model_path = "mnist_model.keras"
app.state.model = keras.models.load_model(model_path)
start_http_server(8001)

# Prometheus metrics
api_usage = Counter("api_usage", "API Usage", ["client_ip"])
api_running_time = Gauge("api_running_time", "API Running Time", ["client_ip"])
api_cpu_utilization = Gauge("api_cpu_utilization", "API CPU Utilization", ["client_ip"])
api_memory_utilization = Gauge("api_memory_utilization", "API Memory Utilization", ["client_ip"])

def predict_digit(model, data_point):
    data_point = np.array(data_point).reshape((1, 784))
    prediction = model.predict(data_point)
    digit = np.argmax(prediction)
    return str(digit)

def format_image(image):
    image = image.resize((28, 28))
    image = image.convert('L')
    data_point = [pixel / 255.0 for pixel in list(image.getdata())]
    return data_point

@app.post("/predict")
async def predict(request: Request, file: UploadFile = File(...)):
    client_ip = request.client.host

    try:
        start_time = time.time()
        image = Image.open(file.file)
        data_point = format_image(image)
        model = app.state.model
        digit = predict_digit(model, data_point)

        # Update Prometheus metrics
        api_usage.labels(client_ip).inc()
        api_running_time.labels(client_ip).set(time.time() - start_time)
        api_cpu_utilization.labels(client_ip).set(psutil.cpu_percent())
        api_memory_utilization.labels(client_ip).set(psutil.virtual_memory().percent)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500, media_type="application/json")

    return JSONResponse(content={"digit": digit}, media_type="application/json")