CREATE DATABASE CHARACTER SET 'latin1';


-- CREATE TABLES

  -- TABLE : product
  CREATE TABLE product (
      id INT UNSIGNED NOT NULL AUTO_INCREMENT,
      product_name VARCHAR(50) NOT NULL, UNIQUE,
      product_brand VARCHAR(100) NOT NULL,
      nutrition_grade CHAR(1) NOT NULL,
      product_url VARCHAR(2000) NOT NULL,
      product_store VARCHAR(200) DEFAULT NULL,
      fat FLOAT DEFAULT NULL,
      sugar FLOAT DEFAULT NULL,
      category VARCHAR(200) DEFAULT NULL,
      PRIMARY KEY (id)
  )ENGINE=InnoDB;

  -- TABLE : category
  CREATE TABLE category (
      id INT UNSIGNED NOT NULL AUTO_INCREMENT,
      category_name VARCHAR(150) NOT NULL,
      PRIMARY KEY (id)
  )ENGINE=InnoDB;

  -- TABLE : saved
  CREATE TABLE saved (
      id INT UNSIGNED NOT NULL AUTO_INCREMENT,
      saved_product_name VARCHAR(50) NOT NULL,
      saved_substitute_name VARCHAR(50) NOT NULL,
      PRIMARY KEY (id)
  )ENGINE=InnoDB;

  -- TABLE : category_products
  CREATE TABLE category_products (
  	  product_id INT UNSIGNED,
  	  category_id INT UNSIGNED,
  )ENGINE=INNODB;


-- CREATE FOREIGN KEY

    -- FK category_products : product_id
    ALTER TABLE category_products
    ADD CONSTRAINT fk_cat_prod_product_id FOREIGN KEY (product_id) REFERENCES product(id);

    -- FK category_product : category_id
    ALTER TABLE category_products
    ADD CONSTRAINT fk_cat_prod_product_id FOREIGN KEY (category_id) REFERENCES category(id);

    -- FK saved :  saved_product_name
    ALTER TABLE saved
    ADD CONSTRAINT fk_sav_prod_product_id FOREIGN KEY (saved_product_name) REFERENCES product(id);

    -- FK saved : saved_substitute_name
    ALTER TABLE saved
    ADD CONSTRAINT fk_sav_subs_product_id FOREIGN KEY (saved_substitute_name) REFERENCES product(id);


-- CREATE INDEXES

    -- Index category : category_name
    ALTER TABLE category
    ADD INDEX ind_cat_name (category_name);

    -- Index product : product_name
    ALTER TABLE product
    ADD INDEX ind_product_name (product_name);