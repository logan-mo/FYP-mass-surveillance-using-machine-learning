import os
import glob
from subprocess import call
import shutil

BASE_DIR = "training_data"
OUTPUT_DIR = "number_plate"
with open(os.path.join(BASE_DIR, "classes.txt")) as f:
    classes = f.readlines()
    classes = [x.strip() for x in classes]

# desired_classes = list(set(classes) - set(["number_plate"]))
desired_classes = ["number_plate"]
desired_classes_indices = [classes.index(cls.lower()) for cls in desired_classes]

annotations = glob.glob(os.path.join(BASE_DIR, "labels", "*"))
annotations


if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

if not os.path.exists(os.path.join(OUTPUT_DIR, "labels")):
    os.mkdir(os.path.join(OUTPUT_DIR, "labels"))

if not os.path.exists(os.path.join(OUTPUT_DIR, "images")):
    os.mkdir(os.path.join(OUTPUT_DIR, "images"))

current_dir = os.getcwd()

for annotation_file in annotations:
    desired_data = []
    with open(annotation_file) as f:
        data = [x.strip() for x in f.readlines()]
        data_split = [x.split() for x in data]
        for split in data_split:
            if (
                int(split[0]) in desired_classes_indices
            ):  # If the current row is a desired class
                desired_data.append(split)

        for idx, desired in enumerate(desired_data):
            # Replace the class index with the new index
            desired[0] = str(desired_classes.index(classes[int(desired[0])].lower()))
            desired_data[idx] = " ".join(desired)

    if len(desired_data) > 0:
        with open(
            os.path.join(OUTPUT_DIR, "labels", os.path.basename(annotation_file)), "w"
        ) as f:
            f.write("\n".join(desired_data))
            print(
                "Wrote {} lines to {}".format(
                    len(desired_data),
                    os.path.join(OUTPUT_DIR, os.path.basename(annotation_file)),
                )
            )

        image_file = os.path.join(
            BASE_DIR, "images", os.path.basename(annotation_file).replace("txt", "png")
        )
        output_image_path = os.path.join(OUTPUT_DIR, "images") + os.sep
        print(f"Copying {image_file} to {output_image_path}")

        if not os.path.exists(image_file):
            raise ValueError()

        shutil.copy(image_file, output_image_path)

with open(os.path.join(OUTPUT_DIR, "classes.txt"), "w") as f:
    f.write("\n".join(desired_classes))
