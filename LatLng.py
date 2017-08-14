import json

class LatLng(object):
    # Create a point object
    
    def __init__(self, obj1=None, obj2=None, noWrap=False):

        self.latitude = 0  # Latitude
        self.longitude = 0  # Longitude
        if ((isinstance(obj1, int) or isinstance(obj1, float)) and 
            (isinstance(obj2, int) or isinstance(obj2, float))):
            self.latitude = obj1  # Latitude
            self.longitude = obj2  # Longitude
        else:
            raise ValueError("Invalid initializers")
            
        if self.latitude < -90:
            self.latitude = -90
        if self.latitude > 90:
            self.latitude = 90

        # allow wrapped longitude
        if noWrap == False:
            self.longitude %= 360
            if 180 < self.longitude < 360:
                self.longitude = (self.longitude % 180) - 180
                       
    def lat(self):
        return self.latitude
    
    def lng(self):
        return self.longitude
    
    def toJSON(self):
        myCoord = {}
        myCoord["lat"] = self.latitude
        myCoord["lng"] = self.longitude
        return json.dumps(myCoord)

    def toString(self):
        return "latitude=" + str(self.latitude) + ", longitude=" + str(self.longitude)

    def toUrlValue(self):
        return "" + str(round(self.latitude,6)) + "," + str(round(self.longitude,6))
