from selenium import webdriver
import time
import schedule

def get_flight_price():
    # Inicializando o navegador
    browser = webdriver.Chrome()

    # URL do voo
    url = "https://www.google.com/travel/flights/search?tfs=CBwQAhojEgoyMDI1LTExLTAxagcIARIDR1JVcgwIAxIIL20vMDZjNjIaIxIKMjAyNS0xMS0xMmoMCAMSCC9tLzA2YzYycgcIARIDR1JVQAFIAXABggELCP___________wGYAQE"
    browser.get(url)

    # Pegando o preço da página
    price = browser.find_element("class name", "jLMuyc").text
    time.sleep(5)

    # Salvando o preço no arquivo
    with open("price.txt", "w") as price_archive:
        price_archive.write(price)

    # Fechar o navegador após a execução
    browser.quit()

# Executando a função imediatamente
get_flight_price()

# Agendando a execução da função a cada 2 semanas
schedule.every(2).weeks.do(get_flight_price)

# Loop para rodar o agendador
while True:
    schedule.run_pending()
    time.sleep(60 * 60 * 24 * 7)  # Esperar 1 semana (em segundos)
