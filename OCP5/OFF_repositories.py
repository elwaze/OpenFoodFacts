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

    def write_in_db(self):
        pass


class CategoryRepository(BaseRepository):
    pass


class StoreRepository(BaseRepository):
    pass


class UserRepository(BaseRepository):
    pass
