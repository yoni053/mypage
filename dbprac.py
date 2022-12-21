from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.mhjf0sv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

 # 저장 
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 
db.users.delete_one({'name':'bobby'})
