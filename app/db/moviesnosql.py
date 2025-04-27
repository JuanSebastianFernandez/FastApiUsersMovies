from pymongo import MongoClient

#Local
# db_client = MongoClient().local

#Remote
db_client = MongoClient("mongodb+srv://sebastianOca:ServerOCA@oca.efgnz.mongodb.net/?retryWrites=true&w=majority&appName=oca").test