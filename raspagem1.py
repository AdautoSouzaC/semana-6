from requests_html import HTMLSession
url = 'http://raspagem.herokuapp.com/'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.stretched-link")
for link in links:
    print(link.attrs['href'])