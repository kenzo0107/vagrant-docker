require 'test_helper'

class UsersControllerTest < ActionDispatch::IntegrationTest
  setup do
    @user = users(:one)
  end

  test "should get index" do
    get users_url
    assert_response :success
  end

  test "should get new" do
    get new_user_url
    assert_response :success
  end

  test "should create user" do
    assert_difference('User.count') do
      post users_url, params: { user: { avatar: @user.avatar, building_number: @user.building_number, city: @user.city, country: @user.country, email: @user.email, first_name: @user.first_name, last_name: @user.last_name, latitude: @user.latitude, longitude: @user.longitude, nickname: @user.nickname, secondary_address: @user.secondary_address, street_address: @user.street_address, street_name: @user.street_name, zip_code: @user.zip_code } }
    end

    assert_redirected_to user_url(User.last)
  end

  test "should show user" do
    get user_url(@user)
    assert_response :success
  end

  test "should get edit" do
    get edit_user_url(@user)
    assert_response :success
  end

  test "should update user" do
    patch user_url(@user), params: { user: { avatar: @user.avatar, building_number: @user.building_number, city: @user.city, country: @user.country, email: @user.email, first_name: @user.first_name, last_name: @user.last_name, latitude: @user.latitude, longitude: @user.longitude, nickname: @user.nickname, secondary_address: @user.secondary_address, street_address: @user.street_address, street_name: @user.street_name, zip_code: @user.zip_code } }
    assert_redirected_to user_url(@user)
  end

  test "should destroy user" do
    assert_difference('User.count', -1) do
      delete user_url(@user)
    end

    assert_redirected_to users_url
  end
end
