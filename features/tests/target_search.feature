Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Input car into search field and Click on search icon
    Then Product results for car are shown

  Scenario: check if every product on Target search results page has a product name and a product image
    Given Open target main page
    When Input car into search field and Click on search icon
    Then Verify that every product has a product name a product image