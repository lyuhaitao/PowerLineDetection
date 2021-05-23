# AUTOGENERATED! DO NOT EDIT! File to edit: 01_my_data_structure.ipynb (unless otherwise specified).

__all__ = ['LPoints', 'Hline', 'ImageBuffer']

# Cell
class LPoints:
    "the class is used to record the points' indices in the original dataset."
    def __init__(self, args):
        '''
        args: a List array including the ID in original data
        '''
        k = [i for i in range(len(args))]
        dic = dict.fromkeys(k)
        for k,v in enumerate(args):
            dic[k] = v
        self.dic = dic


# Cell
class Hline(object):
    "a class is used to record the details of lines extracted by Hough Transform"
    '''
    coord: parameters of a line
    line: detailed coordinates
    '''
    def __init__(self, *args):
        self.coord = args[0]
        self.line = args[1]
        self.angle = args[2]
        self.dist = args[3]
    def getLengthOfLine(self):
        line = self.line
        return len(line)

# Cell
class ImageBuffer():
    "it is use to record the buffer image details of powerline corridors"
    def __init__(self, **kwargs):
        self.img = kwargs['img']
        self.coord = kwargs['coord']