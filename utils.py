

from classes.coassurance import Coassurance
from classes.facultative import Facultative
from classes.garantie import Garantie
from classes.risque import Risque

import hashlib as hs
from datetime import datetime



def generate_code(source : str) -> str:
    fnow = datetime.now().strftime("__%d-%m-%Y_%H:%M:%S")
    source = source + fnow
    hash_object = hs.sha256(b'{}'.format(source))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def to_dicts(objects : list) -> list:
    olist = []
    for obj in objects:
        olist.append(obj.to_dict())
    return olist