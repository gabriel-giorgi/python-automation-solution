# Created by ggiorgi at 4/7/2018
Feature: Project Management
  # Enter feature description here

  @Working
  Scenario: Create new project
    Given I'm logged in redmine homepage
    When I go to project module
    And create a new project with following fields
      | module name    | enabled |
      | issue_tracking | True    |
      | time_tracking  | False   |
      | news           | True    |
      | documents      | False   |
      | files          | True    |
      | wiki           | False   |
      | repository     | True    |
      | calendar       | False   |
      | gantt          | True    |

    Then I should see the project created inside management module

  @Working
  Scenario Outline: Delete project
    Given I'm logged in redmine homepage
    When I go to administration module
    And I go to projects submodule
    And I delete "<project_name>" project
    Then I should not see "<project_name>" inside management module
    Examples:
      | project_name   |
      | Joseph Mcmahon |


  @NotImplementedYet
  Scenario Outline: Create new issue status
    Given I'm logged in redmine homepage
    When I go to administration module
    And  I go to issue statuses
    And  I create following new status : "<status_name>"
    Examples:
      | status_name |
      | test status |