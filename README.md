# **FastAPI Based AI search app 🔎💻**

This repo contains a fine-tuned YOLOv8 model on e-commerce images spanning across difference categories.
It currently can classify e-commerce images into 18 categories with the possibility of incrreasing the number of categories in future iterations.

### _To use this API, copy and run this code in your terminal_
```python
git clone https://github.com/emmanuelani/YOLO_visual_search

docker build -t my-app .
```

The above code will build a docker image which you can now run on your system.

The app takes in an image, processes it and pass it to the model which then predcits the image category.
