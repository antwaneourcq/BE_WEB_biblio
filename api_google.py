from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import session
import SGBD


id_objet_reservable = None

def get_id_utilisateur():
    #à coder (voir si on garde le mail)
    #SGBD.createConnection()
    id_utilisateur = session['id']
    #SGBD.closeConnection()
    return id_utilisateur

#id_utilisateur = get_id_utilisateur()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']




def se_connecter():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    filename_token = 'token.pickle'
    
    if session['europe']==1:
        filename_token = "token_europe.pickle"
    if session["asie"]==1:
        filename_token = "token_asie.pickle"
    if session["amerique"]==1:
        filename_token = "token_amerique.pickle"
    if session["oceanie"]==1:
        filename_token = "token_oceanie.pickle"
    else:
        filename_token = "token_afrique.pickle"

    if os.path.exists(filename_token):
        with open(filename_token, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(filename_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


def creer_event(calendrier, date, heure_debut, heure_fin, promo, nb_pers):
    # format 'AAAA-MM-JJ' date
    # format 'HH-MM-SS' heure_d
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    print("calendrier sélectionné api : ", calendrier)

    filename_token = 'token.pickle'
    if session['europe']==1:
        filename_token = "token_europe.pickle"
        id_objet_reservable = 1
    if session["asie"]==1:
        filename_token = "token_asie.pickle"
        id_objet_reservable = 4
    if session["amerique"]==1:
        filename_token = "token_amerique.pickle"
        id_objet_reservable = 3
    if session["oceanie"]==1:
        filename_token = "token_oceanie.pickle"
        id_objet_reservable = 5
    else:
        filename_token = "token_afrique.pickle"
        id_objet_reservable = 2

    if os.path.exists(filename_token):
        with open(filename_token, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(filename_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': 'Occupé',
        'location': '',
        'description': "identifiant :"+ session["mail"] + " promo :" + promo + " nombre de personnes : " + str(nb_pers),
        'start': {
            'dateTime': date + 'T' + heure_debut + ':00+02:00',
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': date + 'T' + heure_fin + ':00+02:00',
            'timeZone': 'Europe/Paris',

        },
    }
    event = service.events().insert(calendarId=calendrier, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    id_utilisateur = session["id"]
    print("id: ", session['id'], session['mail'])
    ###partie base de donnée
    cnx = SGBD.createConnection()
    msg = SGBD.ajout_reserver(cnx, date, heure_debut, heure_fin, id_objet_reservable, id_utilisateur, nb_pers)
    SGBD.closeConnection(cnx, cnx.cursor()) #a rendre plus joli
    return msg


def supprimer_event(date, heure_debut):
    # format 'AAAA-MM-JJ' date
    # format 'HH-MM-SS' heure_d
    #heure_fin = heure_debut
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    filename_token = 'token.pickle'
    if session['europe']==1:
        filename_token = "token_europe.pickle"
    if session["asie"]==1:
        filename_token = "token_asie.pickle"
    if session["amerique"]==1:
        filename_token = "token_amerique.pickle"
    if session["oceanie"]==1:
        filename_token = "token_oceanie.pickle"
    else:
        filename_token = "token_afrique.pickle"

    if os.path.exists(filename_token):
        with open(filename_token, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(filename_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # cette partie ne marche pas

    id_utilisateur = session["id"]
    cnx = SGBD.createConnection()
    id_event = 0 #base de donnée
    msg = SGBD.suppression_reserver(cnx, id_event)
    SGBD.closeConnection(cnx, cnx.cursor()) #a rendre plus joli

    ##

    event_id = 0
    list_event_id,list_date,list_heure_debut = prochains_event(date,heure_debut)

    for i in range(len(list_event_id)):
        if date==list_date[i] :
            if heure_debut+':00'==list_heure_debut[i] :
                event_id = list_event_id[i]
                print(event_id)

    service.events().delete(calendarId='primary', eventId=event_id).execute()



def prochains_event(date,heure_debut):
    datetime_event_debut=date+'T'+heure_debut+':00+02:00'
    datetime_event_fin=date+'T'+'19:30'+':00+02:00'
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    filename_token = 'token.pickle'
    if session['europe']==1:
        filename_token = "token_europe.pickle"
    if session["asie"]==1:
        filename_token = "token_asie.pickle"
    if session["amerique"]==1:
        filename_token = "token_amerique.pickle"
    if session["oceanie"]==1:
        filename_token = "token_oceanie.pickle"
    else:
        filename_token = "token_afrique.pickle"

    if os.path.exists(filename_token):
        with open(filename_token, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(filename_token, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # print('Getting the upcoming 20 events')
    events_result = service.events().list(calendarId='primary', timeMin=datetime_event_debut,timeMax=datetime_event_fin,
                                          maxResults=20, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    date = []
    eventId = []
    heure_debut = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        eventId.append(event.get('id'))
        l = start.split("T")
        date.append(l[0])
        heure_debut.append( l[1].split('+')[0])
        # print(start, event['summary'], event.get('id'))
    return eventId,date,heure_debut

if __name__ == '__main__':
    # se_connecter()
    pass
