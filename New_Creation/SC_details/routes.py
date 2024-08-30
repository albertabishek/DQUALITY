from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  SC_Ratings, SC_Shops
from sqlalchemy import func
from ..models import db
import os

SC_details = Blueprint('SC_details',__name__,static_folder="static",template_folder="templates")

 

 




#For SC Shops


# rendering pages for filling the form

@SC_details.route('/SC_shop_adding_page')
def SC_shop_adding_page():
    return render_template('SCs/SC_shop_adding_page.html')


# rendering landing pages

@SC_details.route('/SC_category_template')
def SC_category_template():
    return render_template('SCs/SC_category_template.html')


@SC_details.route('/SC_shop_template',methods=['POST'])
def SC_shop_template():
    if request.method == 'POST':
        Category = request.form['C']
        if Category:
            return render_template('SCs/SC_shop_template.html',Category=Category)
    return 'Something went wrong. Please try again.'
    

@SC_details.route('/SC_shop_page',methods=['POST'])
def SC_shop_page():
    SCD = SC_Shops.query.order_by(SC_Shops.Shop_name).all()

    rating = (
    SC_Ratings.query
    .with_entities(SC_Ratings.shop_name, func.round(func.avg(SC_Ratings.rating), 1).label('Average_rating'))
    .group_by(SC_Ratings.shop_name)
    .all()
)
    
    if request.method == 'POST':
       Category = request.form['C1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if  SCD  and Place and District and Category:
         return render_template('SCs/SC_shop_page.html',SCD=SCD, Place=Place,District=District, rating=rating, Category=Category)
       elif  SCD  and Place and Category:
         return render_template('SCs/SC_shop_page.html',SCD=SCD, Place=Place, rating=rating, Category=Category)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@SC_details.route('/SC_ratings',methods=['POST'])
def SC_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = SC_Ratings(rating=rate,shop_name=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('SCs/SC_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@SC_details.route('/SC_shop_upload_page',methods=['POST'])
def SC_shop_upload_page():
    if request.method == 'POST':
        file = request.files['file']
        shopname = request.form['shop_name']  # Retrieve the name from the form
        tag2 = request.form['T2']
        tag3 = request.form['T3']
        category = request.form['C1']
        contact_info = request.form['C_info']
        Llink = request.form['location_link']
        Lname = request.form['location_name']
        quality = request.form['quality']
        

        if file and shopname and Llink  and Lname  and tag2 and tag3 and contact_info and category:
            filename = file.filename
            file.save(os.path.join('New_Creation/SC_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = SC_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info, category=category)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('SCs/SC_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@SC_details.route('/SC_uploaded_file/<filename>')
def SC_uploaded_file(filename):
    return send_from_directory('SC_images', filename)




