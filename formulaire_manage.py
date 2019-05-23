from flask import session
import bdd, api_google
import SGBD as sgbd

#print("cal_select : ", session["cal_sel"])
def calendar_selected(name):
    session["calendar"] = ""
    session["europe"], session["amerique"], session["asie"], session["afrique"], session["oceanie"] = 0, 0, 0, 0, 0
    try:
        session.calendar = name
        session["sel_cal"] = name
        if name == 'europe':
            session["europe"] = 1
            session["calendar"] = "europe.bibliotheque.enac@gmail.com"

        if name == "afrique":
            session["afrique"] = 1
            session["calendar"] = "afrique.bibliotheque.enac@gmail!.com"
        
        if name == "amerique":
            session["amerique"] = 1
            session["calendar"] = "amerique.bibliotheque.enac@gmail.com"
        
        if name == "asie":
            session["asie"] = 1
            session["calendar"] = "asie.bibliotheque.enac@gmail.com"
        
        if name == "oceanie":
            session["oceanie"] = 1 
            session["calendar"] = "oceanie.bibliotheque.enac@gmail.com"
    except:
        return "calendar_to_choose"
    return "calendar_success"

def session_is_admin(id):
    try:
        session["is_admin"] = bdd.is_admin(id)
    except:
        session["is_admin"] = 0
    return session["is_admin"]

#authentification
def verif_connect(dataform):
    print('session : ', session)
    login = dataform['id_connexion']
    mdp = dataform['mdp_connexion']
    res = bdd.authentification(login, mdp)
    print(res)
    print('avant try de l authentification')
    # authentification réussie - initialisation des sessions
    try:
        session["mail"] = login
        session["id"] = res[0]["id_utilisateur"]
        session["nom"] = res[0]["nom"]
        session["prenom"] = res[0]["prenom"]
        #session["mail"] = res[0][mail] utilisé pour se conneter avant donc en soi inutile
        session["logged_in"] = 1
        page_redirect = ["reservation", "auth_success"]
        session_is_admin(session["id"])
        print("type de id : ", type(session["id"]))
    except (KeyError, IndexError): #as e:
        # echec d' authentification
        page_redirect = ["se_connecter", "auth_fail"]
    return page_redirect

def approve_deconnect():
    print('session : ', session)
    try:
        session["logged_in"] = 0
        page_redirect = ["index", "dec_success"]
        session.clear() #suppression de données de navigation après déconnexion
    except:
        page_redirect = ["se_deconnecter", "dec_fail"]
    return page_redirect

def add_comment(dataform):
    print('session : ', session)
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
    print('session : ', session)
    msg = "delComment_success"
    idC = dataform["idC"]
    res = bdd.del_commentData(idC)
    if res != "":
        msg = "delComment_success"
    return msg

def add_reservation(dataform):
    date = dataform['date']
    heure_debut = dataform['h_debut']
    heure_fin = dataform['h_fin']
    try:
        promo = dataform['promo']
        nb_pers = dataform['nb_pers']
    except KeyError:
        nb_pers = 1
        promo = "Bibliotheque"
    calendrier = session["calendar"]
    print("session pour calendrier : ", session)
    info = "insComment_success"
    #cnx = sgbd.createConnection()
    msg = api_google.creer_event(calendrier, date, heure_debut, heure_fin, promo, nb_pers)
    if msg != "":
        info="insReservation_fail"
    return info

def del_reservation(dataform):
    date = dataform['date']
    heure_debut = dataform['h_debut']
    info = "insComment_success"
    #cnx = sgbd.createConnection()
    msg = api_google.supprimer_event(date, heure_debut)
    if msg != "":
        info="insReservation_fail"
    return info

def get_mail_utilisateur():
    return session["mail"]