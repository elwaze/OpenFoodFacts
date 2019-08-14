#! /usr/bin env python3
# coding: utf-8

from OFF_repositories import ProductRepository
from OFF_repositories import CategoryRepository
from OFF_repositories import StoreRepository
from OFF_repositories import UserRepository
from database import db


class Product:
    objects = ProductRepository(db)

    def __init__(
            self,
            link=None,
            name=None,
            brand=None,
            nutriscore=None,
            categories=None,
            stores=None,
            users=None
    ):
        self.link = link
        self.name = name
        self.brand = brand
        self.nutriscore = nutriscore
        self.categories = categories    # collection / liste (si ordonné)
        self.stores = stores    # collection / liste (si ordonné)
        self.users = users  # collection / liste (si ordonné)


class Category:
    objects = CategoryRepository(db)

    def __init__(
            self,
            name=None,
            average_nutriscore=None,
            products=None
    ):
        self.name = name
        self.average_nutriscore = average_nutriscore
        self.products = products    # collection / liste (si ordonné)


class Store:
    objects = StoreRepository(db)

    def __init__(
            self,
            name=None,
            products=None
    ):
        self.name = name
        self.products = products    # collection / liste (si ordonné)
        self.idstore = None


class User:
    objects = UserRepository(db)

    def __init__(
            self,
            name=None,
            products=None
    ):
        self.name = name
        self.products = products


if __name__ == "__main__":
    pass
