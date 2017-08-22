#!/bin/bash

sudo rm -rf app/ config db/ log/ public/ README.md tmp bin config.ru lib/ package.json Rakefile test vendor
cp /dev/null Gemfile.lock
cp Gemfile.bk Gemfile
