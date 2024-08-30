from flask import render_template,request,send_from_directory,Blueprint
from sqlalchemy import func
from ..models import Foods,Food_Shops,Food_Ratings,Fcategory
from New_Creation import db 
import os

Food_details = Blueprint('Food_details', __name__,static_folder="static",template_folder="templates")


 



# rendering pages for filling the form

@Food_details.route('/food_adding_page')
def food_adding_page():
    return render_template('Foods/food_adding_page.html')

@Food_details.route('/food_shop_adding_page')
def food_shop_adding_page():
    return render_template('Foods/food_shop_adding_page.html')


@Food_details.route('/food_category_adding_page')
def food_category_adding_page():
     return render_template('Foods/food_category_adding_page.html')

# rendering landing pages



@Food_details.route('/foods_template')
def foods_template():
    data = Fcategory.query.order_by(Fcategory.category).all()
    return render_template('Foods/foods_template.html',data=data)


@Food_details.route('/foods_page',methods=['POST'])
def foods_page():
    files = Foods.query.order_by(Foods.name).all()
    if request.method == 'POST':
        fo = request.form['a']

        if fo == 'f1':
           C1 = request.form['C1']
           if C1 :
              return render_template('Foods/foods_page.html',files=files,C1=C1)
        elif fo == 'f2':
           C2 = request.form['C2']
           if C2 :
              return render_template('Foods/foods_page.html',files=files,C2=C2)  
      
    return 'Something went wrong. Please try again.'


@Food_details.route('/food_shop_template',methods=['POST'])
def food_shop_template():
    if request.method == 'POST':
        Flink = request.form['Fname']
        if Flink:
           return render_template('Foods/food_shop_template.html',Flink=Flink)
    return 'Something went wrong. Please try again.'


@Food_details.route('/food_shops_page',methods=['POST'])
def food_shops_page():
    shopies = Food_Shops.query.order_by(Food_Shops.Shop_name).all()

    rating = (
    Food_Ratings.query
    .with_entities(Food_Ratings.details,Food_Ratings.food_name,Food_Ratings.shop_name, func.round(func.avg(Food_Ratings.rating), 1).label('Average_rating'))
    .group_by(Food_Ratings.details)
    .all()
)

    if request.method == 'POST':
       Flink = request.form['Flink']
       Price = request.form['PR1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if Flink and shopies and Price and Place and District:
         return render_template('Foods/food_shops_page.html',shopies=shopies,Flink=Flink,Price=int(Price),Place=Place,District=District,rating=rating)
       elif Flink and shopies and Price and Place:
         return render_template('Foods/food_shops_page.html',shopies=shopies,Flink=Flink,Price=int(Price),Place=Place,rating=rating)

    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@Food_details.route('/food_ratings', methods=['POST'])
def food_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        Sname = request.form['Sname']
        sname = request.form['sname']
        fname = request.form['fname']
        if rate and Sname and sname and fname:
            new_file = Food_Ratings(rating=rate, details=Sname, shop_name=sname,food_name=fname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('Foods/food_rating_success.html')
        
    return 'Something went wrong. Please try  again.'  


@Food_details.route('/food_shop_upload_page',methods=['POST'])
def food_shop_upload_page():
    if request.method == 'POST':
        file = request.files['file']
        shopname = request.form['shop_name']  # Retrieve the name from the form
        tag1 = request.form['T1']
        tag2 = request.form['T2']
        tag3 = request.form['T3']
        contact_info = request.form['C_info']
        Llink = request.form['location_link']
        Lname = request.form['location_name']
        quality = request.form['quality']
        price = request.form['price']

        if file and shopname and Llink and price and Lname  and tag1 and tag2 and tag3 and contact_info :
            filename = file.filename
            file.save(os.path.join('New_Creation/Foods_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = Food_Shops(Shop_name = shopname , price = price, Quality=quality, location_text=Lname, location_link=Llink, filename=filename, F_tag=tag1, P_tag=tag2, D_tag=tag3, contact_Info=contact_info)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Foods/food_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@Food_details.route('/food_upload_page',methods=['POST'])
def food_upload_page():
    if request.method == 'POST':
        name = request.form['name1']  # Retrieve the name from the form
        Category1 = request.form['C1']
        Category2 = request.form['C2']
        Category3 = request.form['C3']
        link = request.form['links']
        file = request.files['file']
       
        if file and name and link and Category1 and Category2 and Category3:
            filename = file.filename
            file.save(os.path.join('New_Creation/Foods_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = Foods(name=name, link=link, filename=filename, category_1=Category1, category_2=Category2, category_3=Category3)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Foods/food_adding_page.html')
    
    return 'Something went wrong. Please try again.'


@Food_details.route('/food_category_upload_page',methods=['POST'])
def food_category_upload_page():
    if request.method == 'POST':
        
        Category = request.form['C1']
        Category_value = request.form['C2']
       
        if Category_value and Category:
            new_file = Fcategory( category=Category,category_value=Category_value)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Foods/food_category_adding_page.html')
    
    return 'Something went wrong. Please try again.'


@Food_details.route('/F_uploaded_file/<filename>',methods=['POST','GET'])
def F_uploaded_file(filename):
    return send_from_directory('Foods_images', filename)

