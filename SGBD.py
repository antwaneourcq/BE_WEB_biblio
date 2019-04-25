import mysql.connector
from mysql.connector import errorcode
config = {
    'user': 'root',
    'password': 'mysql',
    'host': 'localhost',
    'database': 'bibliotheque',
    'raise_on_warnings': True #à vérifier si virgule ou pas
}

### gestion du sql

def createConnection():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)

def closeConnection(cnx, cursor):
    cursor.close()
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

### alcove

def ajout_alcove(cnx, continent, ville, couleur, dispo, nb_places, id_espace_actuel):
    #vérifier types + auto incrémentation de id ?
    id = get_id_obj_res(cnx) + 1
    ajout_obj_res(cnx, id, "alcove")
    requete = "INSERT INTO alcove (id_objet_reservable, nom_continent, nom_ville, couleur, disponibilite, nb_places, id_espace_actuel) VALUES(%s,%s,%s,%s,%s,%s);"
    param = (id, continent, ville, couleur, dispo, nb_places, id_espace_actuel)
    requete_sql(cnx, requete, param)

def maj_alcove(cnx, id, continent, ville, couleur, dispo, nb_places, id_espace_actuel):
    #vérifier les données (types) + id existant
    requete = "UPDATE alcove SET nom_continent = %s, nom_ville = %s, couleur = %s, disponibilite = %s, nb_places = %s, id_espace_actuel = %s WHERE id_objet_reservable = %s;"
    param = (continent, ville, couleur, dispo, nb_places, id_espace_actuel, id)
    requete_sql(cnx, requete, param)

def suppression_alcove(cnx, id):
    #vérifier si l'alcove existe
    suppression_objet_res(cnx, id)
    #requete = "DELETE FROM alcove WHERE id_objet_reservable = %s;"
    #param = (id)
    #requete_sql(cnx, requete, param)         

### objets réservables

def ajout_obj_res(cnx, id, type_obj):
    requete = "INSERT INTO objets_reservables (id_objet_reservable, type_objet_reservable) VALUES(%s,%s);"
    param = (id, type_obj)
    requete_sql(cnx, requete, param)

def maj_objet_res(cnx, id, type_obj):
    requete = "UPDATE objets_reservables SET type_objet_reservable = %s WHERE id_objet_reservable = %s;"
    param = (type_obj, id)
    requete_sql(cnx, requete, param)

def suppression_objet_res(cnx, id):
    requete = "DELETE FROM objets_reservables WHERE id_objet_reservable = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

def get_id_obj_res(cnx): #en attente de Louli
    requete = "SELECT max(id) FROM objets_reservables"
    try :
        cnx.autocommit(False)
        curseur = cnx.cursor()
        curseur.execute(requete)
        id = curseur.fetchone()
        cnx.commit()
    except Exception as e:
        print(e)
        cnx.rollback()
    curseur.close()
    return id

### ressources externes

def ajout_res_ext(cnx, id, nom_ressource, etat_ressource, disponibilite):
    requete = "INSERT INTO ressources_externes (id_objet_reservable, nom_ressource, etat_ressource, disponibilite) VALUES(%s,%s,%s,%s);"
    param = (id, nom_ressource, etat_ressource, disponibilite)
    requete_sql(cnx, requete, param)

def maj_res_ext(cnx, id, nom_ressource, etat_ressource, disponibilite):
    requete = "UPDATE ressources_externes SET nom_ressource = %s, etat_ressource = %s, disponibilite = %s WHERE id_objet_reservable = %s;"
    param = (nom_ressource, etat_ressource, disponibilite, id)
    requete_sql(cnx, requete, param)

def suppression_res_ext(cnx, id):
    requete = "DELETE FROM ressources_externes WHERE id_objet_reservable = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### ressources internes

def ajout_res_int(cnx, id, nom_ressource, id_espace_actuel):
    requete = "INSERT INTO ressources_internes (id_objet_reservable, nom_ressource, id_espace_actuel) VALUES(%s,%s,%s);"
    param = (id, nom_ressource, id_espace_actuel)
    requete_sql(cnx, requete, param)

def maj_res_int(cnx, id, nom_ressource, id_espace_actuel):
    requete = "UPDATE ressources_internes SET nom_ressource = %s, id_espace_actuel = %s WHERE id_objet_reservable = %s;"
    param = (nom_ressource, id_espace_actuel, id)
    requete_sql(cnx, requete, param)

