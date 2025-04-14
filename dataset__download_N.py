# from lavis.datasets.builders.base_dataset_builder import load_dataset_config
# from lavis.datasets.builders import registry

# yaml_path = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/lavis/configs/datasets/coco/defaults_cap.yaml"
# cfg = load_dataset_config(yaml_path)
# builder = registry.get_builder_class("coco_caption")(cfg)
# dataset = builder.build_datasets()

# print(dataset["train"][0])


# import os

# # ✅ This must be set *before* importing LAVIS
# os.environ["DATA_DIR"] = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/my_datasets"
# os.environ["LAVIS_CONFIG_PATH"] = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/lavis/configs"

# from lavis.datasets.builders.base_dataset_builder import load_dataset_config
# from lavis.datasets.builders import registry

# # ✅ Use correct YAML path and dataset name
# yaml_path = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/lavis/configs/datasets/coco/defaults_cap.yaml"
# cfg = load_dataset_config(yaml_path)

# builder = registry.get_builder_class("coco_caption")(cfg)

# # ✅ This should now save to the path you defined above
# dataset = builder.build_datasets()

# print(dataset["train"][0])



import os
from lavis.datasets.builders import load_dataset_config, registry

# Set paths explicitly
os.environ["LAVIS_CONFIG_PATH"] = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/lavis/configs"
os.environ["DATA_DIR"] = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/my_datasets"  # ← add this!

# Load YAML config

yaml_path = "/home/draiman/Desktop/Nima/LAVIS_/LAVIS/lavis/configs/datasets/coco/defaults_cap.yaml"

cfg = load_dataset_config(yaml_path)

# Build dataset
builder = registry.get_builder_class("coco_caption")(cfg)
dataset = builder.build_datasets()

# Show sample
print(dataset["train"][0])
