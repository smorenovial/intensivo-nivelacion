from scipy import misc
l = misc.lena()
misc.imsave('lena.png', l) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(l)
plt.show()

lena = scipy.lena() 
lx, ly = lena.shape
 # Recorte de la imagen
crop_lena = lena[lx/4:-lx/4, ly/4:-ly/4]
 # up <-> down flip

rotate_lena = ndimage.rotate(lena, 45)
rotate_lena_noreshape = ndimage.rotate(lena, 45, reshape=False)