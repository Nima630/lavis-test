
# from omegaconf import OmegaConf
# from lavis.common.registry import registry
# import torch

# # Load config YAML (directly with OmegaConf)
# cfg = OmegaConf.load("lavis/projects/blip2/train/qformer_scratch.yaml")

# # Get dataset config block
# coco_cfg = cfg.datasets["coco_caption"]

# # Get builder and pass the dataset config
# builder_cls = registry.get_builder_class("coco_caption")
# builder = builder_cls(coco_cfg)

# # Build the dataset (usually a dict of splits like 'train')
# datasets = builder.build_datasets()
# train_dataset = datasets["train"]

# # Wrap in DataLoader
# loader = torch.utils.data.DataLoader(train_dataset, batch_size=1, shuffle=False)

# # Get and print a sample
# samples = next(iter(loader))

# print("\n=== SAMPLE KEYS ===")
# print(samples.keys())

# print("\n=== SAMPLE CONTENT ===")
# for k, v in samples.items():
#     print(f"{k}: {type(v)}, shape: {getattr(v, 'shape', 'N/A')}")
#     if isinstance(v, list):
#         print(f"  First item: {v[0]}")




# import json
# import os

# src = "./my_datasets/coco/annotations/coco_karpathy_train.json"
# dst = "./my_datasets/coco/annotations/coco_tiny_train.json"

# os.makedirs(os.path.dirname(dst), exist_ok=True)

# with open(src, "r") as f:
#     data = json.load(f)

# small_data = data[:100]

# with open(dst, "w") as f:
#     json.dump(small_data, f)

# print(f"✅ Wrote {len(small_data)} samples to {dst}")




import json

src = "my_datasets/coco/annotations/coco_karpathy_train.json"
dst = "my_datasets/coco/annotations/coco_tiny_train.json"

with open(src, "r") as f:
    data = json.load(f)

# Take only the first 10 examples
tiny_data = data[:10]

with open(dst, "w") as f:
    json.dump(tiny_data, f, indent=2)  # Add indent for readability
