import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="159753", database="mydb")

if (mydb):
    print("connection Successful")
else:
    print("Connection Failed")

mycursor = mydb.cursor()
columns = ""


def selectTest(name):
    mycursor.execute("SELECT * FROM {name}".format(name=name))
    for x in mycursor:
        return (x)


def getNoticiasCirculo():
    mycursor.execute(
        "SELECT a.idUpdates, a.updNome, a.updDataInicio, a.imagem FROM updates a INNER JOIN importancias b ON updIDImp = idImportancias WHERE b.idImportancias = 1 ORDER BY updDataInicio LIMIT 9;")
    for x in mycursor:
        return (x)


def getNoticiasRecentes():
    mycursor.execute(
        "SELECT idUpdates, updNome, updDescricao, updDataInicio, imagem FROM updates ORDER BY updDataInicio LIMIT 9;")
    for x in mycursor:
        return (x)


def getTopicos():
    mycursor.execute("SELECT catNome FROM categorias");
    for x in mycursor:
        return {"topico": x}
