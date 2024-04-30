from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from io import StringIO
import requests

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/", response_class=HTMLResponse)
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    data = StringIO(contents.decode("utf-8"))
    df = pd.read_csv(data)

    # Adjusted format: Directly send list of records
    inference_request = {
        "dataframe_records": df.to_dict(orient='records')
    }

    endpoint = "http://127.0.0.1:1234/invocations"

    response = requests.post(endpoint, json=inference_request)
    if response.status_code == 200:
        predictions = response.json()
        return templates.TemplateResponse("index.html", {"request": request, "predictions": predictions})
    else:
        raise HTTPException(status_code=response.status_code, detail=str(response.text))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
