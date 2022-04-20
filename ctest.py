AVENANT = {
        "deja_traite": 0, 
        "garantie_par_risque": 1,
        "statut_coassurance": 0,  # 0: aucun, -1: accepteur, 1: cession

        "num_police": "1252",
        "code_inter": "12",
        "num_avenant": "2",

        "code_assure": "",
        "nom": "",
        "prenoms": "",
        "activite": "",

        "date_effet": "04/08/2022",
        "date_emission": "04/08/2021",  # date_comp
        "date_echeance": "04/08/2021",

        "code_categorie": "",
        "libelle_categorie": "",
        "code_branche": "",
        "libelle_branche": "",

        "risques": [
            {
                "code_risque": "1",
                "libelle_risque": "1",
                "classe_risque": "1",
                "libelle_classe_risque": "1",
                "id_risque": "1",
            },
            {
                "code_risque": "",
                "libelle_risque": "",
                "classe_risque": "",
                "libelle_classe_risque": "",
                "id_risque": "5"
            }
        ],

        "garanties": [
            {
                "code_garantie": "",
                "libelle_branche_reass": "",
                "capitaux": 1000,
                "smp": 1500,
                "prime_nette": 100,

                "id_risque": "",  # prend -1 si le risque correspond à tous les risques sinon
                "id_garantie": "5"  # prend -1 si le risque correspond à tous les risques sinon
            },
            {
                "code_garantie": "",
                "libelle_branche_reass": "",
                "capitaux": 1000,
                "smp": 1500,
                "prime_nette": 100,

                "id_risque": "",
                "id_garantie": "4"  # prend -1 si le risque correspond à tous les risques sinon
            }
        ],

        "facultatives": [
            {
                "code_reass": "",
                "reassureur": "",
                "taux_fac": "",
                "tauxx_commission": "",

                "code_branche_assurance": "4",
                "libelle_branche_reass": "",

                "prime_fac": "",
                "montant_commission": "",
                "capitaux_net": "",

                "id_facultative": "52"
            },
            {
                "code_reass": "",
                "reassureur": "",
                "taux_fac": "",
                "tauxx_commission": "",

                "code_branche_assurance": "5",
                "libelle_branche_reass": "",

                "prime_fac": "",
                "montant_commission": "",
                "capitaux_net": "",

                "id_facultative": "45"
            },
            {
                "code_reass": "",
                "reassureur": "",
                "taux_fac": "",
                "tauxx_commission": "",

                "code_branche_assurance": "",
                "libelle_branche_reass": "",

                "prime_fac": "",
                "montant_commission": "",
                "capitaux_net": "",

                "id_facultative": "22"
            },
            {
                "code_reass": "",
                "reassureur": "",
                "taux_fac": "",
                "tauxx_commission": "",

                "code_branche_assurance": "",
                "libelle_branche_reass": "",

                "prime_fac": "",
                "montant_commission": "",
                "capitaux_net": "",

                "id_facultative": "24"
            }
        ],

        "coassurances": [
            {
                "statut": "",
                "part_coass": "",
                "nom_coassureur": "",
                "taux_coass": "",
                "id_coass": "65"
            },
            {
                "statut": "",
                "part_coass": "",
                "nom_coassureur": "",
                "taux_coass": "",
                "id_coass": "21"
            }
        ],

        "cession_legale": {
            "annee": "",
            "taux_cl": ""
        }
    }
