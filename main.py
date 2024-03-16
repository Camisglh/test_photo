import os
from PIL import Image


def create_images(folder_names, output_filename):
    """
    Функция merge_images_to_tiff объединяет изображения из указанных папок в один TIFF-файл.
    Она принимает два аргумента:
    1. folder_names - список имен папок, из которых нужно взять изображения
    2. output_filename - имя выходного TIFF-файла, в который будут объединены изображения
    """
    images = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for folder_name in folder_names:
        folder_path = os.path.join(current_dir, folder_name)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if file_path.endswith(".png"):
                image = Image.open(file_path)
                image = image.convert("RGB")
                images.append(image)

    widths, heights = zip(*(img.size for img in images))
    max_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new("RGB", (max_width, total_height), color="white")
    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.size[1]

    new_image.save(output_filename, "TIFF", compression="tiff_deflate")


if __name__ == "__main__":
    folder_names = input("Введите список папок через запятую: ").split(",")
    folder_names = [folder.strip() for folder in folder_names]
    output_filename = "Result.tif"
    create_images(folder_names, output_filename)
