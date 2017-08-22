json.extract! user, :id, :nickname, :first_name, :last_name, :email, :avatar, :zip_code, :state, :city, :town, :latitude, :longitude, :birtyday, :created_at, :updated_at
json.url user_url(user, format: :json)
