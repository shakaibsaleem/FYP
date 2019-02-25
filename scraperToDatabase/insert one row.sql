insert into Category values ('unstitched')
insert into Color values ('Yellow')
insert into Material values ('Lawn')
insert into Website values ('Khaadi','https://www.khaadi.com/pk/')

select * from Category
select * from Color
select * from Material
select * from Website

insert into Product values ((select idCategory from Category where Category = 'unstitched'),(select idMaterial from Material where Material = 'Lawn'),(select idColor from Color where Color = 'Yellow'),(select idWebsite from Website where WName = 'Khaadi'),'DF19104',3300,'https://www.khaadi.com/pk/df19104-yellow-3pc.html',1,'df19104-yellow-3pc','Front Lawn Printed 1.25mBack Lawn Printed 1.25mSleeve Lawn Printed 0.5mChiffon Printed Dupatta 2.5mShalwar 2.5m')
select * from Product
