from flask import session
import bdd, api_google
import SGBD as sgbd

#authentification
def verif_connect(dataform):
    login = dataform['id_connexion']
    mdp = dataform['mdp_connexion']
    res = bdd.authentification(login, mdp)
    print(res)
    print('avant try de l authentification')
    # authentification réussie - initialisation des sessions
    try:
        session["id"] = res[0]["id_utilisateur"]
        session["nom"] = res[0]["nom"]
        session["prenom"] = res[0]["prenom"]
        #session["mail"] = res[0][mail] utilisé pour se conneter avant donc en soi inutile
        session["logged_in"] = 1
        page_redirect = ["reservation", "auth_success"]
    except (KeyError, IndexError): #as e:
        # echec d' authentification
        page_redirect = ["se_connecter", "auth_fail"]

    return page_redirect

def approve_deconnect():
    try:
        session["logged_in"] = 0
        page_redirect = ["index", "dec_success"]
    except:
        page_redirect = ["se_deconnecter", "dec_fail"]
    return page_redirect

def add_comment(dataform):
    print("arrivé dans add_comment du formulaire")
    nom = dataform['last_name']
    prenom = dataform['first_name']
    mail = dataform['email']
    message = dataform['message']
    info = "insComment_success"
    cnx = sgbd.createConnection()
    print('formulaire add comment cnx : ', cnx, type(cnx))
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

def add_reservation(dataform):
    print("arrivé dans add_reservation du formulaire")
    date = dataform['date']
    heure_debut = dataform['h_debut']
    heure_fin = dataform['h_fin']
    promo = dataform['promo']
    nb_pers = dataform['nb_pers']
    info = "insComment_success"
    #cnx = sgbd.createConnection()
    msg = api_google.creer_event(date, heure_debut, heure_fin, promo, nb_pers)
    if msg != "":
        info="insReservation_fail"
    return info