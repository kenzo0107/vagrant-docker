ActiveRecord::Base.transaction do
  Faker::Config.locale = :ja
  User.delete_all
  100.times do
    User.create(
      nickname: Faker::Name.name,
      first_name: Faker::Name.first_name,
      last_name: Faker::Name.last_name,
      email: Faker::Internet.email,
      avatar: Faker::Avatar.image,
      city: Faker::Address.city,
      street_name: Faker::Address.street_name,
      street_address: Faker::Address.street_address,
      secondary_address: Faker::Address.secondary_address,
      building_number: Faker::Address.building_number,
      zip_code: Faker::Address.zip_code,
      country: Faker::Address.country,
      latitude: Faker::Address.latitude,
      longitude: Faker::Address.longitude
    )
  end
end
