from pathlib import Path
from PIL import Image

allowed_files: list = ['.jpg', '.jpeg', '.png', '.bmp']
source_path: str = 'source_images'
output_path: str = 'output_images'
CUT_AROUND_IMG: int = 2


def crop_image(file: Path, cut_around: int = 0) -> Image:
    cut = cut_around
    current_suffix = file.suffix

    with Image.open(file) as img:
        width, height = img.size
        width = width
        height = height
        part_width = width // 2
        part_height = height // 2

        coordinates = [
            (cut, cut, part_width - cut, part_height - cut),  # Top left
            (part_width + cut, cut, width - cut, part_height - cut),  # Top right
            (cut, part_height + cut, part_width - cut, height - cut),  # Bottom left
            (part_width + cut, part_height + cut, width - cut, height - cut)  # Bottom right
        ]
        parts = [img.crop(coord) for coord in coordinates]
        for i, part in enumerate(parts):
            part.save(f"{output_path}//{file.stem}//{file.name}_{i + 1}.{current_suffix}")


def cut_images_from_dir(source_dir: str = source_path,
                        output_dir: str = output_path,
                        cut_around: int = 0) -> None:

    folder = Path(source_dir)
    Path(f"{output_dir}//").mkdir(parents=True, exist_ok=True)

    for file in folder.iterdir():
        if file.is_file() and file.suffix in allowed_files:
            Path(f"{output_dir}//{file.stem}").mkdir(exist_ok=True)
            crop_image(file, cut_around=cut_around)


if __name__ == '__main__':
    cut_images_from_dir(source_dir=source_path,
                        output_dir=output_path,
                        cut_around=CUT_AROUND_IMG)
