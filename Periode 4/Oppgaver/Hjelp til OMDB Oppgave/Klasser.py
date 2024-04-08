class SokResultat:
    """ Tar inn en dictionary with the data for this result
        The dictionary tilsvarer json sendt from the API"""
    def __init__(self, data:dict[str, str]):
        self.tittel = data.get("Title")  #bruker get-method for å gjøre det mer robust.
        self.aar = data.get("Year")
        self.id = data.get("imdbID")
        self.poster = data.get("Poster")
        self.type = data.get("Type")

    def __str__(self):
            return f"Title: {self.tittel}, Year:{self.aar}, ID:{self.id}, Type:{self.type}"