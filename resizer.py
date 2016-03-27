import os, sys, PIL
from PIL import Image
"""
you will need PIL to use this script
USAGE: in cmd python resizer.py width height path filetypes
width = desired width of image n px. If you want it calculated type x
height = desired height of image n px. If you want it calculated type x
  you cant leave both width and height as x
path = filepath, if you want to use current folder, type x
filetypes = if you want to resize only certain image extensions, write them as
  tuple, otherwise leave blank and default image extensions will be used
"""

Awidth = sys.argv[1]
Aheight = sys.argv[2]
Apath = sys.argv[3]
if len(sys.argv) == 4:
  Afiletypes = sys.argv[4]
else:
  Afiletypes = 'x'

def resize(width, height, files):
  if (width == 'x') and (height == 'x'):
    print 'You need to set at least one size'
    exit()

  for image in files:
    if width == 'x':
      height = int(height)
      img = Image.open(image)
      Pheight = (height / float(img.size[1]))
      Cwidth = int((float(img.size[0]) * float(Pheight)))
      img = img.resize((Cwidth, height), PIL.Image.ANTIALIAS)
      img.save('resized_'+image)
      
    elif height == 'x':
      width = int(width)
      img = Image.open(image)
      Pwidth = (width / float(img.size[0]))
      Cheight = int((float(img.size[1]) * float(Pwidth)))
      img = img.resize((width, Cheight), PIL.Image.ANTIALIAS)
      img.save('resized_'+image)
    
  print 'All resized'
  exit()
      
#Get names of all files in directory
def get_files(directory, filetypes):

  if filetypes == 'x':
    filetypes = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
  
  file_name =  os.path.basename(sys.argv[0])
  if directory == 'x':
    directory = os.path.abspath(__file__).replace(file_name, '')

  files = []  
  for f in os.listdir(directory):
    if os.path.splitext(f)[1].lower() in filetypes:
      files.append(f)

  if files == []:
    return 'No such files'
         
  return resize(Awidth, Aheight, files)

# Run the above function and store its results in a variable.   
files = get_files(Apath, Afiletypes)


  