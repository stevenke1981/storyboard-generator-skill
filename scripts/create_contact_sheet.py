#!/usr/bin/env python3
"""Create a storyboard contact sheet from generated panel images."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a labeled storyboard contact sheet.")
    parser.add_argument("--input-dir", required=True, help="Directory containing panel images.")
    parser.add_argument("--output", required=True, help="Output PNG/JPG/WebP path.")
    parser.add_argument("--columns", type=int, default=4, help="Number of columns in the grid.")
    parser.add_argument("--thumb-width", type=int, default=420, help="Thumbnail width in pixels.")
    parser.add_argument("--label-height", type=int, default=38, help="Label strip height in pixels.")
    parser.add_argument("--padding", type=int, default=18, help="Outer and inter-cell padding.")
    parser.add_argument("--background", default="#f4f1eb", help="Canvas background color.")
    parser.add_argument("--label-background", default="#171717", help="Label strip color.")
    parser.add_argument("--label-fill", default="#ffffff", help="Label text color.")
    return parser.parse_args()


def load_font(size: int) -> ImageFont.ImageFont:
    for font_name in ("arial.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def list_images(input_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def make_thumbnail(path: Path, width: int) -> Image.Image:
    with Image.open(path) as source:
        image = source.convert("RGB")
    height = max(1, round(image.height * width / image.width))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> int:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output = Path(args.output)
    images = list_images(input_dir)

    if not images:
        raise SystemExit(f"No images found in {input_dir}")
    if args.columns < 1:
        raise SystemExit("--columns must be >= 1")

    thumbs = [(path, make_thumbnail(path, args.thumb_width)) for path in images]
    thumb_height = max(thumb.height for _, thumb in thumbs)
    cell_width = args.thumb_width
    cell_height = thumb_height + args.label_height
    rows = math.ceil(len(thumbs) / args.columns)

    canvas_width = args.padding + args.columns * (cell_width + args.padding)
    canvas_height = args.padding + rows * (cell_height + args.padding)
    canvas = Image.new("RGB", (canvas_width, canvas_height), args.background)
    draw = ImageDraw.Draw(canvas)
    font = load_font(22)

    for index, (path, thumb) in enumerate(thumbs):
        row = index // args.columns
        column = index % args.columns
        x = args.padding + column * (cell_width + args.padding)
        y = args.padding + row * (cell_height + args.padding)
        image_y = y + args.label_height

        draw.rectangle([x, y, x + cell_width, y + args.label_height], fill=args.label_background)
        label = path.stem
        draw.text((x + 12, y + 7), label, fill=args.label_fill, font=font)
        canvas.paste(thumb, (x, image_y))

        if thumb.height < thumb_height:
            draw.rectangle(
                [x, image_y + thumb.height, x + cell_width, image_y + thumb_height],
                fill=args.background,
            )

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
