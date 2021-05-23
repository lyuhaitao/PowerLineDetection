# AUTOGENERATED! DO NOT EDIT! File to edit: 02_functions.ipynb (unless otherwise specified).

__all__ = ['generateLPByIDS', 'getPointsFromSource', 'locatePointsFromBuffer_3D', 'calOutlierByIQR',
           'generateLineBordersByBuffer']

# Cell
from .lyuds import *
import numpy as np

# Cell
def generateLPByIDS(idx):
    """generate a Lpoints class based on a point list.

       idx : bool type like [ True False  True False  True False  True  True False False]
    """
    a = np.argwhere(idx == True)
    a = a.T
    nid = a.ravel()
    return LPoints(nid)

# Cell
def getPointsFromSource(**kwargs):
    """ Based on the class LPoints, obtain points from the original data.

        {'LP': lp, 'POINTS':xyz}
    """
    lp = kwargs['LP']
    xyz = kwargs['POINTS']
    return xyz[list(lp.dic.values())]

# Cell
def locatePointsFromBuffer_3D(**kwargs):
    """
    Description: obtain points from original point cloud base on the image buffer in 3D space

                self-defined the range of Z axis (Height) is used.

    """
    img_buffer = kwargs['img_buffer']
    min_xyz = kwargs['min_xyz']
    pts = kwargs['pts']
    cellsize = kwargs['cellsize']
    zrange = kwargs['zrange'] # [z_min, z_max]
    z_min, z_max = zrange
    #
    ly, lx = np.nonzero(img_buffer)
    x_min, y_min = min_xyz[0:2]
    px = cellsize * lx + x_min
    py = cellsize * ly + y_min
    nid_line=[]
    zipped = zip(px,py)
    for i,j in zipped:
        fcx = np.logical_and(pts[:,0] >= i, pts[:,0] < (i + cellsize))
        fcy = np.logical_and(pts[:,1] >= j, pts[:,1] < (j + cellsize))
        fcz = np.logical_and(pts[:,2] >= z_min, pts[:,2] <= z_max)
        idx = np.logical_and(fcx, fcy)
        idx = np.logical_and(idx, fcz)
        a = np.argwhere(idx==True)
        a = a.ravel()
        nid_line = nid_line + a.tolist()
    return nid_line

# Cell
def calOutlierByIQR(a):
    """
    Calculating the Outlier Fences Using the Interquartile Range.
    return: [lower inner fence, lower outer fence, upper inner fence, upper outer fence]
    """
    iqr = np.quantile(a,0.75) - np.quantile(a,0.25)
    inner_para = iqr * 1.5
    outer_para = iqr * 3
    lower_inner_fence = np.quantile(a,0.25) - inner_para
    lower_outer_fence = np.quantile(a,0.25) - outer_para
    upper_inner_fence = np.quantile(a,0.75) + inner_para
    upper_outer_fence = np.quantile(a,0.75) + outer_para
    return {'lower_inner_fence': lower_inner_fence,
            'lower_outer_fence': lower_outer_fence,
            'upper_inner_fence': upper_inner_fence,
            'upper_outer_fence': upper_outer_fence
           }

# Cell
def generateLineBordersByBuffer(**kwargs):
    """
    generate borders of powerlines based on the corridors
    """
    img_buffer = kwargs['img_buffer']
    min_xyz = kwargs['min_xyz']
    pts = kwargs['pts'] # deep copy of the original data
    #
    b = np.zeros((pts.shape[0],2))
    pts = np.hstack((pts,b))
    #
    cellsize = kwargs['cellsize']
    ly, lx = np.nonzero(img_buffer)
    x_min, y_min = min_xyz[0:2]
    px = cellsize * lx + x_min
    py = cellsize * ly + y_min
    nid_line=[]
    zipped = zip(px,py)
    for i,j in zipped:
        fcx = np.logical_and(pts[:,0] >= i, pts[:,0] < (i + cellsize))
        fcy = np.logical_and(pts[:,1] >= j, pts[:,1] < (j + cellsize))
        idx = np.logical_and(fcx, fcy)
        a = pts[idx,2]
        if len(a) == 0:
            continue
        dic_border = calOutlierByIQR(a)
        lower_inner_fence = dic_border['lower_inner_fence']
        upper_inner_fence = dic_border['upper_inner_fence']
        pts[idx, 3] = lower_inner_fence
        pts[idx, 4] = upper_inner_fence
        #
        a = np.argwhere(idx==True)
        a = a.ravel()
        nid_line = nid_line + a.tolist()
    return pts[np.unique(nid_line)]