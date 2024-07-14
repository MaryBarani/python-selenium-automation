Feature: cart tests

  Scenario: check if the user's cart is empty when user login
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: Check if the user is able to add an item to cart
    Given Open target main page
    When Input dress into search field
    And Click on search icon
    Then Product results for dress are shown
    When Click on add to card button
#    Then Verify the item is added to the cart