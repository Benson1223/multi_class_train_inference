from ultralytics import YOLO

def main():
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # Use the model
    model.train(data="key_data.yaml", epochs=100000)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    
    path = model.export(format="onnx")  # export the model to ONNX format

if __name__ == '__main__':
    main()
