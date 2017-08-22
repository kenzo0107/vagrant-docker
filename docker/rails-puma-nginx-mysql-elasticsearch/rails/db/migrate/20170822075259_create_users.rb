class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :nickname
      t.string :first_name
      t.string :last_name
      t.string :email
      t.string :avatar
      t.string :city
      t.string :street_name
      t.string :street_address
      t.string :secondary_address
      t.string :building_number
      t.string :zip_code
      t.string :country
      t.string :latitude
      t.string :longitude

      t.timestamps
    end
  end
end
