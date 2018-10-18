RDS is one of Amazon services that can be used to create database. 
# RDS
To create database and connect it to your code. You should follow the steps bellow:
1. Open your AWS management cosole.
2. In All Services you will find Database.Click on RDS.
3. Click on create database
<img width="1059" alt="screen shot 2018-10-18 at 11 03 32 am" src="https://user-images.githubusercontent.com/31826320/47165342-c037b000-d2c7-11e8-9a4e-676b6b21a526.png">
<img width="1208" alt="screen shot 2018-10-18 at 11 05 33 am" src="https://user-images.githubusercontent.com/31826320/47165343-c037b000-d2c7-11e8-94b4-ad0eed934c09.png">
4. Choose type of the database (I chose mysql)
<img width="1407" alt="screen shot 2018-10-18 at 11 06 49 am" src="https://user-images.githubusercontent.com/31826320/47165344-c037b000-d2c7-11e8-9da0-d0c990b9a187.png">
5. Enter database Instance name and username and password. You need these with database connection in your code.
<img width="1375" alt="screen shot 2018-10-18 at 11 12 17 am" src="https://user-images.githubusercontent.com/31826320/47165345-c037b000-d2c7-11e8-9083-6bd1a8ba3c78.png">
6. database name and port. You also need these with database connection in your code.
<img width="1060" alt="screen shot 2018-10-18 at 11 12 29 am" src="https://user-images.githubusercontent.com/31826320/47165346-c037b000-d2c7-11e8-8091-845b66a72ab1.png">
7.Click on create database 
<img width="1239" alt="screen shot 2018-10-18 at 11 13 03 am" src="https://user-images.githubusercontent.com/31826320/47165347-c037b000-d2c7-11e8-815f-18c04e798bdd.png">
8. Back to Dashboard and click on DB Instances
<img width="1117" alt="screen shot 2018-10-18 at 11 15 22 am" src="https://user-images.githubusercontent.com/31826320/47165348-c0d04680-d2c7-11e8-8966-a632ec433907.png">
9. Click on database and click on DB Instance that you create.
<img width="1623" alt="screen shot 2018-10-18 at 11 15 38 am" src="https://user-images.githubusercontent.com/31826320/47165349-c0d04680-d2c7-11e8-8ed9-0d7cadcfa652.png">
10. Now you can get endpoint and DB name and username.
<img width="1627" alt="screen shot 2018-10-18 at 11 15 58 am" src="https://user-images.githubusercontent.com/31826320/47165350-c0d04680-d2c7-11e8-9271-152bcedb688d.png">
11. Go to application.py and change the following based on your database. 
     ```
        app.config['MYSQL_DATABASE_HOST'] = 'endpoint of the database from RDS'
        app.config['MYSQL_DATABASE_USER'] = 'username of the database from RDS'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'Password of the database from RDS'
        app.config['MYSQL_DATABASE_DB'] = 'name of the of the database from RDS'
      ```
12. Go to terminal and enter the followings:
      ```
        export PATH=$PATH:/usr/local/mysql/bin
        mysql -h <endpoint> -P 3306 -u <username> -p
      ```
13. Click eneter Then termianl will ask you to enter password. Enter your DB password.
14. Enter your mysql code (e.g. create tabel)
<img width="1067" alt="screen shot 2018-10-18 at 11 38 04 am" src="https://user-images.githubusercontent.com/31826320/47166628-a2b81580-d2ca-11e8-8c5d-f34417b33b75.png">
15. The following mysql code is to create table that will work in my example above.
     
     ```
          show databases;
          use yourdatabase name;
          CREATE TABLE users( 
          id INTEGER PRIMARY KEY AUTO_INCREMENT, 
          name varchar(20) UNIQUE NOT NULL,email varchar(30), 
          password TEXT NOT NULL);
          
      ```

