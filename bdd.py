import mysql.connector
from mysql.connector import errorcode


config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'bibliotheque',
        'raise_on_warnings': True
    }



#connexion au serveur de la base de données
def connexion():
    cnx = ""
    
    try:
        cnx = mysql.connector.connect(**config)
        print('CANAL TENTATIVE:',cnx)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    if not cnx:
        print("canal vide")
    return cnx


#fermeture de la connexion au serveur de la base de données
def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()




# transforme le résultat de la requete select en dictionnaire ayant pour index le nom des colonnes de la table en BD
def convert_dictionnary(cursor):
    columns = cursor.description
    result = []
    # reception des données sous forme de dictionnaire avec le nom des colonnes.
    for value in cursor.fetchall():
        tmp = {}
        for (index, column) in enumerate(value):
            tmp[columns[index][0]] = column
        result.append(tmp)
    return result


# teste l'authentification
def authentification(login,mdp):
    try:
        cnx = connexion()
        print('coucou ', cnx)
        cursor = cnx.cursor()
        print('hallo ', cursor)
        sql = "SELECT * FROM utilisateurs WHERE mail=%s AND mdp=%s LIMIT 1"
        param = (login, mdp)
        cursor.execute(sql, param)
        res = convert_dictionnary(cursor)
        close_bd(cursor, cnx)
        print(res)
    except mysql.connector.Error as err:
        res = "Failed authentification : {}".format(err)
    #finally:
    #close_bd(cursor, cnx)
    return res

def deconnexion():
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        
    except mysql.connector.Error as err:
        res = "Failed deconnexion : {}".format(err)
    finally:
        close_bd(cursor, cnx)
    return res

###suite à adapter pour nos tables

# récupère toutes les données de la table commentaire
def get_allCommentData():
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        sql = "SELECT * FROM commentaires"
        cursor.execute(sql)
        res = convert_dictionnary(cursor)
    except mysql.connector.Error as err:
        res = "Failed get comment data : {}".format(err)
    finally:
        close_bd(cursor, cnx)
        print('données : ', res)
    return res

# ajoute un commentaire dans la table commentaire
def add_commentData(nom, message, email):
    msg = ""
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        sql = "INSERT INTO commentaires (nom, comment, email) VALUES (%s, %s, %s);"
        param = (nom, message, email)
        cursor.execute(sql, param)
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed add_commentData : {}".format(err)
    finally:
        close_bd(cursor, cnx)
    return msg
# supprime un commentaire dans la table commentaire
def del_commentData(id_comment):
    msg = ""
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        sql = "DELETE FROM commentaires WHERE id_comment=%s;"
        param = (id_comment,)
        cursor.execute(sql, param)
        cnx.commit()
    except mysql.connector.Error as err:
        msg = "Failed del_commentData : {}".format(err)
    finally:
        close_bd(cursor, cnx)
    return msg

def get_allProbleme():
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        sql = "SELECT * FROM problemes"
        cursor.execute(sql)
        res = convert_dictionnary(cursor)
    except mysql.connector.Error as err:
        res = "Failed get problems data : {}".format(err)
    finally:
        close_bd(cursor, cnx)
        print('données : ', res)
    return res
