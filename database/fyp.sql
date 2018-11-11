CREATE TABLE Website (
  idWebsite INTEGER  NOT NULL   IDENTITY ,
  WName VARCHAR(50)    ,
  WAddress VARCHAR(200)      ,
PRIMARY KEY(idWebsite));
GO




CREATE TABLE ScraperRun (
  idScraperRun INTEGER  NOT NULL   IDENTITY ,
  TimeStamp DATETIME  NOT NULL    ,
PRIMARY KEY(idScraperRun));
GO




CREATE TABLE Users (
  idUser INTEGER  NOT NULL   IDENTITY ,
  Username VARCHAR(20)  NOT NULL  ,
  Passkey VARCHAR(20)  NOT NULL  ,
  FirstName VARCHAR(20)    ,
  LastName VARCHAR(20)    ,
  Contact VARCHAR(12)    ,
  Email VARCHAR(50)  NOT NULL    ,
PRIMARY KEY(idUser));
GO




CREATE TABLE Material (
  idMaterial INTEGER  NOT NULL   IDENTITY ,
  Material VARCHAR(20)      ,
PRIMARY KEY(idMaterial));
GO




CREATE TABLE Color (
  idColor INTEGER  NOT NULL   IDENTITY ,
  Color VARCHAR(20)      ,
PRIMARY KEY(idColor));
GO




CREATE TABLE Category (
  idCategory INTEGER  NOT NULL   IDENTITY ,
  Category VARCHAR(20)      ,
PRIMARY KEY(idCategory));
GO




CREATE TABLE Product (
  idProduct INTEGER  NOT NULL   IDENTITY ,
  idCategory INTEGER  NOT NULL  ,
  idMaterial INTEGER  NOT NULL  ,
  idColor INTEGER  NOT NULL  ,
  idWebsite INTEGER  NOT NULL  ,
  PName VARCHAR(50)    ,
  PPrice FLOAT    ,
  PAddress VARCHAR(200)  NOT NULL  ,
  PisAvaialble BIT    ,
  PCode VARCHAR(20)    ,
  PDescription VARCHAR(200)      ,
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


CREATE TABLE Likes (
  idUser INTEGER  NOT NULL  ,
  idProduct INTEGER  NOT NULL    ,
PRIMARY KEY(idUser, idProduct)    ,
  FOREIGN KEY(idUser)
    REFERENCES Users(idUser),
  FOREIGN KEY(idProduct)
    REFERENCES Product(idProduct));
GO


CREATE INDEX Likes_FKIndex1 ON Likes (idUser);
GO
CREATE INDEX Likes_FKIndex2 ON Likes (idProduct);
GO


CREATE INDEX IFK_Rel_07 ON Likes (idUser);
GO
CREATE INDEX IFK_Rel_09 ON Likes (idProduct);
GO


CREATE TABLE ScrapingDetails (
  idProduct INTEGER  NOT NULL  ,
  idScraperRun INTEGER  NOT NULL  ,
  ActivityDetails VARCHAR(20)  NOT NULL    ,
PRIMARY KEY(idProduct, idScraperRun)    ,
  FOREIGN KEY(idProduct)
    REFERENCES Product(idProduct),
  FOREIGN KEY(idScraperRun)
    REFERENCES ScraperRun(idScraperRun));
GO


CREATE INDEX ScrapingDetails_FKIndex1 ON ScrapingDetails (idProduct);
GO
CREATE INDEX ScrapingDetails_FKIndex2 ON ScrapingDetails (idScraperRun);
GO


CREATE INDEX IFK_Rel_11 ON ScrapingDetails (idProduct);
GO
CREATE INDEX IFK_Rel_12 ON ScrapingDetails (idScraperRun);
GO


CREATE TABLE ProductsViewed (
  idProduct INTEGER  NOT NULL  ,
  idUser INTEGER  NOT NULL  ,
  TimeStamp DATETIME  NOT NULL    ,
PRIMARY KEY(idProduct, idUser)    ,
  FOREIGN KEY(idProduct)
    REFERENCES Product(idProduct),
  FOREIGN KEY(idUser)
    REFERENCES Users(idUser));
GO


CREATE INDEX ProductsViewed_FKIndex1 ON ProductsViewed (idProduct);
GO
CREATE INDEX ProductsViewed_FKIndex2 ON ProductsViewed (idUser);
GO


CREATE INDEX IFK_Rel_11 ON ProductsViewed (idProduct);
GO
CREATE INDEX IFK_Rel_12 ON ProductsViewed (idUser);
GO



