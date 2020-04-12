package objectRepository.SimulatorTesting;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class PageObjects {

	WebDriver driver;

	@FindBy(id="valorAplicar")
	WebElement inputValorAplicar;

	@FindBy(id="valorInvestir")
	WebElement inputValorInvestir;

	@FindBy(id="tempo")
	WebElement inputQuantoTempo;
	
	@FindBy(xpath="//*[@id=\"formInvestimento\"]/div[4]/div[2]/div[2]/a")
	WebElement dropNumMeses;
	
	@FindBy(xpath="//*[@id=\"formInvestimento\"]/div[5]/ul/li[2]/button")
	WebElement btnSimular;
	
	@FindBy(xpath="//*[@id=\"formInvestimento\"]/div[1]/input[2]")
	WebElement radioBtnEmpresa;

	public PageObjects(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
	}

	public WebElement inputValorAplicar() {
		return inputValorAplicar;
	}

	public WebElement inputValorInvestir() {
		return inputValorInvestir;
	}
	
	public WebElement inputQuantoTempo() {
		return inputQuantoTempo;
	}
	
	public WebElement dropNumMeses() {
		return dropNumMeses;
	}
	
	public WebElement btnSimular() {
		return btnSimular;
	}

}
