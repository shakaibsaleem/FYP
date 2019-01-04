!pip install -q mahotas
!pip install -q milk
!pip install -q jug 
!pip install -q Image

##from google.colab import auth
##auth.authenticate_user()
##
##from google.colab import drive
##drive.mount('/content/drive/')
from PIL import Image

##a = Image.open('/content/drive/Images_No_Human/abc.jpg')

# from google.colab import files
# uploaded = files.upload()

# #print(uploaded)
# for name, data in uploaded.items():
#   with open(name, 'wb') as f:
#     #f.write(data)
#     print ('saved file', name)

from glob import glob
import mahotas
import mahotas.features
import milk
from jug import TaskGenerator


def features_for(imname):
    img = mahotas.imread(imname)
    return mahotas.features.haralick(img).mean(0)
 


features_for(a)
