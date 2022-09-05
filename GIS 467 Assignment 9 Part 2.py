""""
Using the States file geodatabase feature class:
 Add a new field to store population density
Use an UpdateCursor to calculate the population density using the shape area geometry token and the population field
"""
import arcpy

states_fc = r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 9 - fixed\States.gdb\States"
#add your new field
arcpy.AddField_management(states_fc, "pop_density", "FLOAT") #in_table, field_name, field_type
#create cursor
cursor = arcpy.da.UpdateCursor(states_fc, ['pop_density', 'pop2010', 'SHAPE@AREA'])


for row in cursor:
    try:
        row[0] = float(row[1])/float(row[2])
    except Exception as e:
        print(f"{row} failed due to {e}.") #or acrpy.addMessage / arcpy.addError
    
    cursor.updateRow(row)
    
"""
treesLayer = r"c:\CampusData.gdb\Campus_TreePoints" 
arcpy.AddField_management(treesLayer, "area", "DOUBLE")

with arcpy.da.UpdateCursor(treesLayer, ["TREE_TYPE", "DBH", "area"]) as cursor:
    for row in cursor:
        dbh = row[1]
        radius = (dbh / 3.14) / 2
        row[2] = radius
        cursor.updateRow(row)

"""