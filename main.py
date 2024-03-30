from pathlib import Path
from PIL import Image

allowed_files = ['.jpg', '.jpeg', '.png']
source_path = 'source_images'
output_path = 'output_images'


def crop_image(file: Path) -> Image:
    current_suffix = file.suffix
    with Image.open(file) as img:

        width, height = img.size
        part_width = width // 2
        part_height = height // 2

        coordinates = [
            (0, 0, part_width, part_height),  # Top left
            (part_width, 0, width, part_height),  # Top right
            (0, part_height, part_width, height),  # Bottom left
            (part_width, part_height, width, height)  # Bottom right
        ]

        parts = [img.crop(coord) for coord in coordinates]
        for i, part in enumerate(parts):
            part.save(f"{output_path}//{file.stem}//{file.name}_{i + 1}.{current_suffix}")


def cut_images_from_dir(source_dir: str = source_path, output_dir: str = output_path) -> None:
    folder = Path(source_dir)
    Path(f"{output_dir}//").mkdir(parents=True, exist_ok=True)

    for file in folder.iterdir():
        if file.is_file() and file.suffix in allowed_files:
            Path(f"{output_dir}//{file.stem}").mkdir(exist_ok=True)
            crop_image(file)


cut_images_from_dir()
