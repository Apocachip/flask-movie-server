import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cztqqfotbirp.ap-northeast-2.rds.amazonaws.com',
        database = 'movie_recommend_app_db',
        user = 'movie_user',
        password= 'movie1234'
    )
    return connection