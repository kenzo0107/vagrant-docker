json.extract! user, :id, :nickname, :first_name, :last_name, :email, :avatar, :city, :street_name, :street_address, :secondary_address, :building_number, :zip_code, :country, :latitude, :longitude, :created_at, :updated_at
json.url user_url(user, format: :json)
