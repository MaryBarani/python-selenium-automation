Feature: Main page tests

  Scenario: Check if the logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In and From right side navigation menu, click Sign In
    Then Verify Sign In form opened


