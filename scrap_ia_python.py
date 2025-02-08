from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openai import OpenAI

URL_TARGET = "https://example.com"  # URL de la página a scrapear
output_file = "datos_scrapeados.txt"  # Archivo donde se guardarán los datos scrapeados
response_file = "respuesta_chatgpt.txt"  # Archivo con la respuesta de ChatGPT

OPENAI_API_KEY = "TU_API_AQUI"
client = OpenAI(api_key=OPENAI_API_KEY)

# conf Selenium con ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  
options.add_argument("--headless")  
options.add_argument("--ignore-certificate-errors")  
driver = webdriver.Chrome(options=options)

try:

    with open(output_file, "w") as f:
        f.write("Datos scrapeados:\n\n")

    print("Accediendo a la página objetivo...")
    driver.get(URL_TARGET)

    print("Esperando que la página cargue...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    print("Extrayendo datos...")
    titulos = driver.find_elements(By.TAG_NAME, "h1")  # Ejemplo: extraer todos los <h1>
    parrafos = driver.find_elements(By.TAG_NAME, "p")  # Ejemplo: extraer todos los <p>

    # guardar los datos en el archivo de salida
    with open(output_file, "a") as f:
        f.write("Títulos encontrados:\n")
        for titulo in titulos:
            f.write(titulo.text + "\n")

        f.write("\nPárrafos encontrados:\n")
        for parrafo in parrafos:
            f.write(parrafo.text + "\n")

    print(f"\nDatos extraídos guardados en '{output_file}'.")

    print("\nLeyendo el archivo scrapeado...")
    with open(output_file, "r") as file:
        contenido = file.read()

    # dividir el contenido
    def dividir_contenido(contenido, max_chars=2000):
        """Divide el contenido en partes de longitud máxima."""
        partes = []
        while contenido:
            partes.append(contenido[:max_chars])
            contenido = contenido[max_chars:]
        return partes

    partes = dividir_contenido(contenido, max_chars=2000)

    todas_las_respuestas = []

    # procesar cada parte con OpenAI
    for idx, parte in enumerate(partes, start=1):
        print(f"\nProcesando parte {idx} de {len(partes)}...")
        try:
            # Enviar la solicitud a OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Modelo de OpenAI
                messages=[
                    {"role": "system", "content": "Eres un asistente útil."},
                    {"role": "user", "content": f"Resume este texto:\n{parte}"}
                ]
            )
            # Obtener la respuesta del modelo
            respuesta_gpt = response.choices[0].message.content
            todas_las_respuestas.append(f"Parte {idx}:\n{respuesta_gpt}\n")
        except Exception as e:
            print(f"Error al procesar la parte {idx}: {e}")
            todas_las_respuestas.append(f"Parte {idx}:\nError al procesar esta parte.\n")

    with open(response_file, "w") as f:
        f.write("Respuestas de ChatGPT:\n\n")
        f.writelines(todas_las_respuestas)

    print(f"\nTodas las respuestas guardadas en '{response_file}'.")

except Exception as e:
    print(f"Error general: {e}")

finally:
    
    driver.quit()