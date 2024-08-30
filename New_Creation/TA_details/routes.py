from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  TA_Ratings, TA_Shops
from sqlalchemy import func
from ..models import db
import os

TA_details = Blueprint('TA_details',__name__,static_folder="static",template_folder="templates")

 

 




#For TA Shops


# rendering pages for filling the form

@TA_details.route('/TA_shop_adding_page')
def TA_shop_adding_page():
    return render_template('TAs/TA_shop_adding_page.html')


# rendering landing pages

@TA_details.route('/TA_category_template')
def TA_category_template():
    return render_template('TAs/TA_category_template.html')


@TA_details.route('/TA_shop_template',methods=['POST'])
def TA_shop_template():
    if request.method == 'POST':
        Category = request.form['C']
        if Category:
            return render_template('TAs/TA_shop_template.html',Category=Category)
    return 'Something went wrong. Please try again.'
    

@TA_details.route('/TA_shop_page',methods=['POST'])
def TA_shop_page():
    TAD = TA_Shops.query.order_by(TA_Shops.Shop_name).all()

    rating = (
    TA_Ratings.query
    .with_entities(TA_Ratings.shop_name, func.round(func.avg(TA_Ratings.rating), 1).label('Average_rating'))
    .group_by(TA_Ratings.shop_name)
    .all()
)
    
    if request.method == 'POST':
       Category = request.form['C1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if  TAD  and Place and District and Category:
         return render_template('TAs/TA_shop_page.html',TAD=TAD, Place=Place,District=District, rating=rating, Category=Category)
       elif  TAD  and Place and Category:
         return render_template('TAs/TA_shop_page.html',TAD=TAD, Place=Place, rating=rating, Category=Category)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@TA_details.route('/TA_ratings',methods=['POST'])
def TA_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = TA_Ratings(rating=rate,shop_name=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('TAs/TA_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@TA_details.route('/TA_shop_upload_page',methods=['POST'])
def TA_shop_upload_page():
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
            file.save(os.path.join('New_Creation/TA_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = TA_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info, category=category)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('TAs/TA_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@TA_details.route('/TA_uploaded_file/<filename>')
def TA_uploaded_file(filename):
    return send_from_directory('TA_images', filename)




