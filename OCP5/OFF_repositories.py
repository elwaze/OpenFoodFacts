#! /usr/bin env python3
# coding: utf-8


# lieu qui contient les methodes qui permettront de realiser les opérations utiles dans l'appli
# (ex get_unhealthy_products_by_category)
# c'est ici qu'on a le sql: toute la couche d'acces a la bdd
# méthodes spécifiques pour les interactions avec la bdd. C'est cest repositories là qui vont se connecter à la bdd

class BaseRepository:
    def __init__(self, db):
        self.db = db


class ProductRepository(BaseRepository):
    def get_products(self):
        # on en a besoin de celle là ???
        rows = self.db.query("""
            SELECT *
        """)
        pass

    def get_products_by_category(self, category):
        pass

    def get_products_by_score_upper(self, score):
        pass

    def get_products_by_score_lower(self, score):
        pass

    def insert(self, link=None, name=None, nutriscore=None, categories=None):
        # requete sql de type insert:
        rows = self.db.query("""
            INSERT
        """)
        pass

    def insert_by_model(self, product):
        """

        :param product:
        :type product: OFF_models.Product
        :return:
        """
        # requete sql de type insert:
        rows = self.db.query(product.insert_sql_query)
        pass

class CategoryRepository(BaseRepository):
    def write_in_db(self, name=None, products=None, ):
        # self.cursor = self.db.cursor()
        # add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(data_categories[category_number]))
        # self.cursor.execute(add_category)
        # self.db.commit()
        # self.cursor.close()
        pass


class StoreRepository(BaseRepository):
    pass


class UserRepository(BaseRepository):
    pass
