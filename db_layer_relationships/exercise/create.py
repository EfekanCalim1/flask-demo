from app import db, Orders, Customers, Products

db.create_all()

ben = Customers(name= 'Ben', email= 'ben@ben.com')

phone = Products(name='iPhone 12 Pro', price=1049.00)

db.session.add(ben)
db.session.add(phone)
db.session.commit()

order_phone = Orders(product_id=phone.id, customer_id=ben.id)

db.session.add(order_phone)
db.session.commit()
