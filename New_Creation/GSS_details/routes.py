from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  GSS_Ratings, GSS_Shops
from sqlalchemy import func
from ..models import db
import os

GSS_details = Blueprint('GSS_details',__name__,static_folder="static",template_folder="templates")

 

 




#For GSS Shops


# rendering pages for filling the form

@GSS_details.route('/GSS_shop_adding_page')
def GSS_shop_adding_page():
    return render_template('GSSs/GSS_shop_adding_page.html')


# rendering landing pages

@GSS_details.route('/GSS_category_template')
def GSS_category_template():
    return render_template('GSSs/GSS_category_template.html')


@GSS_details.route('/GSS_shop_template',methods=['POST'])
def GSS_shop_template():
    if request.method == 'POST':
        Category = request.form['C']
        if Category:
            return render_template('GSSs/GSS_shop_template.html',Category=Category)
    return 'Something went wrong. Please try again.'
    

@GSS_details.route('/GSS_shop_page',methods=['POST'])
def GSS_shop_page():
    GSSD = GSS_Shops.query.order_by(GSS_Shops.Shop_name).all()

    rating = (
    GSS_Ratings.query
    .with_entities(GSS_Ratings.shop_name, func.round(func.avg(GSS_Ratings.rating), 1).label('Average_rating'))
    .group_by(GSS_Ratings.shop_name)
    .all()
)
    
    if request.method == 'POST':
       Category = request.form['C1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if  GSSD  and Place and District and Category:
         return render_template('GSSs/GSS_shop_page.html',GSSD=GSSD, Place=Place,District=District, rating=rating, Category=Category)
       elif  GSSD  and Place and Category:
         return render_template('GSSs/GSS_shop_page.html',GSSD=GSSD, Place=Place, rating=rating, Category=Category)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@GSS_details.route('/GSS_ratings',methods=['POST'])
def GSS_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = GSS_Ratings(rating=rate,shop_name=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('GSSs/GSS_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@GSS_details.route('/GSS_shop_upload_page',methods=['POST'])
def GSS_shop_upload_page():
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
            file.save(os.path.join('New_Creation/GSS_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = GSS_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info, category=category)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('GSSs/GSS_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@GSS_details.route('/GSS_uploaded_file/<filename>')
def GSS_uploaded_file(filename):
    return send_from_directory('GSS_images', filename)




