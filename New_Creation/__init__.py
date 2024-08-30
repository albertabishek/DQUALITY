from flask import Flask
from flask_bcrypt import Bcrypt
 
from  .models import db ,login_manager
from .forms import RegistrationForm,LoginForm
 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '86dbba64fcc01c47427a65d4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
 
 
app.app_context().push()
 



with app.app_context():
    db.create_all()

login_manager.init_app(app)
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'




from New_Creation.Food_details.routes import Food_details
from New_Creation.main.routes import main
from New_Creation.HB_details.routes  import HB_details
from New_Creation.CA_details.routes import CA_details
from New_Creation.TE_details.routes import TE_details
from New_Creation.BE_details.routes import BE_details
from New_Creation.HF_details.routes import HF_details
from New_Creation.GGS_details.routes import GGS_details
from New_Creation.GSS_details.routes import GSS_details
from New_Creation.SC_details.routes import SC_details
from New_Creation.SM_details.routes import SM_details
from New_Creation.TA_details.routes import TA_details


app.register_blueprint(Food_details)
app.register_blueprint(main)
app.register_blueprint(HB_details)
app.register_blueprint(CA_details)
app.register_blueprint(TE_details)
app.register_blueprint(BE_details)
app.register_blueprint(HF_details)
app.register_blueprint(GGS_details)
app.register_blueprint(GSS_details)
app.register_blueprint(SC_details)
app.register_blueprint(SM_details)
app.register_blueprint(TA_details)
 
 
 