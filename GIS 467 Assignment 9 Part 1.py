"""
1.
Using the fire perimeters (2008) shapefile, use a SearchCursor to find:
The name of the biggest fire
The name of the smallest fire
Which agency dealt with the most fires, and how many

2.
Using the States file geodatabase feature class:
 Add a new field to store population density
Use an UpdateCursor to calculate the population density using the shape area geometry token and the population field
"""
import arcpy

fires = r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 9 - fixed\Fire_Perimeters_2008\Fire_Perimeters_2008.shp"

cursor = arcpy.da.SearchCursor(fires,['FIRE_NAME','SHAPE_AREA','AGENCY'])

min_fire = float("+inf")
max_fire = float("-inf")

max_agency = float("-inf")
agencies = []

for fireName, area, agency in cursor:
    agencies.append(agency)      
    if(area > max_fire):
        max_fire = area
        bigName = fireName
    elif(area<min_fire):
        min_fire = area
        smallName = fireName
    #print("The {} fire was {} square meters large.".format(fireName,area)) #(prints all fires)

for agency in agencies:
    if(agencies.count(agency) > max_agency):
        bigAgency = agency
        max_agency = agencies.count(agency)
        
print("The {} fire was {} square meters large.".format(bigName, max_fire))
print("The {} fire was {} square meters small.".format(smallName, min_fire))
print(f"The {bigAgency} agency dealt with {agencies.count(bigAgency)} fires")