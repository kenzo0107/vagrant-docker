FROM ruby:2.4.1
MAINTAINER Kenzo Tanaka <kenzo.tanaka0107@gmail.com>

RUN apt-get update -qq && apt-get install -y git build-essential libpq-dev nodejs mysql-client
RUN mkdir /app
WORKDIR /app

COPY ./rails/Gemfile      /app/Gemfile
COPY ./rails/Gemfile.lock /app/Gemfile.lock
RUN bundle install -j4

COPY . /app

# make directory for sockert
RUN mkdir -p /app/tmp/sockets

VOLUME /app/tmp

RUN bundle exec rails assets:precompile RAILS_ENV=production

EXPOSE 3000

CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
