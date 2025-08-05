from fastapi  import FastAPI, File, UploadFile


app = FastAPI()

@app.post("/search")
def search(image: UploadFile = File(...)):

    return "Search API is working"



@app.get("/")
def read_root():
    return "Hello World!"


