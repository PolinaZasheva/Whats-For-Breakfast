from PIL import Image, ImageOps

infile = "belgianwaffle.jpg"
original_image = Image.open("Resources/" + infile)
size = (299, 299)
fit_and_resized_image = ImageOps.fit(original_image, size, Image.ANTIALIAS)
outfile = "Resources/resized_" + infile
fit_and_resized_image.save(outfile)
