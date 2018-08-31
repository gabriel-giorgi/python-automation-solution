# Created by ggiorgi at 4/7/2018
Feature: Project Management
  # Enter feature description here
  @Broken
  Scenario:
    Given I'm logged in redmine homepage
    When I go to project module
    And create a new project with following fields

      | issue_tracking |  | True  |
      | time_tracking  |  | False |
      | news           |  | True  |
      | documents      |  | False |
      | files          |  | True  |
      | wiki           |  | False |
      | repository     |  | True  |
      | calendar       |  | False |
      | gantt          |  | True  |

    Then I should see the project created inside management module
