class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :nickname
      t.string :first_name
      t.string :last_name
      t.string :email
      t.string :avatar
      t.string :zip_code
      t.string :state
      t.string :city
      t.string :town
      t.string :latitude
      t.string :longitude
      t.date :birtyday

      t.timestamps
    end
  end
end
