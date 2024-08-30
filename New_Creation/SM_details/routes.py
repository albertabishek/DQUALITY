from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  SM_Ratings, SM_Shops
from sqlalchemy import func
from ..models import db
import os

SM_details = Blueprint('SM_details',__name__,static_folder="static",template_folder="templates")

 

 




#For SM Shops


# rendering pages for filling the form

@SM_details.route('/SM_shop_adding_page')
def SM_shop_adding_page():
    return render_template('SMs/SM_shop_adding_page.html')


# rendering landing pages

@SM_details.route('/SM_category_template')
def SM_category_template():
    return render_template('SMs/SM_category_template.html')


@SM_details.route('/SM_shop_template',methods=['POST'])
def SM_shop_template():
    if request.method == 'POST':
        Category = request.form['C']
        if Category:
            return render_template('SMs/SM_shop_template.html',Category=Category)
    return 'Something went wrong. Please try again.'
    

@SM_details.route('/SM_shop_page',methods=['POST'])
def SM_shop_page():
    SMD = SM_Shops.query.order_by(SM_Shops.Shop_name).all()

    rating = (
    SM_Ratings.query
    .with_entities(SM_Ratings.shop_name, func.round(func.avg(SM_Ratings.rating), 1).label('Average_rating'))
    .group_by(SM_Ratings.shop_name)
    .all()
)
    
    if request.method == 'POST':
       Category = request.form['C1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if  SMD  and Place and District and Category:
         return render_template('SMs/SM_shop_page.html',SMD=SMD, Place=Place,District=District, rating=rating, Category=Category)
       elif  SMD  and Place and Category:
         return render_template('SMs/SM_shop_page.html',SMD=SMD, Place=Place, rating=rating, Category=Category)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@SM_details.route('/SM_ratings',methods=['POST'])
def SM_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = SM_Ratings(rating=rate,shop_name=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('SMs/SM_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@SM_details.route('/SM_shop_upload_page',methods=['POST'])
def SM_shop_upload_page():
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
            file.save(os.path.join('New_Creation/SM_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = SM_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info, category=category)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('SMs/SM_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@SM_details.route('/SM_uploaded_file/<filename>')
def SM_uploaded_file(filename):
    return send_from_directory('SM_images', filename)




