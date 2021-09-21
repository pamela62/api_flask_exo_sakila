#Nous avons une configuration globale : Config 
class Config(object):
    DEBUG = False
    TESTING = False

# deux configurations spécifiques au environnement: ProductionConfig et DevelopmentConfig
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    #------------configuration à la connection mysql------------------
    "MYSQL_HOST" = "localhost"
    "MYSQL_USER" = "root"
    "MYSQL_PASSWORD" = "root"
    "MYSQL_DB" = "sakila"