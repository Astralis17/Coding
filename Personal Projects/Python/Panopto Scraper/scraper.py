import aTools
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless') # Run without display

driver = webdriver.Firefox(options=options)
driver.get('https://ioe.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=6d884d89-2188-40fd-838a-b42c013a3d3c')

# Copy HTML
html = driver.page_source
print(html)
with open(aTools.localPath("./log1.html"), "w") as file:
    file.write(html)

driver.quit()
