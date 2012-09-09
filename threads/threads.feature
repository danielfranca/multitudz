Feature: Threads
Scenario: Create Thread
    Given a logged user
    When I click "New Thread"
    And I type in field "participants" value "Da"
    And I fill in field "title" with value "Testando criação de thread"
    And I fill in field "body" with value "Novo campo</br>Testando linha 2    FIM"
    And I send the form
    Then I see the text "Testando criação de thread"