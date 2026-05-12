import os
from rembg import remove
from PIL import Image

input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

formats = (".png", ".jpg", ".jpeg", ".webp")

for file_name in os.listdir(input_folder):

    if file_name.lower().endswith(formats):

        input_path = os.path.join(input_folder, file_name)

        output_file = os.path.splitext(file_name)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_file)

        print(f"Processing: {file_name}")

        image = Image.open(input_path)

        result = remove(image)
        result = result.convert("RGBA")

        # White background
        white_bg = Image.new("RGBA", result.size, (255, 255, 255, 255))
        final_image = Image.alpha_composite(white_bg, result)

        final_image = final_image.convert("RGB")

        final_image.save(output_path, quality=100)

print("\n✅ Done!")