from fastapi  import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tempfile

app = FastAPI()

@app.post("/search")
async def search(image: UploadFile = File(...)):
    if not image:
        return JSONResponse(content={"error": "No image uploaded"}, status_code=400)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image_path = tmp.name
        tmp.write(await image.read())

    return "Search API is working"



@app.get("/")
def read_root():
    return "Hello World!"




