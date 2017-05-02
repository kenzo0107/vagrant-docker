## Rails 5.1.0 (Puma) + Nginx + Mysql by docker-comopse on Vagrant(Ubuntu)

```
vagrant%$ cd /vagrant/rails-puma-nginx-mysql/
```

## create rails project via docker-comopse 

```
// database = mysql
vagrant%$ docker-compose run --rm web rails new . --force --database=mysql --skip-bundle

// You see new rails project.
vagrant%$ ls -al ./rails
```

## set puma.rb

```
// backup
vagrant%$ cp ./rails/config/puma.rb ./rails/config/puma.rb.bk
vagrant%$ cp puma.rb ./rails/config/
```

- ./rails/config/puma.rb

```
threads_count = ENV.fetch("RAILS_MAX_THREADS") { 5 }.to_i
threads threads_count, threads_count
port        ENV.fetch("PORT") { 3000 }
environment ENV.fetch("RAILS_ENV") { "development" }
plugin :tmp_restart

app_root = File.expand_path("../..", __FILE__)
bind "unix://#{app_root}/tmp/sockets/puma.sock"
```

## Create docker image

```
vagrant%$ docker-compose build

...
...

Successfully built 021f023d490a
```

## set database access information

```
// backup
vagrant%$ cp ./rails/config/database.yml ./rails/config/database.yml.bk
vagrant%$ cp database.yml ./rails/config/database.yml
```

- ./rails/config/database.yml

```
default: &default
  adapter: mysql2
  encoding: utf8
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
  username: root
  password: <%= ENV['MYSQL_ROOT_PASSWORD'] %>  # <--- MYSQL_ROOT_PASSWORD
  host: db # <--- service name
```


## create database using rails rake

```
vagrant%$ docker-compose run --rm web rake db:create
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

We are ready! run rails !

## run rails

```
vagrant%$ docker-compose up -d
```

You access to 'http://192.168.35.101', and see rails's Welcome page.
