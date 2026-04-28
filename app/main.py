from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from prometheus_fastapi_instrumentator import Instrumentator # pyright: ignore[reportMissingImports]
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Online", "message": "API Stress Tester pronta para o caos"}

@app.get("/stress")
def stress_cpu(duration: int = 10):
    start_time = time.time()
    end_time = start_time + duration
    num1 = 1

    while time.time() < end_time :
        resultado = num1 * num1 + 1
        #print(resultado)

    return {"message": f"Stress finalizado após {duration} segundos"}

Instrumentator().instrument(app).expose(app)