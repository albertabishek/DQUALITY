from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  TE_Ratings, TE_Shops
from sqlalchemy import func
from ..models import db
import os

TE_details = Blueprint('TE_details',__name__,static_folder="static",template_folder="templates")

 

 




#For TE Shops


# rendering pages for filling the form

@TE_details.route('/TE_shop_adding_page')
def TE_shop_adding_page():
    return render_template('TEs/TE_shop_adding_page.html')


# rendering landing pages

@TE_details.route('/TE_category_template')
def TE_category_template():
    return render_template('TEs/TE_category_template.html')


@TE_details.route('/TE_shop_template',methods=['POST'])
def TE_shop_template():
    if request.method == 'POST':
        Category = request.form['C']
        if Category:
            return render_template('TEs/TE_shop_template.html',Category=Category)
    return 'Something went wrong. Please try again.'
    

@TE_details.route('/TE_shop_page',methods=['POST'])
def TE_shop_page():
    TED = TE_Shops.query.order_by(TE_Shops.Shop_name).all()

    rating = (
    TE_Ratings.query
    .with_entities(TE_Ratings.shop_name, func.round(func.avg(TE_Ratings.rating), 1).label('Average_rating'))
    .group_by(TE_Ratings.shop_name)
    .all()
)
    
    if request.method == 'POST':
       Category = request.form['C1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if  TED  and Place and District and Category:
         return render_template('TEs/TE_shop_page.html',TED=TED, Place=Place,District=District, rating=rating, Category=Category)
       elif  TED  and Place and Category:
         return render_template('TEs/TE_shop_page.html',TED=TED, Place=Place, rating=rating, Category=Category)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@TE_details.route('/TE_ratings',methods=['POST'])
def TE_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = TE_Ratings(rating=rate,shop_name=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('TEs/TE_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@TE_details.route('/TE_shop_upload_page',methods=['POST'])
def TE_shop_upload_page():
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
            file.save(os.path.join('New_Creation/TE_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = TE_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info, category=category)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('TEs/TE_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@TE_details.route('/TE_uploaded_file/<filename>')
def TE_uploaded_file(filename):
    return send_from_directory('TE_images', filename)




