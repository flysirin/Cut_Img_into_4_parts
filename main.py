from pathlib import Path
from PIL import Image

allowed_files = ['.jpg', '.jpeg', '.png']
source_path = 'source_images'
output_path = 'output_images'
CUT_AROUND_IMG = 2


def crop_image(file: Path) -> Image:
    current_suffix = file.suffix
    with Image.open(file) as img:

        width, height = img.size
        width = width - CUT_AROUND_IMG
        height = height - CUT_AROUND_IMG
        part_width = width // 2 - CUT_AROUND_IMG
        part_height = height // 2 - CUT_AROUND_IMG

        coordinates = [
            (CUT_AROUND_IMG, CUT_AROUND_IMG, part_width, part_height),  # Top left
            (part_width, CUT_AROUND_IMG, width, part_height),  # Top right
            (CUT_AROUND_IMG, part_height, part_width, height),  # Bottom left
            (part_width, part_height, width, height)  # Bottom right
        ]
        print(coordinates)
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
