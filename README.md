# FYP-mass-surveillance-using-machine-learning

Data

https://www.kaggle.com/code/sarthakmodi/object-detection-using-yolov8/input

Train Validation Test Split Code : https://github.com/akashAD98/Train_val_Test_split/blob/main/yolov5_v7_v9_split.py

While training on vast.ai Ubuntu VM, Encountered the error:

ImportError: libGL.so.1: cannot open shared object file: No such file or directory

and solved it using:

apt-get update && apt-get install ffmpeg libsm6 libxext6  -y