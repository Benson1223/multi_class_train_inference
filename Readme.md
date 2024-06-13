Keyboard layout automation check(YOLO model training and Inference)

Author: PQA intern Benson Lin

Project Describe: Training YOLO V8 model to do layout detection.

Project Flow: “Data Label” --> ”Model Training” --> ”Inference”

< Data Label >
Step1: Use label tool to label training data (tool: https://roboflow.com/), when you load the file to this webpage, you can begin to label.

Step2: When finish label you can export the image file and label file, than put them to the folder: “datasets/momo640/train/images” and “datasets/momo640/train/label”.( Here, training data is used as an example. Testing and validating are the same.)

< Model Training >
Step1: put the “keydata.yaml” to the folder. This define training category:

Step2: put pretrain weight: “yolov8n.pt” to the folder

Step3: pip install -r requirements.txt

Step4:python train.py, when finish train, you can get the best weight at route “\runs\detect”

< Inference>
Step1: drag the “best.pt” best weight from route “\runs\detect\weights” to the same route as inference.py

Step2: python inference.py, than you can get inference result at “detected_images”




