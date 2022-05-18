import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="usuario",
  password="",
  database="bancodedados",
  # port="3306"
  # caso necessite usar um banco de dados web, será necessário colocar a porta, basta retirar o comentário da linha 7. Lembrando que a porta padrão é 3306, mas existem servidores que alteram, então antes de colocar a porta, verifica qual é a porta do seu servidor.
)
mycursor = mydb.cursor()
