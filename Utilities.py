
#!/home/vlarobbyk/anaconda3/envs/ai python

__author__ = "vlarobbyk"
__copyright__ = "Grupo de Investigación en Inteligencia Artificial y Tecnologías de Asistencia"
__credits__ = ["V. Robles-Bykbaev"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "vlarobbyk"
__email__ = "vrobles@ups.edu.ec"
__status__ = "Production"

import numpy as np

import os
import re
import random

from shutil import copyfile

class Utilities:
    
    def __init__(self):
        self.regex = re.compile('([A-Z|a-z|0-9]+(_)?)+(-)[0-9]+(\.)(png)')
        self.ext = 'png'
        
        
    def list_corpus(self,path):
        _files = [path+'/'+_f for _f in os.listdir(path) if self.regex.match(_f)!=None]
        return _files
    
    def split_train_validation(self, _list, train = 0.8, train_dir = 'train', val_dir = 'validation'):
        key = None
        htable = {}
        vtable = {}
        total = 0
        pos = 0
        
        for entry in _list:
            key = entry.split('/')[-1].split('-')[0]
            if key not in htable:
                htable[key] = [entry]
            else:
                htable[key].append(entry)
        
        for key in htable:
            random.shuffle(htable[key])
            total = round(float(len(htable[key]))*(1.0-train))
            for i in range(total):
                pos = random.randint(0,len(htable[key])-1)
                if not key in vtable:
                    vtable[key] = [htable[key][pos]]
                    del htable[key][pos]
                else:
                    vtable[key].append(htable[key][pos])
                    del htable[key][pos]

        for key in htable:
            #print('Size. ',len(htable[key]),'|', len(vtable[key]))
            #print(htable[key],'\n',vtable[key])
            for e in htable[key]:
                copyfile(e,train_dir+'/'+e.split('/')[-1])
    
            for e in vtable[key]:
                copyfile(e,val_dir+'/'+e.split('/')[-1])


if __name__=="__main__":
    utilities = Utilities()
    htable = utilities.list_corpus(path = 'corpus/')
    utilities.split_train_validation(htable)
    
