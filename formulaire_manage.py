from flask import session
import bdd
import SGBD as sgbd

#authentification
def verif_connect(dataform):
    login = dataform['login']
    mdp = dataform['MDP']
    res = bdd.authentification(login, mdp)

    # authentification réussie - initialisation des sessions
    try:
        session["id"] = res[0]["id_user"]
        session["nom"] = res[0]["nom"]
        session["prenom"] = res[0]["prenom"]
        session["logged_in"] = 1
        page_redirect = ["index", "auth_success"]
    except (KeyError, IndexError): #as e:
        # echec d' authentification
        page_redirect = ["login", "auth_fail"]

    return page_redirect

def add_comment(dataform):
    print("arrivé dans add_comment du formulaire")
    nom = dataform['nom']
    prenom = dataform['prenom']
    mail = dataform['mail']
    message = dataform['message']
    info = "insComment_success"
    cnx = sgbd.createConnection()
    msg = sgbd.ajout_commentaire(cnx, nom, prenom, mail, message)
    if msg != "":
        info="insComment_fail"
    return info

def del_comment(dataform):
    msg = "delComment_success"
    idC = dataform["idC"]
    res = bdd.del_commentData(idC)
    if res != "":
        msg = "delComment_success"

    return msg

