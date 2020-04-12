package pageTests;

import resources.UrlVariables;

import org.apache.logging.log4j.Logger;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import configurations.BasePageObject;
import configurations.TestRule;
import io.github.bonigarcia.wdm.WebDriverManager;

import static resources.UrlVariables.*;

import java.io.IOException;
import java.util.concurrent.TimeUnit;
import resources.UrlVariables;

public class BrowserSettings extends BasePageObject {
	
    public BrowserSettings(WebDriver driver, Logger log) {
		super(driver, log);
	}
	@Test
    public void WebDriverManagerTest() {
        openUrl("http://toolsqa.com");
    }
    @Before
    public void startTest() throws IOException {
    	WebDriverManager.chromedriver().setup();
        
        //Create a instance of your web driver - chrome
    	WebDriver driver = new ChromeDriver();
	    TestRule.initiTest(new UrlVariables().BASE_URL);
    }


}
