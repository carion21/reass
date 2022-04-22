from __future__ import annotations

from classes.coassurance import Coassurance
from classes.facultative import Facultative
from classes.garantie import Garantie
from classes.risque import Risque

#from utils import to_coassurances, to_dicts, to_factultatives, to_facultatives, to_garanties, to_risques


class Avenant:

    def __init__(self) -> None:
        self.deja_traite = 0
        self.garantie_par_risque = 0
        self.statut_coassurance = 0

        self.num_police = ""
        self.code_inter = ""
        self.num_avenant = ""

        self.code_assure = ""
        self.nom = ""
        self.prenoms = ""
        self.activite = ""
        self.date_effet = ""
        self.date_emission = ""
        self.date_echeance = ""

        self.code_categorie = ""
        self.libelle_categorie = ""
        self.code_branche = ""
        self.libelle_branche = ""

        self.risques = []
        self.garanties = []
        self.facultatives = []
        self.coassurances = []

        #self.cas = 0
        #self.cas = 1 => on suppose que chaque garantie est lié à un seul risque
        #self.cas = 2 => on suppose que toutes les garanties sont liées à tous les risques
    
        #on suppose le cas par défaut
        self.cas = 0

    def change_cas(self, cas : int):
        self.cas = cas
        self.attribute_garanties_to_risques()

    def from_dict(self, data : dict) -> None:
        self.deja_traite = data["deja_traite"]
        self.nom = data["nom"]
        self.prenoms = data["prenoms"]
        self.activite = data["activite"]
        self.date_effet = data["date_effet"]
        self.date_emission = data["date_emission"]
        self.date_echeance = data["date_echeance"]

        self.code_categorie = data["code_categorie"]
        self.libelle_categorie = data["libelle_categorie"]
        self.code_branche = data["code_branche"]
        self.libelle_branche = data["libelle_branche"]

        self.risques = to_risques(data["risques"],data["garanties"])
        self.garanties = to_garanties(data["garanties"])
        self.facultatives = to_facultatives(data["facultatives"])
        self.coassurances = to_coassurances(data["coassurances"])

    def to_dict(self):
        odict = {
            "deja_traite": self.deja_traite,
            "nom": self.nom,
            "prenoms": self.prenoms,
            "activite": self.activite,
            "date_effet": self.date_effet,
            "date_emission": self.date_emission,
            "date_emission": self.date_emission,
            "code_categorie": self.code_categorie,
            "libelle_categorie": self.libelle_categorie,
            "code_branche": self.code_branche,
            "libelle_branche": self.libelle_branche,
            "risques": to_dicts(self.risques),
            "garanties": to_dicts(self.garanties),
            "facultatives": to_dicts(self.facultatives),
            "coassurances": to_dicts(self.coassurances),
        }
        return odict


    def get_garanties_by_risque(self, risque : Risque) -> list[Garantie]:
        garanties = []
        for garantie in self.garanties:
            if garantie.id_risque == risque.id_risque:
                garanties.append(garantie)
        return garanties


    def attribute_garanties_to_risques(self) -> None:
        """
        Attribuer 'toutes les' garanties aux différents risques selon le cas de figure
        """
        nrisques = []
        for risque in self.risques:
            risque.garanties = self.get_garanties_by_risque(risque) if self.cas == 1 else self.garanties
            nrisques.append(risque)
        self.risques = nrisques

    def attribute_garantie_to_risques(self, garantie : Garantie) -> None:
        """
        Attribuer une garantie à un ou plusieurs risques de l'avenant actuel
        """
        nrisques = []
        for risque in self.risques:
            if garantie.id_risque == "-1":
                risque.garanties.append(garantie)
            else:
                if risque.id_risque == garantie.id_risque:
                    risque.garanties.append(garantie)
            nrisques.append(risque)
        self.risques = nrisques

    def takoff_garantie_to_risques(self, garantie : Garantie) -> None:
        """
        Retirer une garantie à un ou plusieurs risques de l'avenant actuel
        """
        nrisques = []
        for risque in self.risques:
            if garantie.id_risque == "-1":
                risque.garanties.append(garantie)
            else:
                if risque.id_risque == garantie.id_risque:
                    risque.garanties.append(garantie)
            nrisques.append(risque)
        self.risques = nrisques
    

    def find_a_risque(self, id_risque : str) -> tuple[bool,Risque,int]:
        exist = False
        arisque = None
        position= None
        for risque in self.risques:
            if risque.id_risque == id_risque:
                exist = True
                arisque = risque
                position = self.risques.index(risque)
                break
        return exist, arisque, position

    def find_a_garantie(self, garanties: list[Garantie], id_garantie : str) -> tuple[bool,Risque,int]:
        exist = False
        agarantie = None
        position= None
        for garantie in garanties:
            if garantie.id_garantie == id_garantie:
                exist = True
                agarantie = garantie
                position = garanties.index(garantie)
                break
        return exist, agarantie, position

    def find_a_facultative(self, id_facultative : str) -> tuple[bool,Facultative,int]:
        exist = False
        afacultative = None
        position= None
        for afac in self.facultatives:
            if afac.id_facultative == id_facultative:
                exist = True
                afacultative = afac
                position = self.facultatives.index(afac)
                break
        return exist, afacultative, position
    

    def find_a_coassurance(self, id_coass : str) -> tuple[bool,Coassurance,int]:
        exist = False
        acoassurance = None
        position= None
        for coass in self.coassurances:
            if coass.id_coass == id_coass:
                exist = True
                acoassurance = coass
                position = self.coassurances.index(coass)
                break
        return exist, acoassurance, position

    def add_risque(self, risque : Risque) -> bool:
        try:
            risque.generate_temporary_id()
            self.risques.append(risque)
            return True
        except: return False

    def remove_risque(self, risque : Risque) -> bool:
        verif, risque, i = self.find_a_risque(risque.id_risque)
        if verif:
            if self.cas == 2:
                self.risques.pop(i)
                return True
            else:
                vods = []
                for garantie in risque.garanties:
                    vod = self.remove_garantie(garantie)
                    vods.append(vod)
                verification_of_delete = True
                for vs in vods:
                    verification_of_delete = verification_of_delete and vs
                if verification_of_delete:
                    self.risques.pop(i)
                return verification_of_delete
        else: return False
        

    def add_garantie(self, garantie : Garantie) -> bool:
        if garantie.id_risque == "":
            return False
        else:
            try:
                self.attribute_garantie_to_risques(garantie)
                self.garanties.append(garantie)
                return True
            except: return False

    def remove_garantie(self, garantie : Garantie) -> bool:
        if garantie.id_risque == "":
            return False
        elif garantie.id_garantie == "":
            return False
        else:
            try:
                if garantie.id_risque != "-1":
                    exist_r, risque, ir = self.find_a_risque(garantie.id_risque)
                    if exist_r:
                        exist_g, garantie, ig = self.find_a_garantie(risque.garanties, garantie.id_garantie)
                        if exist_g:
                            risque.garanties.pop(ig)
                            self.risques[ir] = risque
                            return True
                        else: return False
                    else: return False
            except: return False

    def add_facultative(self, facultative : Facultative) -> bool:
        try: 
            self.facultatives.append(facultative)
            return True
        except: return False

    def remove_facultative(self, facultative : Facultative) -> bool:
        try:
            exist, _, position = self.find_a_facultative(facultative.id_facultative)
            if exist:
                self.facultatives.pop(position)
                return True
            else: return False
        except: return False

    def add_coassurance(self, coassurance : Coassurance) -> bool:
        try: 
            self.coassurances.append(coassurance)
            return True
        except: return False

    def remove_coassurance(self, coassurance : Coassurance) -> bool:
        try:
            exist, _, position = self.find_a_coassurance(coassurance.id_coass)
            if exist:
                self.coassurances.pop(position)
                return True
            else: return False
        except: return False


