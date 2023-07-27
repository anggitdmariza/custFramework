import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.verifyElementVisible(findTestObject('5. invoice/button_Cancel_c'))

WebUI.verifyElementVisible(findTestObject('5. invoice/button_Finish_c'))

WebUI.verifyElementVisible(findTestObject('5. invoice/desc_c'))

WebUI.verifyElementVisible(findTestObject('5. invoice/label_Payment Information'))

WebUI.verifyElementVisible(findTestObject('5. invoice/label_Price Total'))

WebUI.verifyElementVisible(findTestObject('5. invoice/label_Shipping Information'))

WebUI.verifyElementVisible(findTestObject('5. invoice/name_c'))

WebUI.verifyElementVisible(findTestObject('5. invoice/price_c'))

WebUI.verifyElementVisible(findTestObject('5. invoice/shipping_method'))

WebUI.verifyElementVisible(findTestObject('5. invoice/shopping_id'))

WebUI.verifyElementVisible(findTestObject('5. invoice/total_item'))

WebUI.verifyElementVisible(findTestObject('5. invoice/total_payment'))

WebUI.verifyElementVisible(findTestObject('5. invoice/total_price'))

WebUI.verifyElementVisible(findTestObject('5. invoice/total_Tax'))

