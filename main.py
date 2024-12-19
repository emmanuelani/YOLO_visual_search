from fastapi import FastAPI, File, UploadFile
from PIL import Image
import uvicorn
from ultralytics import YOLO
import io
import numpy as np

# Initializing the FastAPI app
app = FastAPI(
    title="Visual Search API-2",
    description="This is the API that will be used for the visual search feature",
)

# Load the YOLO model
model = YOLO("vision_model.pt")

# Categories
classes = model.names


@app.on_event("startup")
def startup():
    print("Application starting!")


# Make the prediction using the fine-tuned YOLO model
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Check the file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        return {"error": "Invalid file type. Please upload a JPEG or PNG image."}

    try:
        # Read and process the image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        image = image.convert("RGB")  # Ensure compatibility with YOLO

        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Run the YOLO model on the image
        results = model.predict(image_array)

        # Extract predictions
        predictions = []
        for box in results[0].boxes:
            class_id = int(box.cls)  # Class index
            category = classes.get(class_id, "Unknown")
            predictions.append(
                {
                    "class_id": class_id,
                    "category": category,
                    "confidence": float(box.conf),
                    "bbox": box.xyxy.tolist(),  # Bounding box coordinates
                }
            )

        return {"predictions": predictions}
    except Exception as e:
        return {
            "error": "Failed to process the image or make predictions.",
            "details": str(e),
        }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
