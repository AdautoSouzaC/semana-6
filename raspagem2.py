from requests_html import HTMLSession
url = 'http://raspagem.herokuapp.com/'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.stretched-link")
noticias = []
for link in links:
   url = 'http://raspagem.herokuapp.com{}'.format(link.attrs['href'])
   resposta = sessao.get(url)
   infos = resposta.html.find('.blog-post-meta span')
   noticia = {
      'titulo':resposta.html.find('h1', first=True).text,
      'data': infos[0].text,
      'tags': infos[1].text,
      'texto': resposta.html.find('.post-text', first=True).text,

   }
   noticia.append(noticia)
print(noticias)