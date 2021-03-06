# Project name here
> Summary description here.


This file will become your README and also the index of your documentation.

## Install

`pip install your_project_name`

## How to use

Fill me in please! Don't forget code examples:

```python
np.array([1,2,3])
```




    array([1, 2, 3])



```python
las_fp = pathlib.Path('/home/hxl170008/data/t_remain.las')
point_cloud = lp.file.File(las_fp, mode='r')
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
dc = grid_subsampling(points, 1/2)
grid_barycenter = dc['barycenter']
grid_candidate = dc['candidate']
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-5e5131c42ccc> in <module>
          2 point_cloud = lp.file.File(las_fp, mode='r')
          3 points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
    ----> 4 dc = grid_subsampling(points, 1/2)
          5 grid_barycenter = dc['barycenter']
          6 grid_candidate = dc['candidate']


    ~/code/lyutool/lyutool/core.py in grid_subsampling(points, voxel_size)
          7     "Define a function that takes as input an array of points, and a voxel size expressed in meters."
          8     "It returns the sampled point cloud"
    ----> 9     nb_vox=np.ceil((np.max(points, axis=0) - np.min(points, axis=0))/voxel_size)
         10     a = ((points - np.min(points, axis=0)) // voxel_size).astype(int)
         11     non_empty_voxel_keys, inverse, nb_pts_per_voxel= np.unique(a, axis=0, return_inverse=True, return_counts=True)


    NameError: name 'np' is not defined


```python
%matplotlib notebook
decimated_points = np.array(grid_candidate)
plt.figure(figsize=[8,8])
ax = plt.axes(projection='3d')
ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2], s=0.01)
ax.view_init(azim = 180+40,elev = 30)
plt.show()
```
