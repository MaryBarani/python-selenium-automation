Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Input car into search field and Click on search icon
    Then Product results for car are shown
    Then Verify correct search URL opens for car

  Scenario: check if every product on Target search results page has a product name and a product image
    Given Open target main page
    When Input car into search field and Click on search icon
    Then Verify that every product has a product name a product image


  Scenario: User can see favorite tooltip for search results
    Given Open target main page
    When Input tea into search field and Click on search icon
    And Hover favorite icon
    Then favorite tooltip is shown