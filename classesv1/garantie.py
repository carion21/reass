

class Garantie:
    
    def __init__(self):
        self.code_garantie = ""
        self.libelle_branche_reass = ""
        self.capitaux = 0
        self.smp = 0
        self.prime_nette = 0

        self.id_garantie = ""

        self.id_risque = ""

    def from_dict(self, data : dict) -> None:
        self.code_garantie = data["code_garantie"]
        self.libelle_branche_reass = data["libelle_branche_reass"]
        self.capitaux = data["capitaux"]
        self.smp = data["smp"]
        self.prime_nette = data["prime_nette"]

        self.id_risque = data["id_risque"]
        self.id_garantie = data["id_garantie"]

    def to_dict(self) -> dict:
        odict = {
            "id_risque": self.id_risque,
            "id_garantie": self.id_garantie,
            "code_garantie": self.code_garantie,
            "libelle_branche_reass": self.libelle_branche_reass,
            "capitaux": self.capitaux,
            "smp": self.smp,
            "prime_nette": self.prime_nette
        }
        return odict