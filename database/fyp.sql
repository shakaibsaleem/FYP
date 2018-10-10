CREATE TABLE Material (
  idMaterial INTEGER  NOT NULL   IDENTITY ,
  Material VARCHAR(20)      ,
PRIMARY KEY(idMaterial));
GO




CREATE TABLE Website (
  idWebsite INTEGER  NOT NULL   IDENTITY ,
  WName VARCHAR(20)    ,
  WAddress VARCHAR(50)      ,
PRIMARY KEY(idWebsite));
GO




CREATE TABLE Category (
  idCategory INTEGER  NOT NULL   IDENTITY ,
  Category VARCHAR(20)      ,
PRIMARY KEY(idCategory));
GO




CREATE TABLE Color (
  idColor INTEGER  NOT NULL   IDENTITY ,
  Color VARCHAR(20)      ,
PRIMARY KEY(idColor));
GO




CREATE TABLE Product (
  idProduct INTEGER  NOT NULL   IDENTITY ,
  idColor INTEGER  NOT NULL  ,
  idMaterial INTEGER  NOT NULL  ,
  idCategory INTEGER  NOT NULL  ,
  idWebsite INTEGER  NOT NULL  ,
  PName VARCHAR(20)    ,
  PPrice FLOAT    ,
  PAddress VARCHAR(20)    ,
  PisAvaialble BIT      ,
PRIMARY KEY(idProduct)        ,
  FOREIGN KEY(idCategory)
    REFERENCES Category(idCategory),
  FOREIGN KEY(idMaterial)
    REFERENCES Material(idMaterial),
  FOREIGN KEY(idColor)
    REFERENCES Color(idColor),
  FOREIGN KEY(idWebsite)
    REFERENCES Website(idWebsite));
GO


CREATE INDEX Product_FKIndex2 ON Product (idCategory);
GO
CREATE INDEX Product_FKIndex3 ON Product (idMaterial);
GO
CREATE INDEX Product_FKIndex4 ON Product (idColor);
GO
CREATE INDEX Product_FKIndex4 ON Product (idWebsite);
GO


CREATE INDEX IFK_Rel_02 ON Product (idCategory);
GO
CREATE INDEX IFK_Rel_03 ON Product (idMaterial);
GO
CREATE INDEX IFK_Rel_04 ON Product (idColor);
GO
CREATE INDEX IFK_Rel_05 ON Product (idWebsite);
GO



