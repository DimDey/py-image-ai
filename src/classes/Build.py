from src.classes.TypeManager import parseData


class Build:
    def __init__(self, entity):
        way_tags = entity.tags
        self.nodes = entity.nodes
        self.name = way_tags.get('name:ru') or way_tags.get('name') or ''
        self.levels = way_tags.get('building:levels') or 3
        self.type = way_tags.get('building')
        self.color = 'gray'
        self.line_width = 3
        self.z_order = 1
        self.filled = True
        self.dotted = False

        if not self.type:
            self.color = 'black'
            self.line_width = 2
            self.z_order = 2
            self.filled = False

        self.address = {
            "city": way_tags.get("addr:city") or '',
            "street": way_tags.get("addr:street") or '',
            "house_number": way_tags.get("addr:housenumber") or ''
        }
        self.landuse = way_tags.get('landuse') or None
        self.natural = way_tags.get('natural') or None
        self.width = way_tags.get('width') or None

        if way_tags.get('amenity'):
            parseData(way_tags, self)
