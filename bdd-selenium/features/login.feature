Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @smoke @regression
  Scenario: Check that the URL is correct
    Then The URL of the Login Page is correct

  @regression
  Scenario Outline: Log in with unregistered email
    When I enter "<username>" as email
    And I enter "<password>" as password
    And I click the login button
    Then I should see "No customer account found" message
    Examples:
      | username          | password       |
      | pyta9@gmail.com   | 12345678       |
      | pyta9@yahoo.com   | 63246723547623 |
      | google.@gmail.com | asdfghjklcvb   |