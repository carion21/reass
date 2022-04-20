from classes.risque import Risque
from ctest import AVENANT

from classes.avenant import Avenant

data = AVENANT

avenant = Avenant()
avenant.from_dict(data)
avenant.change_cas(1)

print(avenant.to_dict())
print("--------------------------")

risque = Risque()
rd = {
    "code_risque": "",
    "libelle_risque": "1",
    "classe_risque": "1",
    "libelle_classe_risque": "1",
    "id_risque": "",
}
risque.from_dict(rd)
print(risque.to_dict())

print(avenant.add_risque(risque))
print(avenant.to_dict())

print()

