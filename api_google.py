from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from flask import session
import SGBD

# Alcove Europe - Toulouse - 1 - Grise
id_objet_reservable = 1

def get_id_utilisateur(mail):
    #à coder (voir si on garde le mail)
    #SGBD.createConnection()
    id_utilisateur = 666
    #SGBD.closeConnection()
    return id_utilisateur

#id_utilisateur = get_id_utilisateur()

""""gerer les ID des events + gerer le fait de devoir se co à chaque fois + faire un if pour ne pas ajouter un event 
s'il y en a deja un de prevu à cette heure + ne pas pouvoir reserver hors des horaires d'ouverture + creer une fonction duree
+ faire une fonction qui trouve l'id de l'utilisateur en cours"""

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def se_connecter():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)


def creer_event(date, heure_debut, heure_fin, promo, nb_pers):
    # format 'AAAA-MM-JJ' date
    # format 'HH-MM-SS' heure_d
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': 'Occupé',
        'location': '',
        'description': promo + str(nb_pers),
        'start': {
            'dateTime': date + 'T' + heure_debut + ':00+02:00',
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': date + 'T' + heure_fin + ':00+02:00',
            'timeZone': 'Europe/Paris',

        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    ### voir si on garde le mail 
    mail = 'test@h.fr'
    #id_utilisateur = get_id_utilisateur(mail)
    id_utilisateur = session["id"]
    print("id: ", session['id'], session['mail'])
    ###partie base de donnée
    cnx = SGBD.createConnection()
    msg = SGBD.ajout_reserver(cnx, 2, date, 120, heure_debut, id_objet_reservable, id_utilisateur, nb_pers)
    SGBD.closeConnection(cnx, cnx.cursor()) #a rendre plus joli
    return msg


def supprimer_event(date, heure_debut, promo):
    # format 'AAAA-MM-JJ' date
    # format 'HH-MM-SS' heure_d
    heure_fin = heure_debut
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    event = service.events().insert(calendarId='primary', body=event).execute()
    event_id = get_event_id(id_utilisateur, heure_debut, date)
    service.events().delete(calendarId = 'primary', eventId=event_id).execute()

def prochains_event():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], event.get('id'))


if __name__ == '__main__':
    # supprimer_event(0,0)
    prochains_event()
