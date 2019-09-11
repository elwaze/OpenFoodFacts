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

    def get_products_by_user(self, user):
        user_products = self.db.query(user.select_sql_query_prod)
        return user_products

    def get_better_product(self, score):
        better_product = self.db.query(score.select_sql_query_prod)
        return better_product

    def insert_by_model(self, product):
        """
        :param product:
        :type product: purbeurre_models.Product
        :return:
        """
        # requete sql de type insert:
        rows = self.db.query(product.insert_sql_query_product)
        for store in product.stores:
            rows = self.db.query(product.insert_sql_query_store(store))
            rows = self.db.query(product.insert_sql_query_prod_store_relation)
        rows = self.db.query(product.insert_sql_query_categories_products_relation)


class CategoryRepository(BaseRepository):
    def insert_by_model(self, category):
        """
        :param category:
        :type category: purbeurre_models.Category
        :return:
        """
        # requete sql de type insert:
        rows = self.db.query(category.insert_sql_query)

    def get_category_by_product(self, product):
        category = self.db.query(product.select_sql_query_cat)
        return category

    def get_categories(self):
        categories = self.db.query('SELECT name FROM category;')
        return categories

    def get_products_by_category(self, category):
        category_products = self.db.query(category.select_sql_query_prod)
        return category_products


class StoreRepository(BaseRepository):

    def get_store_by_product(self, product):
        stores = self.db.query(product.select_sql_query_stores)
        return stores


class UserRepository(BaseRepository):
    def insert_by_model(self, user):
        rows = self.db.query(user.insert_sql_query)
