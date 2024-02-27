Feature: Login Page

  @smoke @regression
  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the page is

  @regression
  Scenario Outline: Log in with unregistered email
    Given I am on the login page
    When I enter "<username>" as email
    And I enter "<password>" as password
    And I click the login button
    Then I should see "No customer account found" message
    Examples:
      | username          | password       |
      | pyta9@gmail.com   | 12345678       |
      | pyta9@yahoo.com   | 63246723547623 |
      | google.@gmail.com | asdfghjklcvb   |

