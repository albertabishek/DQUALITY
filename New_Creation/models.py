from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_login import UserMixin,LoginManager


 

db = SQLAlchemy()
login_manager = LoginManager()
 


@login_manager.user_loader
def load_user(user_id):
    return Registrationd.query.get(int(user_id)) 

#Database for food table

class Foods(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    category_1 = db.Column(db.String(length=30), nullable=False) #for veg or non-veg and everything
    category_2 = db.Column(db.String(length=30), nullable=False)
    category_3 = db.Column(db.String(length=30), nullable=False)
    link = db.Column(db.String(length=200), nullable=False, unique=True)
    filename = db.Column(db.String(100), nullable=False)

    
class Fcategory(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.String(length=30), nullable=False)
    category_value = db.Column(db.String(length=30), nullable=False)

class Food_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False )
    F_tag = db.Column(db.String(length=50), nullable=False )  #for food name
    P_tag = db.Column(db.String(length=50), nullable=False )  #for location name
    D_tag = db.Column(db.String(length=50), nullable=False )  
    price = db.Column(db.Integer(), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(100), nullable=False )


class Food_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    food_name =  db.Column(db.String(length=50), nullable=False )
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)
    details = db.Column(db.String(length=50), nullable=False )
   



#Database for Health and Beauty table



class HB_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class HB_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)




#Database for Clothing and Accessories table



class CA_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class CA_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)






#Database for  Technology and Electronics table



class TE_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class TE_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)




#Database for  Books and Entertainment table



class BE_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class BE_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)



#Database for  Home and Furniture table



class HF_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class HF_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)




#Database for  General Grocery Shops table



class GGS_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class GGS_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)



#Database for  General and Specility Stores table



class GSS_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class GSS_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)



#Database for  Shopping Centers table



class SC_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class SC_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)




#Database for  Services and Miscellaneous centers table


class SM_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class SM_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)




#Database for  Tourist Attractions table


class TA_Shops(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=50), nullable=False ) 
    category =   db.Column(db.String(length=50), nullable=False )  
    P_tag = db.Column(db.String(length=50), nullable=False )  
    D_tag = db.Column(db.String(length=50), nullable=False ) 
    contact_Info = db.Column(db.String(length=50), nullable=False )
    Quality = db.Column(db.String(10), nullable=False )
    location_text = db.Column(db.String(100), nullable=False )
    location_link = db.Column(db.String(200), nullable=False )
    filename = db.Column(db.String(30), nullable=False )


class TA_Ratings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    shop_name =  db.Column(db.String(length=50), nullable=False )
    rating = db.Column(db.Float(), nullable=False)



#Database for the offers and discount

class offers_and_discount(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Shop_name = db.Column(db.String(length=30), nullable=False)
    starting_date = db.Column(db.String(length=12), nullable=False)
    ending_date = db.Column(db.String(length=12), nullable=False)
    discount = db.Column(db.String(length=30), nullable=False)

#Database for login system
 

class Registrationd(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False)
    email = db.Column(db.String(length=50),nullable=False)
    password = db.Column(db.String(length=30), nullable=False)

    def __repr__(self):
        return f"Registrationd('{self.username}', '{self.email}')"

class Logind(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(length=50), nullable=False)
    date_logged = db.Column(db.DateTime, nullable=False, default=datetime.now)

