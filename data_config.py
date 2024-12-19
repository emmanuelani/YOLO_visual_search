import os
import yaml

# defining paths
base_dir = "C:\\Users\\Manuel\\Desktop\\Visual search gig\\labelled_dataset"

# creating the directory structure
try:
    os.makedirs(os.path.join(base_dir, "images\\train"))
    os.makedirs(os.path.join(base_dir, "labels\\train"))
    os.makedirs(os.path.join(base_dir, "images\\val"))
    os.makedirs(os.path.join(base_dir, "labels\\val"))
except FileExistsError:
    print("Image directory already exists")

# defining dataset configuration

categories = ["air-conditioner", "back-pack", "blender", "female-dress", "female-shoe", "hand-bag", "hoodie", \
        "iron", "laptop", "male-shirt", "male-shoe", "male-short", "microwave", "phone", \
            "refridgerator", "sneaker", "washing-machine", "wrist-watch"]
config = {
    "train": os.path.join(base_dir, "images\\train"),
    "val": os.path.join(base_dir, "images\\val"),
    "nc": len(categories),
    "names": categories
        }


# save configuration as yml file
with open("my_data.yml", "w") as f:
    yaml.dump(config, f)