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


@app.route('/commentaires')
def comment():
    msg = functions.msg_info(request.args)  # message d'info pour ajout ou suppression des commentaires
    comments = bdd.get_allCommentData()
    return render_template('commentaires.html', data=comments, info=msg)


@app.route('/formulaire',methods = ['POST', 'GET'])
def formulaire():
    button_submit = request.form["btn_submit"]

    if button_submit == "form_connect": # authentification
        page_redirect = formulaire_manage.verif_connect(request.form)
        return redirect(url_for(page_redirect[0], info=page_redirect[1]))

    if button_submit == "form_comment": # ajouter un commentaire
        info_add = formulaire_manage.add_comment(request.form)
        return redirect(url_for("comment", info=info_add))

    if button_submit == "del_comment": # suppression d'un commentaire
        msg = formulaire_manage.del_comment(request.form)
        return functions.switch_msg(msg)


@app.route('/login')
def login():
    msg = functions.msg_info(request.args) #message d'info pour echec d'authentification
    return render_template('connecter.html',  info=msg)


@app.route('/logout')
def logout():
   session.clear()
   return redirect(url_for('index'))
