from bs4 import BeautifulSoup


# All the fields of localization
def get_cidade_and_estado(soup: BeautifulSoup):
    try:
        cidade_estado = soup.select(
                'div.publ-card.startup-addrr__grow > p.publ-text')[-1].text
    except IndexError:
        return ''
    return cidade_estado


def get_segmento(soup: BeautifulSoup):
    try:
        segmento = soup.select('p.publ-text.sb-size-10')[1].text
    except IndexError:
        segmento = ''
    return segmento


def get_tamanho(soup: BeautifulSoup):
    try:
        tamanho = soup.select('p.publ-text.sb-size-10')[3].text
    except IndexError:
        tamanho = ''
    return tamanho


def get_social_medias(soup: BeautifulSoup):
    return [link['href'] for link in soup.select(
        'a.publ-social__link.has-text-centered')]


def get_website(soup: BeautifulSoup):
    try:
        website = soup.select_one(
                    'a[class="publ-channel is-radius3 is-unselectable"]'
                )['href']
    except TypeError:
        website = ''
    return website


def get_name(soup: BeautifulSoup):
    try:
        name = soup.select_one('h2.publ-header__name.sb-size-4').text
    except AttributeError:
        name = ''
    return name


def get_mercado(soup: BeautifulSoup):
    try:
        mercado = soup.select(
                'p.startup-timely__data.has-text-weight-semibold.sb-size-6'
                )[0].text
    except IndexError:
        mercado = ''
    return mercado


def get_publico(soup: BeautifulSoup):
    try:
        publico = soup.select(
                'p.startup-timely__data.has-text-weight-semibold.sb-size-6'
                )[1].text
    except IndexError:
        publico = ''
    return publico


def get_modelo(soup: BeautifulSoup):
    try:
        modelo = soup.select(
                'p.startup-timely__data.has-text-weight-semibold.sb-size-6'
                )[2].text
    except IndexError:
        modelo = ''
    return modelo


def get_momento(soup: BeautifulSoup):
    try:
        momento = soup.select(
                'p.startup-timely__data.has-text-weight-semibold.sb-size-6'
                )[3].text
    except IndexError:
        momento = ''
    return momento


def get_all_infos(body) -> list:
    soup = BeautifulSoup(body, "html.parser")
    if soup is None:
        return []

    name = get_name(soup)
    mercado = get_mercado(soup)
    publico = get_publico(soup)
    modelo = get_modelo(soup)
    momento = get_momento(soup)
    estado = get_cidade_and_estado(soup)
    segmento = get_segmento(soup)
    tamanho = get_tamanho(soup)
    redes = get_social_medias(soup)
    website = get_website(soup)

    infos = [
        name, estado,
        mercado, publico, modelo, momento,
        tamanho, segmento, redes, website
        ]

    return infos
