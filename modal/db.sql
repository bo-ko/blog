CREATE DATABASE blog CHARSET=utf8;
USE blog;
CREATE TABLE articl(id int not null primary key auto_increment,
                    title varchar(50) not null,
                    sore varchar(25) not null,
                    time datetime not null,
                    views int default 0,
                    comments int default 0,
                    isDelete bit default 0
                    );

