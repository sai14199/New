import pymongo

client = pymongo.MongoClient("mongodb://sai14199:sai@ac-f2c5ytb-shard-00-00.lgq36z8.mongodb.net:27017,ac-f2c5ytb-shard-00-01.lgq36z8.mongodb.net:27017,ac-f2c5ytb-shard-00-02.lgq36z8.mongodb.net:27017/?ssl=true&replicaSet=atlas-5aseld-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print(db)
d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )



