package saucedemo

import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject

import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.checkpoint.Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling
import com.kms.katalon.core.testcase.TestCase
import com.kms.katalon.core.testdata.TestData
import com.kms.katalon.core.testobject.TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

import internal.GlobalVariable

public class logintest {
	@Keyword
	public void logtest() {
		WebUI.navigateToUrl('https://www.saucedemo.com/')

		WebUI.callTestCase(findTestCase('Pages/1. login/Verify Element Login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input username'), [('username') : 'standard_user'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password'), [('password') : 'secret_sauce'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/2. product/Verify Element product page'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/verify element footer'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.navigateToUrl('https://www.saucedemo.com/')

		WebUI.callTestCase(findTestCase('Pages/1. login/Verify Element Login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input username'), [('username') : 'standard_user'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password - incorrect'), [('notpassword') : 'swaglabs'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Username and password do not match any user in this service'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()

		WebUI.callTestCase(findTestCase('Pages/1. login/input username'), [('username') : 'standard_user'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password - incorrect'), [('notpassword') : ''], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Password is required'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()

		WebUI.callTestCase(findTestCase('Pages/1. login/Verify Element Login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input username - incorrect'), [('notusername') : ''], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password'), [('password') : 'secret_sauce'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Username is required'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()

		WebUI.callTestCase(findTestCase('Pages/1. login/input username - incorrect'), [('notusername') : 'swaglabs'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password'), [('password') : 'secret_sauce'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Username and password do not match any user in this service'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()

		WebUI.callTestCase(findTestCase('Pages/1. login/Verify Element Login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input username - incorrect'), [('notusername') : 'swag'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password - incorrect'), [('notpassword') : 'labs'], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Username and password do not match any user in this service'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()

		WebUI.callTestCase(findTestCase('Pages/1. login/input username - incorrect'), [('notusername') : ''], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/input password - incorrect'), [('notpassword') : ''], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/click button login'), [:], FailureHandling.STOP_ON_FAILURE)

		WebUI.callTestCase(findTestCase('Pages/1. login/read error message'), [('expected') : 'Epic sadface: Username is required'],
		FailureHandling.STOP_ON_FAILURE)

		WebUI.refresh()
	}
}