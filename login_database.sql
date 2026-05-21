create database flask_project;
use flask_project;
create table user_data(username varchar(50) unique not null, password varchar(50) not null,
profile_name varchar(40) not null);
drop table user_data;
select * from user_data;