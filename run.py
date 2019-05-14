from views import app

'''
@app.route('/')
def index():
    d = s.read()
    return d
'''
if __name__ == '__main__':
    app.run(host="localhost", port=80) #--> loacalhost/static/index.html si inex devient un template le sortir de static et le mettre dans template et donc enlever le '/static'
