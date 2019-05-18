from flask import session
import bdd

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
    nom = dataform['nom']
    mail = dataform['mail']
    message = dataform['message']

    info = "insComment_success"
    msg = bdd.add_commentData(nom, message, mail)
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

