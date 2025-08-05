from fastapi  import FastAPI, File, UploadFile


app = FastAPI()

@app.post("/search")
def search():

    return "Search API is working"



@app.get("/")
def read_root():
    return "Hello World!"