def suppression_res_int(cnx, id):
    requete = "DELETE FROM ressources_internes WHERE id_objet_reservable = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### utilisateur id_utilisateur, mail, mdp, nom, prenom
    
def ajout_utilisateur(cnx, id, mail, mdp, nom, prenom):
    requete = "INSERT INTO utilisateur (id_utilisateur, mail, mdp, nom, prenom) VALUES(%s,%s,%s,%s,%s);"
    param = (id, mail, mdp, nom, prenom)
    requete_sql(cnx, requete, param)

def maj_utilisateur(cnx, id, mail, mdp, nom, prenom):
    requete = "UPDATE utilisateur SET mail = %s, mdp = %s, nom = %s, prenom = %s WHERE id_utilisateur = %s;"
    param = (mail, mdp, nom, prenom, id)
    requete_sql(cnx, requete, param)

def suppression_utilisateur(cnx, id):
    requete = "DELETE FROM utilisateur WHERE id_utilisateur = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### enseignants id_utilisateur, matiere

def ajout_enseignant(cnx, id, matiere):
    requete = "INSERT INTO enseignants(id_utilisateur, matiere) VALUES(%s,%s);"
    param = (id, matiere)
    requete_sql(cnx, requete, param)

def maj_enseignant(cnx, id, matiere):
    requete = "UPDATE enseignants SET matiere = %s WHERE id_utilisateur = %s;"
    param = (matiere, id)
    requete_sql(cnx, requete, param)

def suppression_enseignant(cnx, id):
    requete = "DELETE FROM enseignants WHERE id_utilisateur = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### eleves id_, promotion

def ajout_eleve(cnx, id, promotion):
    requete = "INSERT INTO eleves(id_utilisateur, promotion) VALUES(%s,%s);"
    param = (id, promotion)
    requete_sql(cnx, requete, param)

def maj_eleve(cnx, id, promotion):
    requete = "UPDATE eleves SET promotion = %s WHERE id_utilisateur = %s;"
    param = (promotion, id)
    requete_sql(cnx, requete, param)

def suppression_eleve(cnx, id):
    requete = "DELETE FROM eleves WHERE id_utilisateur = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### administrateurs id_ut

def ajout_admin(cnx, id):
    requete = "INSERT INTO administateurs(id_utilisateur) VALUES(%s);"
    param = (id)
    requete_sql(cnx, requete, param)

def suppression_admin(cnx, id):
    requete = "DELETE FROM administrateurs WHERE id_utilisateur = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

### reserver date, duree, heure, id_objet_reservable, id_reservation, id_utilisateur, nb_pers

def ajout_reserver(cnx, id, date, duree, heure, id_objet_reservable, id_utilisateur, nb_pers):
    requete = "INSERT INTO reserver (id_reservation, date, duree, heure, id_objet_reservable, id_utilisateur, nb_pers) VALUES(%s,%s,%s,%s,%s,%s,%s);"
    param = (id, date, duree, heure, id_objet_reservable, id_utilisateur, nb_pers)
    requete_sql(cnx, requete, param)

def maj_reserver(cnx, id, date, duree, heure, id_objet_reservable, id_utilisateur, nb_pers):
    requete = "UPDATE reserver SET date = %s, duree = %s, heure = %s, id_objet_reservable = %s, id_utilisateur = %s, nb_pers = %s WHERE id_utilisateur = %s;"
    param = (date, duree, heure, id_objet_reservable, id_utilisateur, nb_pers, id)
    requete_sql(cnx, requete, param)

def suppression_reserver(cnx, id):
    requete = "DELETE FROM reserver WHERE id_reservation = %s;"
    param = (id)
    requete_sql(cnx, requete, param)

'''
def creation_Table_alcove(nom, fichier):
    #non fini
    with open(fichier, 'r') as f:
        i = 0
        cnx = createConnection()
        for i, line in enumerate(f):
            continent, ville, couleur, dispo, nb_places = line.split(';')
            ajout_alcove(cnx, i, continent, ville, couleur, dispo, nb_places)
'''

def read():
    cnx = createConnection()
    cursor = cnx.cursor()
    requete = "SELECT * FROM objets_reservables"
    curseur = cnx.cursor()
    curseur.execute(requete)
    d = curseur.fetchone()
    curseur.close()
    return d