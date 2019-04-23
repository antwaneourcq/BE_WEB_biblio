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
    requete = "SELECT " + elmt + " FROM " + table + ";"
    curseur = cnx.cursor()
    curseur.execute(requete)
    lignes = curseur.fetchall()
    # s = ""
    for l in lignes: #l peut valoir elmt1, elmt2 si elmt = "elmt1, elmt2"
        print(l)
        # s += l
    curseur.close()
    #return s ###si besoin de récupérer un jour les données de lecture

def ajout_alcove(cnx, id, continent, ville, couleur, dispo, nb_places):
    #vérifier types + auto incrémentation de id ?
    requete = "INSERT INTO alcoves (id_objet_reservable, continent, ville, couleur disponibilite, nb_places) VALUES(%s,%s,%s,%s,%s,%s);"
    param = (id, continent, ville, couleur, dispo, nb_places)
    requete_sql(cnx, requete, param)

def maj_alcove(cnx, id, continent, ville, couleur, dispo, nb_places):
    #vérifier les données (types) + id existant
    requete = "UPDATE alcoves SET continent = %s, ville = %s, couleur = %s, disponibilite = %s, nb_places = %s WHERE id_objet_reservable = %s;"
    param = (continent, ville, couleur, dispo, nb_places, id)
    requete_sql(cnx, requete, param)

def suppression_alcove(cnx, id):
    #vérifier si l'alcove existe
    requete = "DELETE FROM alcoves WHERE id_objet_reservable = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

def requete_sql(cnx, requete, param):
    try :
        cnx.autocommit(False)
        curseur = cnx.cursor()
        curseur.execute(requete, param)
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()
    curseur.close()

def creation_Table_alcove(nom, fichier):
    #non fini
    with open(fichier, 'r') as f:
        i = 0
        cnx = createConnection()
        for i, line in enumerate(f):
            continent, ville, couleur, dispo, nb_places = line.split(';')
            ajout_alcove(cnx, i, continent, ville, couleur, dispo, nb_places)
            

### objets réservables

def ajout_obj_res(cnx, id, type_obj):
    requete = "INSERT INTO objets_reservables (id_objet_reservable, type_objet_reservable) VALUES(%s,%s);"
    param = (id, type_obj)
    requete_sql(cnx, requete, param)

def maj_objet_res(cnx, id, type_obj):
    pass