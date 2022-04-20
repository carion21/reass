
import hashlib as hs
from datetime import datetime


class Risque:
    
    def __init__(self):
        self.code_risque = ""
        self.libelle_risque = ""
        self.classe_risque = ""
        self.libelle_classe_risque = ""

        self.id_risque = ""

        self.garanties = []

    def from_dict(self, data : dict) -> None:
        self.code_risque = data["code_risque"]
        self.libelle_risque = data["libelle_risque"]
        self.classe_risque = data["classe_risque"]
        self.libelle_classe_risque = data["libelle_classe_risque"]

        self.id_risque = data["id_risque"]

    def to_dict(self) -> dict:
        odict = {
            "code_risque": self.code_risque,
            "libelle_risque": self.libelle_risque,
            "classe_risque": self.classe_risque,
            "libelle_classe_risque": self.libelle_classe_risque,
            "id_risque": self.id_risque,
            "garanties": self.garanties
        }
        return odict

    """
    def generate_temporary_id_v1(self) -> None:
        source = self.libelle_classe_risque+"__"+self.classe_risque+"__"+self.libelle_classe_risque
        self.id_risque = generate_code(source)
    """


    def generate_temporary_id(self) -> None:
        source = self.libelle_classe_risque+"__"+self.classe_risque+"__"+self.libelle_classe_risque
        fnow = datetime.now().strftime("__%d-%m-%Y_%H:%M:%S")
        source = source + fnow
        hash_object = hs.sha256(source.encode())

        hex_dig = hash_object.hexdigest()
        self.id_risque = hex_dig
