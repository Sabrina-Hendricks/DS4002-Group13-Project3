import os

# Define the path to your data directory
data_dir = './Data'

# Loop through each breed directory
for breed in os.listdir(data_dir):
    breed_dir = os.path.join(data_dir, breed)
    if os.path.isdir(breed_dir):
        # List all image files in the breed directory
        images = os.listdir(breed_dir)
        
        # Rename each file in the format "Breed_1.jpg", "Breed_2.jpg", etc.
        for i, filename in enumerate(images, start=1):
            new_name = f"{breed}_{i}.jpg"
            old_path = os.path.join(breed_dir, filename)
            new_path = os.path.join(breed_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
