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
  idCategory INTEGER  NOT NULL  ,
  idMaterial INTEGER  NOT NULL  ,
  idColor INTEGER  NOT NULL  ,
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


CREATE INDEX Product_FKIndex1 ON Product (idCategory);
GO
CREATE INDEX Product_FKIndex2 ON Product (idMaterial);
GO
CREATE INDEX Product_FKIndex3 ON Product (idColor);
GO
CREATE INDEX Product_FKIndex4 ON Product (idWebsite);
GO


CREATE INDEX IFK_Rel_07 ON Product (idCategory);
GO
CREATE INDEX IFK_Rel_08 ON Product (idMaterial);
GO
CREATE INDEX IFK_Rel_09 ON Product (idColor);
GO
CREATE INDEX IFK_Rel_10 ON Product (idWebsite);
GO



