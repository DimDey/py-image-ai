from src.classes.types import *
amenity_list = {}


def initTypes():
    addType('place_of_worship', PlaceOfWorshipType)
    addType('pharmacy', PharmacyType)
    addType('bank', BankType)
    addType('townhall', TownhallType)
    addType('cafe', CafeType)
    addType('parking', ParkingType)
    addType('hospital', HospitalType)
    addType('university', UniversityType)
    addType('public_building', UniversityType)
    pass


def parseData(building_data, insert_into):
    build_type = building_data.get('amenity')
    type_parser = getType(build_type)

    if type_parser:
        return type_parser.parseData(building_data, insert_into)
    else:
        print(build_type)
        return []


def addType(amenity_name, amenity_class):
    amenity_list[amenity_name] = amenity_class
    pass


def getType(amenity_name):
    if amenity_name in amenity_list:
        return amenity_list[amenity_name]

initTypes()
