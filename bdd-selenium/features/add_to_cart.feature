Feature: Add to cart

  Background: Open home page
    Given I am on the home page


  Scenario: Add to cart
    When I enter "HTC" in the search field
    And I click the search button
    And I click Add to cart
    Then Cart has "1" item in it