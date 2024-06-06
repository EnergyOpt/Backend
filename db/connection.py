from pymongo import MongoClient

try:

    client = MongoClient(f"mongodb+srv://godsonezekiel31:godson14@cluster0.frnmyqg.mongodb.net/?retryWrites=true&w=majority")
    # client = MongoClient(f"mongodb://localhost:27017")

    db = client.EnergyOpt

    print("Successfully connected to MongoDb")
except Exception as e:
    print("Connection to MongoDb failed:", e)