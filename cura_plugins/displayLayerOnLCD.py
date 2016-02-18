#Name: Display Layer on LCD/
#Info: Display Layer on LCD
#Depend: GCode
#Type: postprocess


#TODO read the file line by line instead
# Read the file into the lines variable



with open(filename, "r") as r:
    lines = r.readlines()


addedlines = []
last_layer = 0

with open(filename, "w") as f:
    
    line = 0
    for line in lines:
        f.write(line)
        if line.find(";LAYER") == 0:
            alb = line.split(':')
	    addline = ';something went wrong'
	    if len(alb) >1:
                layerNum = alb[1]
		last_layer = layerNum
		addline = 'M117 Layer %s...\n' % layerNum
		line++
		addedlines.append(line)

	    f.write(addline)
        line++

#TODO add the total layers, display fraction complete.

with open(filename, "w") as f:
    line = 0
    for line in lines:
        if line in addedlines:
		line += " of %s" % last_layer
	f.write(line)
