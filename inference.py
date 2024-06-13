#####HOW to use YOLO V8 inference(official)
from ultralytics import YOLO
import os
from pathlib import Path

model = YOLO('best.pt')

image_dir = './datasets/momo640/test/images'
image_paths = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]


results = model(image_paths)  


save_dir = 'detected_images'
os.makedirs(save_dir, exist_ok=True)


for i, (result, img_path) in enumerate(zip(results, image_paths)):
    image_name = Path(img_path).name  
    detections = []


    if result.boxes:
        boxes = result.boxes.data  
        for box in boxes:
            class_id = int(box[5]) 
            confidence = box[4]    
            class_name = model.names[class_id]  
            detections.append(f"{class_name} ({confidence:.2f})")

  
    print(f"Image: {image_name}, Detections: {', '.join(detections)}")

   
    save_path = os.path.join(save_dir, f'key_{i}.jpg')
    result.save(save_path)  