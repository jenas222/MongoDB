import pymongo


client = pymongo.MongoClient("mongodb+srv://jenas222:3zivCobe7wbI014W@clusterskola.6w1cj5i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db.drop_collection("people")
result = db.people.insert_many([{"Jmeno": "Jakub", "Mazlicci": ["pes", "kocour"]},
                                {"Jmeno": "David", "Mazlicci": []},
                                {"Jmeno": "Josef", "Mazlicci": ["pes"]},
                                {"Jmeno": "Karel", "Mazlicci": ["pes", "kocka", "kocour"]}])
collection = db.get_collection("people")
querry = {}
while True:
    val = input("Zadej hodnotu: ")
    
    if val == "list":
        output = collection.find(querry)
        for zaznam in output:
            print(zaznam)
    if val == "q":
        break
    if val == "add":
        jmeno = input("Zadej jmeno: ")
        mazlicci = []
        while True:
            mazlicek = input ("Zadej mazlicka: ")            
            if mazlicek == "q":                
                break
            mazlicci.append(mazlicek)
        dictionary = {"Jmeno": jmeno, "Mazlicci": mazlicci}
        collection.insert_one(dictionary)