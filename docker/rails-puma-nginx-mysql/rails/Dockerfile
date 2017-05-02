FROM ruby:2.4.1
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs mysql-client
RUN mkdir /app
WORKDIR /app
ADD ./rails/Gemfile /app/Gemfile
ADD ./rails/Gemfile.lock /app/Gemfile.lock
RUN bundle install
ADD . /app

# make directory for sockert
RUN mkdir -p tmp/sockets

VOLUME /app/public
VOLUME /app/tmp

CMD ["bundle", "exec", "puma"]
