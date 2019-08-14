#! /usr/bin env python3
# coding: utf-8


# lieu qui contient les methodes qui permettront de realiser les opérations utiles dans l'appli
# (ex get_unhealthy_products_by_category)
# c'est ici qu'on a le sql: toute la couche d'acces a la bdd

class BaseRepository:
    def __init__(self, db):
        self.db = db


class ProductRepository(BaseRepository):
    def get_all(self):
        rows = self.db.query("""
        
        """)
        pass

    def get_all_by_category(self, category):
        pass

    def get_all_by_score_upper(self, score):
        pass

    def write_in_db(self, link=None, name=None, brand=None, nutriscore=None, description=None):
        # requete sql de type insert
        pass


class CategoryRepository(BaseRepository):
    def write_in_db(self, name=None):
        # self.cursor = self.db.cursor()
        # add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(data_categories[category_number]))
        # self.cursor.execute(add_category)
        # self.db.commit()
        # self.cursor.close()
        pass

    pass


class StoreRepository(BaseRepository):
    pass


class UserRepository(BaseRepository):
    pass
