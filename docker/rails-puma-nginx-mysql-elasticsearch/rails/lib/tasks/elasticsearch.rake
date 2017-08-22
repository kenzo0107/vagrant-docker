namespace :elasticsearch do
  desc 'create index of Elasticsearch'
  task :create_index => :environment do
    User.create_index!
  end

  desc 'register User to Elasticsearch'
  task :import => :environment do
    User.import
  end
end
