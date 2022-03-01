import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = {"name": "John", "address": "Highway 37"}
x = mycol.insert_one(mydict)
print(x.inserted_id)
mylist = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)
# also works even if we didn't assign ids ourselves
x = mycol.find_one()
# finds the first occurence
print(x)
for x in mycol.find():
    print(x)
# finds all occurences
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)
# returns only some fields, 0 means to exclude
myquery = {"address": "Park Lane 38"}
mydoc = {mycol.find(myquery)}
for x in mydoc:
    print(x)
# filters the result
myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
# advance query search where it returns any occurence in address greater than S
myquery = {"address": {"regex": "^S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
# Same as above just using regex or regular expression
mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)
# sorting the results
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)
# sorting the results in descending order
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)
# updates collection
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
# updates all documents where the address starts with the letter "S"
myresult = mycol.find().limit(5)
for x in myresult:
    print(x)
# limits the occurences to 5
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)
myquery = {"address": {"$regex": "^S"}}
# deletes one
x = mycol.delete_many(myquery)
print(x.deleted_count, "documents deleted.")
# deletes multiple
x = mycol.delete_many({})
print(x.deleted_count, "documents deleted.")
# deletes all
mycol.drop()
# deletes whole database table and returns true if successful
