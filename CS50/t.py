from PIL import Image, ImageFilter

fname = input("Image to open: ")

before = Image.open(fname)
after = before.filter(ImageFilter.FIND_EDGES)
after.save(f"after_{fname}")