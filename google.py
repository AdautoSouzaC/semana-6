from requests_html import HTMLSession
url = 'https://www.google.com/'
sessao = HTMLSession()
resposta = sessao.get(url)
print(resposta.text)
print(resposta.status_code)