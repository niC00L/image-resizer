import os, sys, PIL
from PIL import Image
"""
you will need PIL to use this script
USAGE: python resizer.py <width> <height> <path> <filetypes>

width = desired width of image n px. If you want it calculated type x
height = desired height of image n px. If you want it calculated type x
  you cant leave both width and height as x
path = filepath, if you want to use current folder, type x
filetypes = if you want to resize only certain image extensions, write them as
  tuple, otherwise leave blank and default image extensions will be used
"""

Apath = sys.argv[1]
Awidth = sys.argv[2]
Aheight = sys.argv[3]
if len(sys.argv) == 5:
  Afiletypes = sys.argv[4]
else:
  Afiletypes = 'x'

def resize(width, height, files, directory, single=False):
  if (width == 'x') and (height == 'x'):
    print 'You need to set at least one size'
    exit()

  for image in files:
    if single:
      newDir = './resized'
      img = Image.open(image)
    else:
      img = Image.open(directory+'/'+image)
      newDir = directory+'/resized'
      
    if not os.path.exists(newDir):
      os.makedirs(newDir)    

    if width == 'x':
      height = int(height)
      Pheight = (height / float(img.size[1]))
      width = int((float(img.size[0]) * float(Pheight)))
      
    elif height == 'x':
      width = int(width)
      Pwidth = (width / float(img.size[0]))
      height = int((float(img.size[1]) * float(Pwidth)))      

    else:
      width = int(width)
      height = int(height)      
      Iwidth = img.size[0]
      Iheight = img.size[1]
      if (abs(Iwidth-width) > abs(Iheight-height)):
        Pwidth = (width / float(Iwidth))
        height = int((float(Iheight) * float(Pwidth)))        
      else:
        Pheight = (height / float(Iheight))
        width = int((float(Iwidth) * float(Pheight)))
    
    img = img.resize((width, height), PIL.Image.ANTIALIAS)    
    img.save(newDir+'/resized_'+image)
        
  print 'All resized'
  exit()
      
def get_files(directory, filetypes):

  if filetypes == 'x':
    filetypes = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
  
  file_name =  os.path.basename(sys.argv[0])
  if directory == 'x':
    directory = os.path.abspath(__file__).replace(file_name, '')

  files = []  
  single = False

  if directory.endswith(tuple(filetypes)):
    files.append(directory)
    single = True

  else:
    for f in os.listdir(directory):
      if os.path.splitext(f)[1].lower() in filetypes:
        files.append(f)

    if files == []:
      print 'No such files'
      exit()
    
  return resize(Awidth, Aheight, files, directory, single)

get_files(Apath, Afiletypes)


  
