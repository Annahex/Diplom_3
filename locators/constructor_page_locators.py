from selenium.webdriver.common.by import By

CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']//parent::a[@href='/']")
INGREDIENT_LINK = (By.XPATH, ".//a[starts-with(@href,'/ingredient')]")
INGREDIENT_COUNTER = (By.XPATH, ".//p[starts-with(@class,'counter_counter__num')]")
CLOSE_INGREDIENT_MODAL = (By.XPATH, ".//h2[text()='Детали ингредиента']/parent::div/following-sibling::button")
BASKET_ELEMENT = (By.XPATH, ".//ul[starts-with(@class,'BurgerConstructor_basket')]")
CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
ORDER_ID_HEADER = (By.XPATH, ".//h2[starts-with(@class, 'Modal_modal__title')]")
