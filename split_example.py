#my_string="a man, a plan, a canal, panama!"
my_string="2018-02-27 09:48:55.296889,b'$GPGGA,164902.000,4042.7518,N,11159.0984,W,1,07,1.5,1289.2,M,-16.5,M,,0000*5B\r\n'"
print (my_string)
my_split=my_string.split(",")
#print (my_split)
#print ()
print ("-----------------")
for x in range (len(my_split)):
    print (x,my_split[x])

decimal_latitude=int(my_split[3][0:2])+float(my_split[3][2:])/60
if my_split[4]=="S":
   my_split[4]="N"
   decimal_latitude=decimal_latitude*-1

decimal_longitude=int(my_split[5][0:3])+float(my_split[5][3:])/60
if my_split[6]=="W":
    my_split[6]="E"
    decimal_longitude=decimal_longitude*-1

elev_ft=float(my_split[10])*100/2.54/12

print ("decimal_latitude          = "+str(decimal_latitude)+chr(176)+my_split[4])
print ("decimal_longitude         = "+str(decimal_longitude)+chr(176)+my_split[6])
print ("elevation above sea level = "+str(my_split[10])+str(my_split[11]).lower()+" or "+str(round(elev_ft,1))+"ft")
print ()
print ("format for Google Maps    = "+str(round(decimal_latitude,4))+","+str(round(decimal_longitude,4)))
