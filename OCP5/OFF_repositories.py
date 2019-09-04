#! /usr/bin env python3
# coding: utf-8


# lieu qui contient les methodes qui permettront de realiser les opérations utiles dans l'appli
# (ex get_unhealthy_products_by_category)
# c'est ici qu'on a le sql: toute la couche d'acces a la bdd
# méthodes spécifiques pour les interactions avec la bdd. C'est ces repositories là qui vont se connecter à la bdd

class BaseRepository:
    def __init__(self, db):
        self.db = db


class ProductRepository(BaseRepository):

    def get_products_by_score_lower(self, score):
        bad_products = self.db.query(score.select_sql_query_prod)
        pass

    def get_products_by_category(self, category):
        category_products = self.db.query(category.select_sql_query_prod)
        pass

    def get_products_by_score_upper(self, score):
        pass

    def insert_by_model(self, product):
        """
        :param product:
        :type product: OFF_models.Product
        :return:
        """
        # requete sql de type insert:
        rows = self.db.query(product.insert_sql_query_product)


class CategoryRepository(BaseRepository):
    def insert_by_model(self, category):
        """
        :param category:
        :type category: OFF_models.Category
        :return:
        """
        # requete sql de type insert:
        rows = self.db.query(category.insert_sql_query)

    def get_category_by_product(self, product):
        category = self.db.query(product.select_sql_query_cat)


class StoreRepository(BaseRepository):
    pass


class UserRepository(BaseRepository):
    pass
