# Rails (Puma) + Nginx + Mysql + Elasticsearch by docker-comopse on Vagrant(Ubuntu)

## Setup

```
macOS%$ git clone https://github.com/kenzo0107/vagrant-docker
macOS%$ cd vagrant-docker
macOS%$ vagrant up
macOS%$ vagrant ssh
vagrant%$ cd /vagrant/rails-puma-nginx-mysql-elasticsearch/
vagrant%$ docker-compose up -d
```

## create database

```
vagrant%$ docker-compose run --rm web rails db:create

Created database 'app_development'
Created database 'app_test'

vagrant%$ docker-compose exec db mysql -u root -p -e'show databases;'
Enter password: (password)
+--------------------+
| Database           |
+--------------------+
| information_schema |
| app_development    | <--- add !
| app_test           | <--- add !
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

## create table `users`

```
vagrant%$ docker-compose exec web rails db:migrate

vagrant%$ docker-compose exec db mysql -u root -p app_development -e'show full columns from users;'
Enter password:
+------------+--------------+-----------------+------+-----+---------+----------------+---------------------------------+---------+
| Field      | Type         | Collation       | Null | Key | Default | Extra          | Privileges                      | Comment |
+------------+--------------+-----------------+------+-----+---------+----------------+---------------------------------+---------+
| id         | bigint(20)   | NULL            | NO   | PRI | NULL    | auto_increment | select,insert,update,references |         |
| nickname   | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| first_name | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| last_name  | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| email      | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| avatar     | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| zip_code   | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| state      | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| city       | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| town       | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| latitude   | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| longitude  | varchar(255) | utf8_general_ci | YES  |     | NULL    |                | select,insert,update,references |         |
| birtyday   | date         | NULL            | YES  |     | NULL    |                | select,insert,update,references |         |
| created_at | datetime     | NULL            | NO   |     | NULL    |                | select,insert,update,references |         |
| updated_at | datetime     | NULL            | NO   |     | NULL    |                | select,insert,update,references |         |
+------------+--------------+-----------------+------+-----+---------+----------------+---------------------------------+---------+
```

## Seed

```
vagrant%$ docker-compose run --rm web rails db:seed
```

## Create the index of Elasticsearch

```
vagrant%$ docker-compose exec web rails elasticsearch:create_index
```

check the indexes of elasticsearch.

```
vagrant%$ curl localhost:9200/_aliases?pretty
{
  "es-index-users-development" : {
    "aliases" : { }
  },
  ".kibana" : {
    "aliases" : { }
  }
}
```

```
vagrant%$ docker-compose exec web rails elasticsearch:import
```

## Kibana

Access [http://192.168.35.101:5601](http://192.168.35.101:5601)

fill in `es-index-users-development` on *Index name or pattern* .

![Imgur](http://i.imgur.com/DLkDoEs.png)

Click [Discover](http://192.168.35.103:5601/app/kibana#/discover?_g=()) in kibana menu,  
you see data list of users.


## Rails access to Elasticsearch

Access to [http://192.168.35.101/users](http://192.168.35.101/users) from browser.

You fill in `千葉` to input box and you can see data list related `千葉`.

![Imgur](http://i.imgur.com/rM7Urbu.png)
