import os
from PIL import Image
from torch.utils.data import Dataset

class CarDamageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_files = []
        self.labels = []
        
        # Define damage categories
        self.damage_types = {
            'crack': 0,
            'scratch': 1,
            'tire_flat': 2,
            'dent': 3,
            'glass_shatter': 4,
            'lamp_broken': 5
        }
        
        # Load images from each damage category directory
        for damage_type, label in self.damage_types.items():
            damage_dir = os.path.join(root_dir, damage_type)
            if os.path.exists(damage_dir):
                for img_name in os.listdir(damage_dir):
                    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        self.image_files.append(os.path.join(damage_dir, img_name))
                        self.labels.append(label)

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = self.image_files[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label