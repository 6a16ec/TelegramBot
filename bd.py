import mysql.connector
import token

cnx = mysql.connector.connect(user='6a16ec', password=token.password,
                              host='6a16ec.mysql.pythonanywhere-services.com',
                              database='6a16ec$TelegramTaskManager')
cnx.close()