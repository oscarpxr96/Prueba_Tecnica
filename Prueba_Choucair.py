from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from faker import Faker

class Test_suite(unittest.TestCase):
    def setUp(self):
        # Inicializacion del webdriver
        self.driver = webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")

    def test_MainPage(self):
        #Busqueda efectiva de la pagina en google
        driver = self.driver
        driver.get("http://google.com")
        buscador=driver.find_element_by_name("q")
        buscador.send_keys("https://www.Utest.com")
        buscador.send_keys(Keys.ENTER)
        pagina=driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
        pagina.click()
        time.sleep(2)
        print("Pagina encontrada en google")

    def test_Registro(self):
        fake=Faker()
        driver = self.driver
        driver.get("https://www.Utest.com")
        time.sleep(1)
        Btn_reg=driver.find_element_by_link_text("Join Today").click()

        #Primer Etapa del Registro
        try:
            Cam_FirstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID,"firstName")))
        finally:
            Cam_FirstName.send_keys(fake.name())
        Cam_lastName = driver.find_element_by_id("lastName").send_keys(fake.name())
        Cam_Email = driver.find_element_by_id("email").send_keys(fake.ascii_safe_email())
        opcion_Month = Select(driver.find_element_by_id("birthMonth")).select_by_value("number:2")
        opcion_Day = Select(driver.find_element_by_id("birthDay")).select_by_value("number:2")
        opcion_Year = Select(driver.find_element_by_id("birthYear")).select_by_value("number:1996")
        time.sleep(1)
        Btn_next = driver.find_element_by_xpath("//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[2]/a").click()
        time.sleep(2)

        #Segunda Etapa del Registro
        try:
            Cam_City=WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,"//*[@id='city']")))
        finally:
            Cam_City.send_keys("bogo")
            time.sleep(1)
            Cam_City.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
            Cam_City.send_keys(Keys.ENTER)
            time.sleep(1)
        Cam_Zip=driver.find_element_by_id("zip").send_keys("11111111")
        time.sleep(1)
        Btn_next_device= driver.find_element_by_xpath("//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[2]/div/a/span").click()
        time.sleep(2)

        #Tercera Etapa del registro
        try:
            Cam_MobDev=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='mobile-device']/div[1]/div[2]/div/div[1]/span")))
        finally:
            Cam_MobDev.click()
            opcion_MobDev=driver.find_element_by_xpath("/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/ul/li/div[5]/span/div").click()
            time.sleep(1)
        Cam_Model = driver.find_element_by_xpath("//*[@id='mobile-device']/div[2]/div[2]/div/div[1]/span").click()
        opcion_model=driver.find_element_by_xpath("/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/ul/li/div[23]/span/div").click()
        time.sleep(1)
        Cam_OS = driver.find_element_by_xpath("/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/div[1]/span").click()
        opcion_OS = driver.find_element_by_xpath("/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div[3]/div[2]/div/ul/li/div[25]/span/div").click()
        Btn_LastStep = driver.find_element_by_xpath("//*[@id='regs_container']/div/div[2]/div/div[2]/div/div[2]/div/a/span").click()
        time.sleep(1)

        #Cuarta Etapa del Registro
        Password=driver.find_element_by_xpath("//*[@id='password']").send_keys("PruebaTest123+")
        Conf_Password=driver.find_element_by_xpath("//*[@id='confirmPassword']").send_keys("PruebaTest123+")
        chackmark_1=driver.find_element_by_xpath("//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]").click()
        chackmark_2 =driver.find_element_by_xpath("//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]").click()
        Btn_COmplete=driver.find_element_by_xpath("//*[@id='laddaBtn']/span").click()
        time.sleep(5)
        print("Usuario Registrado")


    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
