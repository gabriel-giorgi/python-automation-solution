# Created by ggiorgi at 4/7/2018
Feature: Project Management
  # Enter feature description here

  Scenario:
    Given I'm logged in redmine homepage
    When I go to project module
    And create a new project with following fields
    Then I should see the project created inside management module
    