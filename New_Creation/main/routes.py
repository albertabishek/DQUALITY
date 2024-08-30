from flask import render_template, Blueprint,redirect,url_for,flash,request
from ..forms import RegistrationForm,LoginForm
from New_Creation import bcrypt,db
from ..models import Registrationd,Logind,offers_and_discount
from flask_login import login_user,current_user,logout_user,login_required

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/start_page')
def starting_page():
    return render_template('starting_page.html')



@main.route('/home')
@main.route('/home_page')
@login_required
def home_page():
    return render_template('home_page.html')



@main.route('/search',methods=['POST'])
def search():
    offer = offers_and_discount.query
    if request.method == "POST":
        search = request.form['search']
        if search:
            offers = offer.filter(offers_and_discount.Shop_name.like('%' + search + '%')).all()
            return render_template('o_and_d.html', offers=offers)
    return 'Something went wrong. Please try again.'



@main.route('/o_and_d')
def o_and_d():
    offers = offers_and_discount.query.all()
    return render_template('o_and_d.html',offers=offers)



@main.route('/edit_offer/<int:id>', methods=['GET','POST'])
def edit_offer(id):
    offer = offers_and_discount.query.get_or_404(id)
    return render_template('edit_offer.html',id=id,offer=offer)



@main.route('/edit_offer_page/<int:id>', methods=['GET','POST'])
def edit_offer_page(id):
    offer = offers_and_discount.query.get_or_404(id)
    if request.method == "POST":
        offer.Shop_name = request.form['shop_name']
        offer.starting_date = request.form['S1']
        offer.ending_date = request.form['E1']
        offer.discount = request.form['D1']
        #update to database
        db.session.add(offer)
        db.session.commit()
        flash("Offer Has Been Updated!",category='success')
        return redirect(url_for('main.o_and_d'))
    return "Something was wrong!"
     
     
@main.route('/delete_offer/<int:id>', methods=['GET','POST'])
def delete_offer(id):
    offer = offers_and_discount.query.get_or_404(id)

    try:
        db.session.delete(offer)
        db.session.commit()

        flash("The offer was deleted successfully",category='success')

        return redirect(url_for('main.o_and_d'))
    except:
        flash("Oop's operation was failed !",category='danger')
        return redirect(url_for('main.o_and_d'))



@main.route('/user_forms_page')
def user_forms_page():
    return render_template('user_forms_page.html')

@main.route('/admin_forms_page')
def admin_forms_page():
    return render_template('admin_forms_page.html')

@main.route('/offer_adding_page')
def offer_adding_page():
    return render_template('offer_adding_page.html')

@main.route('/offer_upload_page',methods=['POST'])
def offer_upload_page():
    if request.method == 'POST':
        shop_name = request.form['shop_name']
        starting_date = request.form['S1']
        ending_date = request.form['E1']
        discount = request.form['D1']
 
        if shop_name and starting_date and ending_date and discount :
                   
            # Create a new record in the database with both name and filename
            new_file = offers_and_discount(Shop_name = shop_name, starting_date=starting_date, ending_date=ending_date, discount=discount)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('offer_adding_page.html')
    
    return 'Something went wrong. Please try again.'


@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
       return redirect(url_for('main.home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Registrationd(username=form.username.data, email=form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html',form=form)


 

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('main.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Registrationd.query.filter_by(email=form.email.data).first()
        if user == None:
            flash('Login Unsuccessful. Please create an account','danger')
        elif user.email == "albertadmin@gmail.com" and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash('Logined successfully','success')
            return redirect(url_for('main.admin_forms_page'))
        elif user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            log = Logind(email= form.email.data )
            db.session.add(log)
            db.session.commit()
            flash('Logined successfully','success')
            return redirect(url_for('main.home_page'))
        else:
            flash('Login Unsuccessful. Please check email and password','danger')
         
    return render_template('login.html', form=form)



@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))


 