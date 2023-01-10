def browser():
    import undetected_chromedriver.v2 as undetectable

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = undetectable.ChromeOptions()

    #options.add_argument('--headless') #disables gui
    #options.add_argument('start-maximized')
    #options.add_argument('--disable-extensions')
    #options.add_argument('--window-size=1080,720');
    
    #options.add_argument('--disable-infobars')
    #options.add_argument('--disable-browser-side-navigation')
    #options.add_argument('--force-device-scale-factor=1')
    
    #options.add_argument('--log-level=3') #disables extensive log
    #options.add_argument('enable-automation') maybe redundant, better off for masking
    options.add_argument('--load-extension=../../../../../Users/jajce3/Documents/GitHub/kleRepublik/extensions/Deluminate_v0.7.7') #install Deluminate extension

    browser = undetectable.Chrome(options = options)

    #antiban: mask user agent
    #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    #browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})

    return browser
