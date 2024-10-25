from app.config.database import Base, engine, SessionLocal
from app.models import address, cart_item, category, order, product, review, user

Base.metadata.create_all(engine)
session = SessionLocal()

users = [
    user.User(username="admin", password="$2b$12$IWAZ.Iz9.z.n5Bz25y6j2O5P7YiT.S.QGZql.aJO.pBcVfVkncqi6", name="Admin", role="ADMIN"),
    user.User(username="john_doe", password="$2b$12$xITtT2X5.VKxvWplwsbMguWpVIv3Nzs8nwBWjIaDm.oDxdghMl4Q2", name="John Doe", role="USER"),
    user.User(username="jane_smith", password="$2b$12$xITtT2X5.VKxvWplwsbMguWpVIv3Nzs8nwBWjIaDm.oDxdghMl4Q2", name="Jane Smith", role="USER"),
    user.User(username="alice_jones", password="$2b$12$xITtT2X5.VKxvWplwsbMguWpVIv3Nzs8nwBWjIaDm.oDxdghMl4Q2", name="Alice Jones", role="USER"),
]
session.add_all(users)
session.flush()

addresses = [
    address.Address(user_id=1, building="Building A", street="123 Main St", district="Downtown", city="Springfield", governorate="Illinois", country="USA", phone="123-456-7890"),
    address.Address(user_id=2, building="Building B", street="456 Elm St", district="Uptown", city="Springfield", governorate="Illinois", country="USA", phone="234-567-8901"),
    address.Address(user_id=3, building="Building C", street="789 Maple St", district="Midtown", city="Springfield", governorate="Illinois", country="USA", phone="345-678-9012"),
    address.Address(user_id=4, building="Building D", street="101 Oak St", district="Suburb", city="Springfield", governorate="Illinois", country="USA", phone="456-789-0123"),
]
session.add_all(addresses)
session.flush()

categories = [
    category.Category(name="Electronics", description="Devices and gadgets"),
    category.Category(name="Clothing", description="Apparel for men and women"),
    category.Category(parent_id=1, name="Mobile Phones", description="Smartphones and accessories"),
    category.Category(parent_id=1, name="Laptops", description="Portable computers"),
    category.Category(parent_id=2, name="Men's Wear", description="Clothing for men"),
    category.Category(parent_id=2, name="Women's Wear", description="Clothing for women"),
]
session.add_all(categories)
session.flush()

products = [
    product.Product(category_id=4, name="HP Laptop", description="A powerful laptop suitable for professional use.", stock=50, price=1299, discount=0),
    product.Product(category_id=3, name="iPhone", description="Latest model of Apple's smartphone.", stock=200, price=999, discount=0),
    product.Product(category_id=3, name="Samsung Galaxy", description="Flagship smartphone from Samsung.", stock=150, price=799, discount=0),
    product.Product(category_id=5, name="Men's Jacket", description="Stylish jacket for men.", stock=30, price=89, discount=0),
    product.Product(category_id=6, name="Women's Dress", description="Elegant dress for various occasions.", stock=20, price=79, discount=0),
    product.Product(category_id=4, name="Gaming Laptop", description="High-performance laptop for gamers.", stock=25, price=1499, discount=0),
]
session.add_all(products)
session.flush()

reviews = [
    review.Review(user_id=2, product_id=1, rating=5, title='Fantastic Laptop', comment='The HP Laptop is a beast for work!'),
    review.Review(user_id=3, product_id=2, rating=4, title='Great iPhone', comment='Love the camera quality on the iPhone!'),
    review.Review(user_id=4, product_id=3, rating=5, title='Excellent Smartphone', comment='The Samsung Galaxy has amazing features!'),
    review.Review(user_id=2, product_id=4, rating=4, title='Stylish Jacket', comment='Very comfortable and looks great!'),
    review.Review(user_id=3, product_id=5, rating=3, title='Nice Dress', comment='The dress is beautiful but slightly tight.'),
    review.Review(user_id=2, product_id=6, rating=5, title='Awesome Gaming Laptop', comment='Perfect for all my gaming needs!'),
]
session.add_all(reviews)
session.commit()
session.close()
