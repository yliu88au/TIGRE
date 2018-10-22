from __future__ import print_function

import numpy as np
import tigre.geometry_default as geometry
import tigre_demo_file.Test_data.data_loader as data_loader
from tigre.Ax import Ax
from tigre.Utilities.plotproj import ppslice
from tigre.Utilities.plotproj import plotproj

geo = geometry.TIGREParameters(high_quality=False)
geo.mode = 'cone'
geo.COR = None
source_img = data_loader.load_head_phantom(number_of_voxels=geo.nVoxel)
angles = np.linspace(0, 2*np.pi, 100, dtype=np.float32)

projsirt = Ax(source_img, geo, angles, 'ray-voxel')
plotproj(projsirt)
#fdk=FDK(projsirt,geo,angles)
# blocksize=input('blocksize:')
niter = 5
# sart=SART(projsirt,geo,angles,niter,init='multigrid',OrderStrategy='angularDistance')
# ppslice(projsirt)


