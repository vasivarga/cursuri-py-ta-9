Feature: Registration page

  Background: Open register page
    Given I am on the register page

  Scenario: Check that the URL is correct
    Then The URL of the Register Page is correct

  Scenario: Register new account with valid data
    When I enter "PY" in the first name input
    And I enter "TA" in the last name input
    And I select "10" "May" "1999" as my birth date
    And I enter a random email address in the email input
    And I enter "pisicaneagra" in the password input
    And I enter "pisicaneagra" in the password confirm input
    And I click the register button
    Then Success message is displayed
    And The success message is "Your registration completed"

  Scenario: Register without completing mandatory fields
    When I click the register button
    Then First name error is displayed
    And Last name error is displayed
    And Email error is displayed
    And Password error is displayed
    And Confirm password error is displayed
