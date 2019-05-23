def switch_msg(info):
    switcher = {
        'insComment_fail': "Problème enregistrement de commentaire",
        'insComment_success': "Le commentaire a bien été enregistré",
        'delComment_fail': "Problème suppression de commentaire",
        'delComment_success': "Le commentaire a bien été supprimé",
        'auth_success': "Authentification réussie",
        'auth_fail': "Echec d'authentification",
        "del_all_comment_success": "Succès de suppression des commentaires",
        "del_all_comment_failed": "Echec de suppression des commentaires"
    }
    return switcher[info]

# si le message d'info est passé en paramètre, on renvoie le texte à afficher
def msg_info(dataRequest):
    msg = ""
    if 'info' in dataRequest:
        info = dataRequest.get('info')
        msg = switch_msg(info)
    return msg