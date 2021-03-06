# Python image resizer #

If you want to resize many images (or just one) to the same resolution, you can simply use this script. You're welcome.

To run this script, you will need Python 2 (obviously) and PIL Image library. I'm sure you're smart enought to figure out how to install these on your own.

Script doesn't resize images in subfolders. 
Resized images will be saved in subfolder named 'resized'. Their names will start with 'resized_'.

## Usage ##

```
#!python

python resizer.py <path> <width> <height> <filetypes>
```

* **width** - Desired max width of resized image. If you want it calculated type 'x'
* **height** - Desired max height of resized image. If you want it calculated type 'x'

You can't leave both width and height as 'x'. If you set both sizes, image will be resized to fit this resolution with maintained aspect ratio.

* **path** - Path to folder with images. If you want to use current folder, type 'x', else type absolute path i.e.:C:\Users\admin\Pictures (windows) or /home/user/Pictures (linux). 
If you want to resize single image, just type its name instead of path. 

* **filetypes** - File extensions you want to resize. By default script resizes .jpg, .jpeg, .png, .bmp and .gif files. If you want to resize certain filetypes type them as tuple, i.e.: ('.jpg', '.png'), else leave blank.

