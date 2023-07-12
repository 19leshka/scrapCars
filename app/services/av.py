from app.services.service import Service


class AVbyService(Service):
    @staticmethod
    async def parse_items(items: list) -> list:
        cars = []
        for item in items:
            el = {}
            el["id"] = (item.find("a", class_="listing-item__link")["href"]).split("/")[3]
            el["img"] = (item.find("img", class_="lazyload")["data-srcset"]).split()[0]
            el["name"] = item.find("span", class_="link-text").text
            el["price"] = item.find("div", class_="listing-item__priceusd").text
            params = item.find("div", class_="listing-item__params").findChildren("div", recursive=False)
            el["year"] = params[0].text
            el["characteristics"] = f'{params[1].text}, {params[2].find("span").text}'
            el["location"] = item.find("div", class_="listing-item__location").text
            try:
                el["text"] = item.find("div", class_="listing-item__message").findChildren("div", recursive=False)[0].text
            except AttributeError:
                el["text"] = ""
            cars.append(el)
        return cars
