import metacritic_types
def get_name(result_element):
    result_element.find("h3", {"class": metacritic_types.TITLE}).find('a').text.strip()

