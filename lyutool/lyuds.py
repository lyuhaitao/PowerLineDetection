# AUTOGENERATED! DO NOT EDIT! File to edit: 01_my_data_structure.ipynb (unless otherwise specified).

__all__ = ['LPoints']

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
