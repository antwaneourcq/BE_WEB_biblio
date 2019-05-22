from flask import render_template, request, redirect, url_for
from flask import Flask
import functions, formulaire_manage, bdd


#app.run(debug=True)
app = Flask(__name__, template_folder = 'template') #__init__.py, 'template'
app.config.from_object('config')



@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/webmasters')
def webmasters():
    return render_template('webmasters.html')
    
@app.route('/villes')
def villes():
    return render_template('villes.html')
    
    
@app.route('/message_recu')
def message_recu():
    return render_template('message_recu.html')

@app.route('/nos_regles')
def nos_regles():
    return render_template('nos_regles.html')

@app.route('/nos_services')
def nos_services():
    return render_template('nos_services.html')

@app.route('/se_connecter')
def se_connecter():
    return render_template('se_connecter.html')

@app.route('/se_deconnecter')
def se_deconnecter():
    #en s'inspirant du formulaire
    page_redirect = formulaire_manage.approve_deconnect()
    return redirect(url_for(page_redirect[0], info=page_redirect[1]))

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')
    
@app.route('/cv_CA')
def cv_CA():
    return render_template('cv_CA.html')
    
@app.route('/cv_LD')
def cv_LD():
    return render_template('cv_LD.html')

@app.route('/cv_AL')
def cv_AL():
    return render_template('cv_AL.html')

@app.route('/cv_DL')
def cv_DL():
    return render_template('cv_DL.html')
    
@app.route('/tutoriel_utilisation')
def tutoriel_utilisation():
    return render_template('tutoriel_utilisation.html')


#suite des routes encore non utilisées
@app.route('/tous_les_commentaires')
def tous_les_commentaires():
    msg = functions.msg_info(request.args)  # message d'info pour ajout ou suppression des commentaires
    comments = bdd.get_allCommentData()
    return render_template('tous_les_commentaires.html', data=comments, info=msg)

@app.route('/commentaires')
def comment():
    return render_template('commentaires.html')

@app.route('/reservation_confirmee')
def reservation_confirmee():
    return render_template('reservation_confirmee.html')

@app.route('/formulaire', methods = ['POST', 'GET'])
def formulaire():
    button_submit = request.form["btn_submit"]
    if button_submit == "form_connect": # authentification
        print('formulaire debut connexion')
        page_redirect = formulaire_manage.verif_connect(request.form)
        return redirect(url_for(page_redirect[0], info=page_redirect[1]))

    if button_submit == "form_comment": # ajouter un commentaire
        info_add = formulaire_manage.add_comment(request.form)
        return redirect(url_for("message_recu", info=info_add))

    if button_submit == "del_comment": # suppression d'un commentaire
        msg = formulaire_manage.del_comment(request.form)
        #return functions.switch_msg(msg)
        return None

    if button_submit == "form_reservation":
        info_add = formulaire_manage.add_reservation(request.form)
        return redirect(url_for("reservation_confirmee", info=info_add))
    
    if button_submit == "supp_reservation":
        info_add = formulaire_manage.del_reservation(request.form)
        #return functions.switch_msg(msg)
        return redirect(url_for("index", info=info_add))

@app.route('/calendar_selection', methods = ['POST', 'GET'])
def calendar_selection():
    print('formulaire : ', request.form)
    button_submit = request.form["btn_submit"]
    #if button_submit == "cal_sel":
    info_add = formulaire_manage.calendar_selected(button_submit)
    return redirect(url_for("reservation", info = info_add))

@app.route('/problemes_courants')
def problemes_courants():
    msg = functions.msg_info(request.args)
    problemes = bdd.get_allProbleme()
    return render_template("problemes_courants.html", data = problemes, info=msg)

@app.route('/login')
def login():
    msg = functions.msg_info(request.args) #message d'info pour echec d'authentification
    return render_template('connecter.html',  info=msg)


@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('index'))
