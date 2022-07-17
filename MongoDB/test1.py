import pymongo

#client = pymongo.MongoClient("mongodb+srv://kuttral99:kuttralanathan@cluster0.f6s4s.mongodb.net/?retryWrites=true&w=majority")
#db = client.test

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Kuttralanathan",
    "email" : "kk99@gmail.com",
    "surname" : "K"
}

db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)
