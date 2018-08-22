# Created by ggiorgi at 4/7/2018
Feature: Login - Login test
  As a user I want to be able to login into the app.

@Working
Scenario Outline: Login into application
Given I connect to redmine
When I enter my username "<user>" and password "<password>"
Then I should see my username "<user>" logged in the homepage
Examples:
  |user    |password|
  |Admin   |River123456|

