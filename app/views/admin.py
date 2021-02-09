from  flask import Blueprint,render_template

ad = Blueprint('ad',__name__,url_prefix='/admin')

@ad.route('/')
def admin():
    return render_template('index.html')
