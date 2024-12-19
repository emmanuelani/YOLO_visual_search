from fastapi import FastAPI, File, UploadFile
from PIL import Image
import uvicorn
from ultralytics import YOLO
# import requests

import io

# initializing the fastAPI app
app = FastAPI(
    title="Visual Search API-4",
    description="This is the API that will be used for the visual search feature",
)

# loading model
model = YOLO("vision_model.pt")

# categories
classes = model.names


# @app.get("/")
# def hello():
#     return {"Message": "Hello World!"}


# @app.on_event("startup")
# def startup():
#     print("Application starting!")


# getting the output from the model's prediction
@app.post("/read_file/")
async def read_file(file: UploadFile = File(...)):
    # check the file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Invalid file type. Please upload a JPEG or PNG image."}
    print("Done!")
    # contents = await file.read()
    # return contents
    # try:
    #     contents = await file.read()
    #     image = Image.open(io.BytesIO(contents))
    #     image.verify()
    #     # image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    # except Exception as e:
    #     return {"error": "Failed to process the image.", "details": str(e)}

    # return image


# make the prediction using the fine-tuned YOLO model
# @app.post("/predict/")
# async def predict():
#     image = await read_file()
#     result = model.predict(image)
#     pred_id = result[0].boxes.cls

#     # extracting the product class name
#     for id, category in classes.items():
#         if pred_id == id:
#             return category

# output = predict(image)
# # print(output)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
