
Feature: test caces for the sign in page

  Scenario: Check if the  user can login with the correct credential
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
    When Input olegriznuk@hotrokh.com and Test1234 on SignIn page
    When Click Sign In with password
    Then Verify user is logged in

 Scenario: Check if website do not allow the user to login with incorrect credential
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened
    When Input test@gmail.com and Test123433332 on SignIn page
    When Click Sign In with password
    Then Verifies that “We can't find your account.” message is shown



