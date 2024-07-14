Feature: Target circle tests

  Scenario: verify the number of benefit cells in Target circle are correct
    Given Open target main page
    When Click on Target circle
    Then Verify target circle page is open
    Then Verify there are 10 benefit cells on the target circle page
