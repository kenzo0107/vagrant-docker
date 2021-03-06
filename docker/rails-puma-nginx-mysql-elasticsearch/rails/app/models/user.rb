class User < ApplicationRecord
  include Elasticsearch::Model
  include Elasticsearch::Model::Callbacks

  INDEX_FIELDS = %w(nickname first_name last_name email avatar zip_code state city town latitude longitude birthday).freeze
  index_name "es-index-users-#{Rails.env}"

  # mapping
  settings do
    mappings dynamic: 'false' do
      indexes :nickname,          analyzer: 'kuromoji', type: 'string'
      indexes :first_name,        analyzer: 'kuromoji', type: 'string'
      indexes :last_name,         analyzer: 'kuromoji', type: 'string'
      indexes :email,             analyzer: 'kuromoji', type: 'string'
      indexes :avatar,            analyzer: 'kuromoji', type: 'string'
      indexes :zip_code,          analyzer: 'kuromoji', type: 'string'
      indexes :state,             analyzer: 'kuromoji', type: 'string'
      indexes :city,              analyzer: 'kuromoji', type: 'string'
      indexes :town,              analyzer: 'kuromoji', type: 'string'
      indexes :latitude,          analyzer: 'kuromoji', type: 'string'
      indexes :longitude,         analyzer: 'kuromoji', type: 'string'
      indexes :birtyday,          analyzer: 'kuromoji', type: 'string'
    end
  end

  def as_indexed_json(option = {})
    self.as_json.select { |k, _| INDEX_FIELDS.include?(k) }
  end

  class << self
    def search(query)
      __elasticsearch__.search({
        query: {
          multi_match: {
            fields: INDEX_FIELDS,
            fuzziness: 'AUTO',
            query: query
          }
        }
      })
    end

    def create_index!
      client = __elasticsearch__.client
      client.indices.delete index: self.index_name rescue nil
      client.indices.create(index: self.index_name,
                            body: {
                                settings: self.settings.to_hash,
                                mappings: self.mappings.to_hash
                            })
    end
  end
end
