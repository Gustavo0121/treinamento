import httpx
from bs4 import BeautifulSoup
from pathlib import Path


def get_content(url: str) -> list:
    """Donwload content web."""

    req = httpx.get(url)
    content = req.text
    soup = BeautifulSoup(content, 'html5lib')
    result = soup.select_one('div.corpo_texto_noticia').contents
    result = [line for line in result if line and isinstance(line, str)]
    # print(result)
    return result

def write_content(fout: str, content: list) -> bool:
    soup = BeautifulSoup('', 'html5lib', from_encoding='iso8859-1')
    for line in content:
        p = soup.new_tag('p')
        p.string = line
        soup.html.body.append(p)
    print(soup)
    Path(fout).write_text(soup.text)
    return True


def run():
    """"""
    content = get_content('https://www.diariodasleis.com.br/legislacao/federal/exibe_artigo.php?ifl=203526')
    write_content('dim18320616-001.html', content)



run()