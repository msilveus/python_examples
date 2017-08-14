import json
import math
from LatLng import LatLng

class LatLngBounds:
    # Constructs a rectangle from the points at its south-west and north-east corners.
    
    def __init__(self, obj1=None, obj2=None):

        self.lat1 = 0 # SW corner Latitude
        self.lng1 = 0 # SW corner Longitude
        self.lat2 = 0 # NE corner Latitude
        self.lng2 = 0 # NE corner Longitude
        
        if isinstance(obj1,LatLng):
            self.lat1 = obj1.lat()
            self.lng1 = obj1.lng()
        elif isinstance(obj1, str):
            try:
                myDict = json.loads(obj1)
                self.lat1 = myDict['lat'] # Latitude
                self.lng1 = myDict['lng'] # Longitude
            except Exception as err:
                raise ValueError("SW corner point is Invalid")
        else:
            raise ValueError("SW corner point is Invalid")
            
        if isinstance(obj2,LatLng):
            self.lat2 = obj2.lat()
            self.lng2 = obj2.lng()
        elif isinstance(obj2, str):
            try:
                myDict = json.loads(obj2)
                self.lat2 = myDict['lat'] # Latitude
                self.lng2 = myDict['lng'] # Longitude
            except Exception as err:
                raise ValueError("NE corner point is Invalid")
        else:
            raise ValueError("NE corner point is Invalid")
        
        # confirm coordinates are correct in their orientation
        if self.lat2 < self.lat1:
            # throw error
            raise ValueError("Your coordinates are reversed - SW entry was " + str(self.lat1) + ", " + str(self.lng1) + " and NE was " + str(self.lat2) + ", " + str(self.lng2) )
        
        # check if SW point longitude is left of NE point
        if ((self.lng1 > 0 and self.lng2 > 0) or 
            (self.lng1 < 0 and self.lng2 < 0)):
            if self.lng1 > self.lng2:
                # throw error
                raise ValueError("Your coordinates are reversed - SW entry was " + str(self.lat1) + ", " + str(self.lng1) + " and NE was " + str(self.lat2) + ", " + str(self.lng2) )
        if self.lng1 > 0 and self.lng2 < 0:
            if self.lng1 < self.lng2:
                # throw error
                raise ValueError("Your coordinates are reversed - SW entry was " + str(self.lat1) + ", " + str(self.lng1) + " and NE was " + str(self.lat2) + ", " + str(self.lng2) )
        
    def contains(self, obj):
        inLat = 0
        inLng = 0
        swLat = self.lat1
        swLng = self.lng1
        neLat = self.lat2
        neLng = self.lng2
        # flag to check if crossing dateline
        datelineCrosser = self.lng1 > self.lng2
        try:
            if isinstance(obj,LatLng):
                inLat = obj.lat()
                inLng = obj.lng()
            elif isinstance(obj, str):
                geoPoint = json.loads(obj)
                print(geoPoint)
                inLat = geoPoint['lat'] # Latitude
                inLng = geoPoint['lng'] # Longitude
            else:
                raise ValueError("Argument value is Invalid")
        except Exception as err:
            raise ValueError("Json Argument value is Invalid")
            
        if swLat < inLat < neLat:
            if datelineCrosser == True:
                swdiff = 180 - swLng
                nediff = 180 + neLng
                # check which side of the dateline the point is on
                if inLng < 0:
                    indiff = 180 + inLng
                    chkdiff = nediff
                else:
                    indiff = 180 - inLng
                    chkdiff = nediff

                if (indiff < chkdiff):
                    return True
                else:
                    return False
            else:
                if swLng < inLng < neLng:
                    return True
                else:
                    return False
        else:
            return False
        
    def toString(self):
        return "lat1=" + str(self.lat1) + ", lng1=" + str(self.lng1) + ", lat2=" + str(self.lat2) + ", lng2=" + str(self.lng2)
    
    def toUrlValue(self):
        return str(round(self.lat1,6)) + "," + str(round(self.lng1,6)) + "," + str(round(self.lat2,6)) + "," + str(round(self.lng2,6))
    