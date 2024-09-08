Feature: Main page tests

  @smoke
  Scenario: Check if the logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened





