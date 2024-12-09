from PIL import Image, ImageOps
import sys


def main():
    # Check for CLA:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".png"):
        sys.exit(f"Invalid input file {sys.argv[1]}")
    if not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".png"):
        sys.exit(f"Invalid output file {sys.argv[2]}")
    if sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
        sys.exit("Input and output have different extensions")

    # Open input file and check for existence
    try:
        with Image.open(sys.argv[1]) as im:
            image_mask = Image.open("shirt.png")
            size = image_mask.size
            im = ImageOps.fit(im, size)
            im.paste(image_mask, image_mask)
            im.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit(f"Input image {sys.argv[1]} does not exist")


if __name__ == "__main__":
    main()
