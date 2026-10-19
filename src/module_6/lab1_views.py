import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r", encoding="utf-8") as file, open("analysis.csv", "w", encoding="utf-8") as analysis:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
 #       writer = csv.DictWriter(analysis, fieldnames=["id", "english_title","brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2)
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness
    
if __name__ == "__main__":
    main()

# Kevin  K. Lux-Sullivan
# 11Oct2026