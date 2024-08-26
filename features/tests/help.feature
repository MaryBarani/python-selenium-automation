Feature: Target Help UI tests


  Scenario:  verify Target Help UI
    Given Open target help  page
    Then Verify UI elements


  Scenario Outline: user can select help topics
    Given Open target help return page
    Then Verify <page_name_1> page is open
    Given Select <expected_text> from Browse help dropdown
    Then Verify <page_name_2> page is open
    Examples:
      |page_name_1  |expected_text      |page_name_2  |
      |Returns      |Partner Programs   |Beauty at Target |
      |Returns      |Orders & Purchases |Print a receipt  |
      |Returns      |Returns & Exchanges |Returns  |
      |Returns      |Promotions & Coupons |Current promotions  |
