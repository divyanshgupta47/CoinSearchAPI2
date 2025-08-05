from fastapi  import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse


app = FastAPI()

@app.post("/search")
def search(image: UploadFile = File(...)):
    if not image:
        return JSONResponse(content={"error": "No image uploaded"}, status_code=400)

    return "Search API is working"



@app.get("/")
def read_root():
    return "Hello World!"



