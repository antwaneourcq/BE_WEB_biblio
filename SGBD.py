import mysql.connector

config = {
    'user': 'root',
    'password': 'mysql',
    'host': 'localhost',
    'database': 'be_Web_Bibliotheque',
    'raise_on_warnings': True, #à vérifier si virgule ou pas
}

def createConnection():
    cnx = None
    try:
        cnx = mysql.connector.connect(**config)
    except Exception as e:
        print("Error :"+ e)
    return cnx

def closeConnection(cnx):
    cnx.close()

def afficher(cnx, table, elmt="*"):
    """table et elmt en chaine de caractere"""
    requete = "SELECT" + elmt + "FROM" + table ";"
    curseur = cnx.cursor()
    curseur.execute(requete)
    lignes = curseur.fetchall()
    # s = ""
    for l in lignes: #l peut valoir elmt1, elmt2 si elmt = "elmt1, elmt2"
        print(l)
        # s += l
    curseur.close()
    #return s ###si besoin de récupérer un jour les données de lecture

def modification_Espace(cnx, modif, id, continent='', ville='', couleur='', dispo='', nb_places=''):
    """
    suppression=0: absence d'argument supplémentaire\n
    ajout=1: ordre d'argument: continent, ville, couleur, dispo, nb_places \n
    mise a jour=2: ordre d'argument: continent, ville, couleur, dispo, nb_places\n
    exemple d'ajout : (cnx, 1, "10", "Antarctique", "Dumont d’Urville", "blanc", "8-10/16-18", "10")
    """

    if modif==0:
        requete = "DELETE FROM Espaces WHERE idEspace = %s;"
        param = (id)
    else:
        #traitement des cas où un champ n'est pas valide...
        continent, ville, couleur, dispo, nb_places = l_param[0], l_param[1], l_param[2], l_param[3], l_param[4]
        if modif==1:
            requete = "INSERT INTO Espaces (idEspace, continent, ville, couleur disponibilite, nb_places) VALUES(%s,%s,%s,%s,%s,%s)"
            param = (id, continent, ville, couleur, dispo, nb_places)
        elif modif==2:
            requete = "UPDATE Espaces SET continent = %s, ville = %s, couleur = %s, disponibilite = %s, nb_places = %s WHERE idEspace = %s;"
            param = (continent, ville, couleur, dispo, nb_places, id)  
        else:
            print("Erreur de saisie")
            modification_Espace()
    try :
        cnx.autocommit(False)
        curseur = cnx.cursor()
        curseur.execute(requete, param)
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()
    curseur.close()

def creation_Table_Espace(nom, fichier):
    with open(fichier,r) as f:
        i = 0
        cnx = createConnection()
        for l in lignes:
            param = l.split(';')
            modification_Espace(cnx, 1, i, param)
            i += 1

    