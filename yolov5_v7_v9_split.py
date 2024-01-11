# %% Kütüphanelerin Yüklenmesi

from IPython.display import Image
import os
import random
import shutil
from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import glob
import time

# #%% Veri Setini %80-%10-%10 Train-Test-Val Olarak Bölme


base_dir = "number_plate"


image_path = os.path.join(base_dir, "images")
label_path = os.path.join(base_dir, "labels")

images = [os.path.join(image_path, x) for x in os.listdir(image_path)]
labels = [
    os.path.join(label_path, x) for x in os.listdir(label_path) if x[-3:] == "txt"
]
images.sort()
labels.sort()
train_images, val_images, train_labels, val_labels = train_test_split(
    images, labels, test_size=0.2, random_state=1
)
val_images, test_images, val_labels, test_labels = train_test_split(
    val_images, val_labels, test_size=0.5, random_state=1
)


root_path = "images/"
folders = ["train", "test/", "val"]
for folder in folders:
    os.makedirs(os.path.join(root_path, folder))

root_path = "labels/"
folders = ["train", "test/", "val"]
for folder in folders:
    os.makedirs(os.path.join(root_path, folder))

# %% Resim ve Labelleri Dosyalara Taşıma


def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False


move_files_to_folder(train_images, "images/train")
move_files_to_folder(val_images, "images/val/")
move_files_to_folder(test_images, "images/test/")
move_files_to_folder(train_labels, "labels/train/")
move_files_to_folder(val_labels, "labels/val/")
move_files_to_folder(test_labels, "labels/test/")
