from PIL import Image
import os

# Define paths
source_dir = r"d:\Coding\portfolio\Portfolio\assets\images"
dest_dir = r"C:\Users\DELL\.gemini\antigravity\brain\b61605ab-2d1a-4f85-8336-d9dac5a50486"

files = [
    ("contact-me-image.jpg", "preview_contact.jpg"),
    ("suit-image.jpg", "preview_suit.jpg")
]

print("Generating previews...")

for src_name, dest_name in files:
    try:
        src_path = os.path.join(source_dir, src_name)
        dest_path = os.path.join(dest_dir, dest_name)
        
        # Open and compress
        with Image.open(src_path) as img:
            # Resize if huge (e.g. > 2000px width)
            if img.width > 2000:
                ratio = 2000 / img.width
                new_size = (2000, int(img.height * ratio))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                
            # Save compressed
            img.save(dest_path, "JPEG", quality=85, optimize=True)
            
        print(f"Generated {dest_name}: {os.path.getsize(src_path)/1024/1024:.2f}MB -> {os.path.getsize(dest_path)/1024/1024:.2f}MB")
    except Exception as e:
        print(f"Error processing {src_name}: {e}")
