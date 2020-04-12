package configurations;

import java.util.List;

import org.apache.logging.log4j.Logger;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class BasePageObject {
	protected WebDriver driver = TestRule.getDriver();
	protected Logger log;

	public BasePageObject(WebDriver driver, Logger log) {
		this.driver = driver;
		this.log = log;
	}

	/** Abrir a pagina de um URL */
	protected void openUrl(String url) {
		driver.get(url);
	}
	
	/** Ache um elemento pelo locator */
	protected WebElement find(By locator) {
		return driver.findElement(locator);
	}

	/** Ache todos os elementos pelo locator */
	protected List<WebElement> findAll(By locator) {
		return driver.findElements(locator);
	}

	/** Clicar no elemento quando aparecer(ficar visivel) */
	protected void click(By locator) {
		waitForVisibilityOf(locator, 5);
		find(locator).click();
	}

	/** digitar texto no locator */
	protected void type(String text, By locator) {
		waitForVisibilityOf(locator, 5);
		find(locator).sendKeys(text);
	}
	
	/**
	 * Espera X segundos por elemento "locator" até ficar visível na página
	 */
	protected void waitForVisibilityOf(By locator, Integer... timeOutInSeconds) {
		int attempts = 0;
		while (attempts < 2) {
			try {
				waitFor(ExpectedConditions.visibilityOfElementLocated(locator),
						(timeOutInSeconds.length > 0 ? timeOutInSeconds[0] : null));
				break;
			} catch (StaleElementReferenceException e) {
			}
			attempts++;
		}
	}

	/**
	 * Espera por uma ExpectedCondition por tempo determinado ou 30s
	 */
	private void waitFor(ExpectedCondition<WebElement> condition, Integer timeOutInSeconds) {
		timeOutInSeconds = timeOutInSeconds != null ? timeOutInSeconds : 30;
		WebDriverWait wait = new WebDriverWait(driver, timeOutInSeconds);
		wait.until(condition);
	}
}
