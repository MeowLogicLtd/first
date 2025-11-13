from PIL import Image       ## Pillow helps to resize the pictures and make GIFs
import imageio.v3 as iio    ## Imageio helps to create GIF
import os                   ## Helps to define path for the INPUT images

# Target size for all frames
target_size = (300, 300)

# List of input image filenames
input_folder = 'input_images'                       # Folder where your images are stored
filenames = ['sean1.png', 'sean2.png', 'sean3.png', 'sean4.png', 'sean5.png']
images = []

for filename in filenames:
    # Open and resize with Pillow
    path = os.path.join(input_folder, filename)  ## Open the input file w/images 

    # Resize with Pillow
    img = Image.open(path).resize(target_size, Image.Resampling.LANCZOS) ## Use path if the imgs are not in the same folder. Replace w/"filename" - same folder.
    
    # Convert to numpy array for imageio
    images.append(img)

# Save as GIF
iio.imwrite('sean_bean.gif', images, duration=500, loop=0)

