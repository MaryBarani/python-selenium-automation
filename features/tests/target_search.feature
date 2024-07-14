Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Input car into search field
    And Click on search icon
    Then Product results for car are shown