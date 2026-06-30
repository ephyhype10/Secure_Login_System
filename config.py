class Config:
    SECRET_KEY = "ChangeThisToARandomSecretKey123!"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ephy2906@localhost/secure_login"

    SQLALCHEMY_TRACK_MODIFICATIONS = False