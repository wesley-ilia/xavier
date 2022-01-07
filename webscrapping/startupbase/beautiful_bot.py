from bs4 import BeautifulSoup


# All the fields of localization
def get_cidade_and_estado(soup: BeautifulSoup):
    try:
        localizacao = soup.find(class_="publ-card startup-addrr__grow")
        localizacao = localizacao.find_all(class_="publ-text")
        cidade_estado = localizacao[-1].text
    except BaseException:
        cidade_estado = ''
    return cidade_estado


def get_segmento_tamanho_and_etc(soup: BeautifulSoup):
    try:
        side_box = soup.find('app-card-body')
        # URL   Segmento  Fundacao  Tamanho  Atualizacao
        # s[0]  s[1]      s[2]      s[3]     s[4]
        side_box = side_box.find_all('article')
    except BaseException:
        side_box = ['', '', '', '', '']
    return side_box


def get_social_media(soup):
    redes = list()
    try:
        links = soup.find(class_='publ-social')
        if links:
            links = links.find_all('a')
            for link in links:
                redes.append(link['href'])
    except BaseException:
        pass
    return redes

def get_website(soup: BeautifulSoup):
    website = soup.select_one('a[class="publ-channel is-radius3 is-unselectable"]')
    return website['href']

def get_all_infos(body):
    soup = BeautifulSoup(body, "html.parser")

    # Name
    name = soup.find(class_="publ-header__name").text

    # Mercado  Publico  Modelo   Momento
    # box[0]   box[1]   box[2]   box[3]
    top_box = soup.find_all(class_="startup-timely__data")

    estado = get_cidade_and_estado(soup)
    # URL   Segmento  Fundacao  Tamanho  Atualizacao
    # s[0]  s[1]      s[2]      s[3]     s[4]
    side_box = get_segmento_tamanho_and_etc(soup)

    redes = get_social_media(soup)

    website = get_website(soup)

    infos = [
        name, estado,
        top_box[0].text, top_box[1].text, top_box[2].text, top_box[3].text,
        side_box[3].p.text, side_box[1].p.text, redes, website.strip()]

    return infos
