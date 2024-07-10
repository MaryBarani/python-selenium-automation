Feature: cart tests

  Scenario: check if the user's cart is empty when user login
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


