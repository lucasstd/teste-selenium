package configurations;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;


public class TestRule {
	private static WebDriver driver;
	private static String activeAutomation;

	public static void initiTest(String env) {

		openApplicationChrome(env);

	}

	public static void afterCenario() {
		if (driver != null) {
			driver.close();
			driver.quit();
			driver = null;
		}
	}

	public static WebDriver getDriver() {
		return driver;
	}

	public TestRule() {
		super();
	}

	public static String getActiveAutomation() {
		return activeAutomation;
	}

	public static void openApplicationChrome(String url) {

		WebDriverManager.chromedriver().setup();
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
		driver.manage().window().maximize();
		driver.navigate().to(url);
	}

}
