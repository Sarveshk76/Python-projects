from pymongo import MongoClient
client = MongoClient()
db = client['Students']
print("Database Created...")
#db.create_collection('MCA')
#db.create_collection('MBA')
print("Collections Created....")
for i in db.list_collection_names():
    print(i)
coll1 = db['MCA']
coll2 = db['MBA']
doc1 = ([{"Name":"Sarvesh","Address":"Ramdas colony","Percentage":"70","City":"Nashik","Specialization":"Java"},
        {"Name":"Rahul","Address":"Akurdi","Percentage":"65","City":"Pune","Specialization":"AIT"},
        {"Name":"Suresh","Address":"Gangapur Road","Percentage":"68","City":"Nashik","Specialization":"Python"}])
doc2 = ([{"Name":"Suraj","Address":"Ramdas colony","Percentage":"70","City":"Nashik","Specialization":"Economics"},
        {"Name":"Abhijit","Address":"Akurdi","Percentage":"65","City":"Pune","Specialization":"Law"},
        {"Name":"Navin","Address":"Gangapur Road","Percentage":"68","City":"Nashik","Specialization":"Social sciences"}])
#Insert documents
res1 = coll1.insert_many(doc1)
res2 = coll2.insert_many(doc2)
print("Data inserted.....")
print(res1.inserted_ids)
print(res2.inserted_ids)
#Update documents
coll1.update_one({"Name":"Sarvesh"},{"$set":{"City":"Mumbai"}})
print("Collection-1 is updated.")
print("Documents in the collection after update operation: ")
for i in coll1.find():
   print(i)
#Drop the collection
coll2.drop()
print("After dropping collection-2")
for i in db.list_collection_names():
    print(i)