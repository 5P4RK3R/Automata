*** Settings ***
Library    SeleniumLibrary

# *** Variables ***
# ${BROWSER}    chromium
# ${HEADLESS}    false

*** Keywords ***

Set Chrome Options
    [Arguments]    ${prefs}
    Create Dictionary    args=--use-fake-ui-for-media-stream    prefs=${prefs}
    Set Variable    ${chrome_options}    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_experimental_option    prefs    ${prefs}
    Call Method    ${chrome_options}    add_argument    --use-fake-ui-for-media-stream
    [Return]    ${chrome_options}

Start Chrome With Media Permissions
    [Arguments]    ${url}
    ${prefs}    Create Dictionary    profile.default_content_setting_values.media_stream_camera=1    profile.default_content_setting_values.media_stream_mic=1
    ${chrome_options}    Set Chrome Options    ${prefs}
    Open Browser    ${url}    browser=chrome    options=${chrome_options}
    Maximize Browser Window

Setup Instagram Flow
    [Arguments]    ${url}
    Open Browser    url=${url}   browser=chrome
    Sleep    5s
    # Start Chrome With Media Permissions
    # ${caps}=    Evaluate    sys.modules['selenium.webdriver'].common.desired_capabilities.DesiredCapabilities.CHROME    sys, selenium
    # # Set To Dictionary    ${caps}    goog:loggingPrefs    {"browser": "ALL"}
    # Create WebDriver    Chrome    desired_capabilities=${caps}
    Maximize Browser Window
    Input Text    //input[@name='username']    mahendransparker@gmail.com
    Input Text    //input[@name='password']    gojuryu45
    Click Button     css:button[type="submit"]
    Sleep    10s
    Click Element  xpath=//div[@role="button" and text()="Not now"]
    Sleep    10s
    Click Button    xpath://div[@role='dialog']//button[@tabindex='0' and contains(text(), 'Not Now')]
    
    Sleep    10s
    Click Element    xpath=//span[contains(text(), 'Profile')]
    Sleep    10s
    Click Element    //a[contains(@href, '/following/') and @role='link' and @tabindex='0']

    Sleep    10s
    Click Element    //button[normalize-space(text())='Following']
    Sleep    100s
    # Close Browser