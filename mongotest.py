from pymongo import MongoClient
client = MongoClient('mongodb+srv://rahulgowda4785:3t0KDthxRyiDrg85@autspot.u42dncc.mongodb.net/?retryWrites=true&w=majority')
dbname = client['Autism']
collection_name = dbname["Userdata"]

myquery = { "userid": "01","emotion":"happy"}
q_results = collection_name.find(myquery)
results = list(q_results)

print(results[0]["solution"])
