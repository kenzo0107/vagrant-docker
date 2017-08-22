ActiveRecord::Base.transaction do
  User.delete_all
  100.times do
    User.create(
      nickname: Faker::Internet.user_name,
      first_name: Faker::Name.first_name,
      last_name: Faker::Name.last_name,
      email: Faker::Internet.email,
      avatar: Faker::Avatar.image,
      zip_code: Faker::Address.zip_code,
      state: Gimei.prefecture.kanji,
      city: Gimei.city.kanji,
      town: Gimei.town.kanji,
      latitude: Faker::Address.latitude,
      longitude: Faker::Address.longitude,
      birtyday: Faker::Date.birthday(18, 65)
    )
  end
end
