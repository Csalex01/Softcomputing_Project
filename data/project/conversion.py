import os
import json
from pathlib import Path
from PIL import Image

# CONFIG
data_root = 'data/visdrone'
image_dir = os.path.join(data_root, 'images')
label_dir = os.path.join(data_root, 'labels')
output_file = os.path.join(data_root, 'annotations', 'instances_train.json')

# VisDrone classes
class_names = [
    'ignored', 'pedestrian', 'person', 'bicycle', 'car', 'van',
    'truck', 'tricycle', 'awning-tricycle', 'bus', 'motor'
]

categories = [{"id": i, "name": name, "supercategory": "none"} for i, name in enumerate(class_names)]

coco = {
    "images": [],
    "annotations": [],
    "categories": categories
}

annotation_id = 0
image_id = 0

image_paths = sorted(Path(image_dir).glob('*.jpg'))

for img_path in image_paths:
    label_path = Path(label_dir) / f"{img_path.stem}.txt"
    if not label_path.exists():
        continue

    with Image.open(img_path) as img:
        width, height = img.size

    coco["images"].append({
        "id": image_id,
        "file_name": img_path.name,
        "width": width,
        "height": height
    })

    with open(label_path) as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) < 6:
                continue
            x, y, w, h, _, class_id = map(int, parts[:6])
            if class_id < 0 or class_id >= len(class_names):
                continue

            coco["annotations"].append({
                "id": annotation_id,
                "image_id": image_id,
                "category_id": class_id,
                "bbox": [x, y, w, h],
                "area": w * h,
                "iscrowd": 0
            })
            annotation_id += 1

    image_id += 1

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    json.dump(coco, f, indent=2)

print(f"✅ Saved COCO JSON to: {output_file}")
