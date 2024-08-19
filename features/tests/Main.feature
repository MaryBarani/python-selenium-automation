Feature: Main page tests

  Scenario: Check if the logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened


  Scenario: Check if the  user can login with the correct credential
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
    When Input olegriznuk@hotrokh.com and Test1234 on SignIn page
    When Click Sign In with password
    Then Verify user is logged in

