# coding: utf-8

def urler(str):
    try:
        link, params = str.split("?", 1)
        path = parse_path(link)
        try:
            req, metka = params.split("#", 1)
            try:
                args = req.split("&")
                return path, args, metka
            except ValueError:
                return path, req, metka
        except ValueError:
            try:
                args = params.split("&")
                return path, args
            except ValueError:
                return path, params
    except ValueError:
        args = []
        if str.count("#") > 0:
            link, metka = str.split("#", 1)
        else:
            link = str
            metka = ""
        path = parse_path(link)
        return path, args, metka


def parse_path(link):
    link = link.split("/")[3:]
    path = ""
    for i in link:
        path += i
    return path
