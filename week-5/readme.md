

## 要求二
建立一個新的資料庫，取名字為 website。在資料庫中，建立會員資料表，取名字為 member。
```mysql
create database `website`;
use `website`;
 create table `member`(
    ->  `id` bigint primary key auto_increment,
    -> `name` varchar(255) not null,
    -> `username` varchar(255) not null,
    -> `password` varchar(255) not null,
    -> `follow_count` int not null default 0,
    -> `time` datetime not null default now());

```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/MemberTable.png)

## 要求三
使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
使用 SELECT 指令取得所有在 member 資料表中的會員資料。

```mysql
insert into `member` (name,username,password) values ("test","test","test");
select * from `member`;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/showMemberTable.png)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

```mysql
select * from `member` order by `time` ASC;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/OrderByASC.png)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
```mysql
select * from `member` order by `time` ASC limit 1,3;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/Limit13.png）
使用 SELECT 指令取得欄位 username 是 test 的會員資料。
```mysql
select * from `member` where `username` = "test";
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/usernameTest.png）
使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```mysql
select * from `member` where `username` = "test" AND `password`="test";
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/usernameTest.png）
使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```mysql
update `member` set `name`="test2" where `username`="test";
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/UpdateTest2.png）

## 要求四
取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```mysql
select count(*) from `member`;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/count.png）
取得 member 資料表中，所有會員 follower_count 欄位的總和。
```mysql
select sum(`follow_count`) from `member`;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/sum.png）
取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```mysql
select avg(`follow_count`) from `member`;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/avg.png）

## 要求五
在資料庫中，建立新資料表，取名字為 message。
```mysql
create table `message`(
    -> `id` bigint primary key auto_increment,
    -> `member_id` bigint not null,
    -> `content` varchar(255) not null,
    -> `time` datetime not null default now(),
    -> foreign key (`member_id`) references `member`(`id`));
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/MessageTable.png）
使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
```mysql
select `name`,`content` from `message` join `member` on `message`.`member_id` = `member`.`id`;
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/JoinContent.png）
使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
```mysql
select `username`,`name`,`content` from `message` join `member` on `message`.`member_id` = `member`.`id` where `username`="test";
```
![image](https://github.com/magam54/wehelp-assignments/blob/main/week-5/images/JoinTest.png）