def attribute_garanties(datas : list, id_risque : str) -> list[Garantie]:
    garanties = [0]
    if len(datas) > 0:
        for data in datas:
            if data["id_risque"] == id_risque:
                garantie = Garantie()
                garantie.from_dict(data)
                garanties.append(garantie)
    return garanties
    
def to_risques(datas_of_risques : list, datas_of_garanties : list) -> list[Risque]:
    risques = []
    if len(datas_of_risques) > 0:
        for datar in datas_of_risques:
            risque = Risque()
            risque.from_dict(datar)
            risque.garanties = attribute_garanties(datas_of_garanties, risque.id_risque)
            risques.append(risque)
    return risques

def to_garanties(datas : list) -> list[Garantie]:
    garanties = []
    if len(datas) > 0:
        for data in datas:
            garantie = Garantie()
            garantie.from_dict(data)
            garanties.append(garantie)
    return garanties

def to_facultatives(datas : list) -> list[Facultative]:
    facultatives = []
    if len(datas) > 0:
        for data in datas:
            facultative = Facultative()
            facultative.from_dict(data)
            facultatives.append(facultative)
    return facultatives

def to_coassurances(datas : list) -> list[Coassurance]:
    coassurances = []
    if len(datas) > 0:
        for data in datas:
            coassurance = Coassurance()
            coassurance.from_dict(data)
            coassurances.append(coassurance)
    return coassurances

def to_dicts(objects : list) -> list:
    olist = []
    for obj in objects:
        olist.append(obj.to_dict())
    return olist

    
                
            



