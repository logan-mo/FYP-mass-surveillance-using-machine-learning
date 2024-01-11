from fastapi import FastAPI, File, UploadFile, Form


app = FastAPI()


@app.get("/")
def health_check():
    return {"message": "working"}


# Currently working with frames. In the future will also work on video streams rstp links
@app.post("/process")
def process(input_frame: UploadFile = File(...), camera_id: str = Form(...)):
    ## Takes the image, sends it to the pipeline, and returns the result
    ## Also saves the result in the database
    ...
