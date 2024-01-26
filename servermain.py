from DRCF import *
default= posj(-0.0, 0.0, 0.0, 0.0, -0.0, 0.0)
Home = posj(82.9, 15.7, -122.5, 2.1, -74.1, 52.1)
wpa = posj(120.0, 4.7, -82.9, -2.1, -108.9, -101.4)

#movel(, v=100, a=100)
# wait(0.5), v=100, a=100)
stud1= posj(124.8, -6.1, -111.5, -0.5, -61.8, 8.3)
stud1x= posx(209.8, -312.1, 185.4, 131.0, 177.4, 15.1)
stud1top= posx(210.0, -304.4, 350.0, 86.0, -179.3, -30.6)
#posj(122.0, -3.2, -108.8, -4.5, -69.4, 7.1)
#posx(215.2, -311.7, 186.9, 150.8, 176.6, 35.3)

stud2 = posj(124.3, -11.9, -111.0, -3.2, -58.8, 9.9)
stud2x = posx(214.3, -334.4, 189.2, 146.7, 175.8, 27.7)
stud2top = posx(214.3, -334.4, 350.0, 146.7, 175.8, 27.7)

stud3 = posj(121.2, -13.4, -107.2, -1.8, -61.4, 5.5)
stud3x = posx(213.1, -356.4, 188.0, 137.5, 174.8, 20.7)
stud3top = posx(213.1, -356.4, 350.0, 137.5, 174.8, 20.7)

stud4 = posj(120.0, -16.8, -105.4, -2.7, -59.2, -0.0)
stud4x = posx(207.6, -371.4, 186.5, 151.6, 177.5, 32.4)
stud4top = 

stud5 = posj(118.7, -17.4, -101.2, -3.3, -62.7, 1.3)
stud5x = posx(209.8, -392.9, 188.6, 150.4, 175.9, 31.5)
stud5top = posx(209.8, -392.9, 350.0, 150.4, 175.9, 31.5)

############################################################################################################### 1

# turn it off
set_digital_output(2, 1)
wait(0.1)
# for safety measure
set_digital_output(1, 0)
set_digital_output(2, 0)
wait(0.5)
movej(stud1, v=100, a=100)# top of the stud 1
movel(stud1x, v=100, a=100) #grab the stud 1
set_digital_output(1, 1)
wait(1)
movel(stud1top, 100, 100)
#movej(posj(122.0, -3.2, -108.8, -4.5, -69.4, 7.1), 40, 100) # testpost one

# movel(posx(222.6, -311.4, 189.5, 5.8, -175.8, -117.4), v=100, a=100)

#in front of machine stud

movej(posj(147.8, -14.2, -76.4, 0.1, -93.6, 23.8), v=80, a=100) # halfway
movej(posj(158.0, -44.6, -32.1, -1.9, -104.8, 34.1), v=80, a=100) # above
movel(posx(596.4, -249.3, 376.8, 163.5, 176.5, 40.3), v=100, a=100) #release stud
set_digital_output(1, 0)
movel(posx(593.1, -244.0, 404.0, 29.4, -177.6, -94.1), v=100, a=100) # above
wait(1)
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
#in front
movej(wpa, v=100, a=100)


#alpha
movej(posj(99.7, -41.2, -42.9, -7.6, -108.5, 67.3), v=80, a=100) # top of speedhex
#movel(posx(81.8, -610.0, 344.0, 118.7, 161.4, 88.5), v=100, a=100)# grab the speedhex
movel(posx(90.8, -608.6, 346.2, 128.4, 161.6, 97.2), v=40, a=100)
set_digital_output(1, 1)
wait(1)
movej(posj(99.7, -41.2, -42.9, -7.6, -108.5, 67.3), v=80, a=100) # top of speedhex
# movej(posj(98.0, -21.5, -75.1, -2.2, -70.3, 68.6), v=80, a=100)  # waypoint 1
movej(wpa, v=100, a=100)

# front of machine speedhex
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex

# movel(posx(589.5, -246.8, 372.1, 103.1, 179.0, 163.4), v=25, a=100) #speedhex release
movel(posx(597.1, -244.4, 375.7, 16.7, -176.6, 76.1), v=100, a=100) # speed hex release
set_digital_output(1, 0)
wait(1)
movel(posx(595.6, -245.7, 372.2, 74.1, 178.9, 134.1), v=100, a=100) # #trick release speedhex
# movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100)
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex
set_digital_output(2, 1)
movej(wpa,  v=100, a=100)

################################################################################################################### 3


############################################################ 2

# turn it off
set_digital_output(2, 1)
# for safety measure
set_digital_output(1, 0)
set_digital_output(2, 0)
wait(0.5)

#grabbing the stud first

movej(stud2, v=70, a=100)# top of the stud
movel(stud2x, v=100, a=100) #grab the stud
set_digital_output(1, 1)
wait(1)
movel(stud2top, v=100, a=100) # top of the stud

#in front of machine stud

movej(posj(147.8, -14.2, -76.4, 0.1, -93.6, 23.8), v=80, a=100) # halfway
movej(posj(158.0, -44.6, -32.1, -1.9, -104.8, 34.1), v=80, a=100) # above
movel(posx(596.4, -249.3, 376.8, 163.5, 176.5, 40.3), v=100, a=100) #release stud
set_digital_output(1, 0)
movel(posx(593.1, -244.0, 404.0, 29.4, -177.6, -94.1), v=100, a=100) # above
wait(1)
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
#in front
movej(wpa, v=100, a=100)

# BETA
movej(posj(100.2, -46.3, -35.9, -1.9, -121.6, -56.6), v=80, a=100)  # top of speedhex
# movel(posx(103.9, -599.2, 371.7, 104.1, 156.1, -52.0), v=100, a=100) # top of the speedhex
#movel(posx(105.2, -579.5, 357.5, 107.8, 160.4, -40.5), v=100, a=100) # grabbing the speedhex
movel(posx(111.9, -593.1, 344.8, 111.7, 153.3, -36.4), v=100, a=100)
set_digital_output(1, 1)
wait(1)
movel(posx(125.5, -581.4, 388.7, 117.4, 160.8, -32.3), v=100, a=100)  # top of speedhex
movej(wpa, v=100, a=100)

# front of machine speedhex
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex
movel(posx(591.1, -248.6, 375.2, 95.4, 177.4, 155.8), v=25, a=100)
set_digital_output(1, 0)
wait(1)
movel(posx(595.6, -245.7, 372.2, 74.1, 178.9, 134.1), v=100, a=100) # #trick release speedhex
movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100) # to of it maybe ?
set_digital_output(2, 1)
movej(wpa,  v=100, a=100)
########################################################################################################## 3

# turn it off
set_digital_output(2, 1)
wait(0.1)
# for safety measure
set_digital_output(1, 0)
set_digital_output(2, 0)

wait(0.5)
movej(stud3, 100, 100)
movel(stud3x, v=70, a=100)# top of the stud 3
set_digital_output(1, 1)
movel(stud3top, v=100, a=100) #grab the stud 3
wait(1)
movel(stud3top, v=100, a=100) # top of the stud

#front of the machine stud
movej(posj(147.8, -14.2, -76.4, 0.1, -93.6, 23.8), v=80, a=100) # halfway
movej(posj(158.0, -44.6, -32.1, -1.9, -104.8, 34.1), v=80, a=100) # above
movel(posx(596.4, -249.3, 376.8, 163.5, 176.5, 40.3), v=80, a=100) #release stud
set_digital_output(1, 0)
movel(posx(593.1, -244.0, 404.0, 29.4, -177.6, -94.1), v=100, a=100) # above
wait(1)
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
#in front
movej(wpa, v=100, a=100)


#charlie
#top of charlie

movej(posj(97.9, -36.9, -48.1, -7.0, -108.7, 189.2), v=80, a=100) # top of the hex
movel(posx(72.9, -577.3, 360.8, 123.4, 157.8, -140.4), v=100, a=100) # grabbing
movel(posx(69.6, -576.4, 360.2, 125.0, 156.3, -138.4), v=100, a=100) # xtra step to move it
set_digital_output(1, 1)
movej(posj(97.5, -23.6, -65.0, -8.3, -90.8, 182.2), v=80, a=100)  # grabbing it safely of speedhex
movej(posj(101.0, -13.5, -73.8, -8.4, -118.5, 182.2), v=80, a=100)  #waypoint 3
movej(posj(151.3, -17.8, -70.0, 1.5, -89.4, 217.4), v=80, a=100) # front of machine
movej(posj(158.5, -43.8, -35.9, -2.4, -101.7, 215.9), v=80, a=100) # latest top
movel(posx(597.1, -244.4, 375.7, 16.7, -176.6, 76.1), v=100, a=100) # speed hex release
set_digital_output(1, 0)
wait(1)
movel(posx(595.6, -245.7, 372.2, 74.1, 178.9, 134.1), v=100, a=100) # #trick release speedhex
movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100) # above
set_digital_output(2, 1)
movej(wpa,  v=100, a=100)

################################################################################################################### 4

# turn it off
set_digital_output(2, 1)
wait(0.1)
# for safety measure
set_digital_output(1, 0)
set_digital_output(2, 0)
wait(0.5)
movej(stud4, v=100, a=100)# top of the stud 1
movel(stud4x, v=100, a=100) #grab the stud 1
set_digital_output(1, 1)
wait(1)
movel(stud4top, 100, 100)
#movej(posj(122.0, -3.2, -108.8, -4.5, -69.4, 7.1), 40, 100) # testpost one

# movel(posx(222.6, -311.4, 189.5, 5.8, -175.8, -117.4), v=100, a=100)

#in front of machine stud

movej(posj(147.8, -14.2, -76.4, 0.1, -93.6, 23.8), v=80, a=100) # halfway
movej(posj(158.0, -44.6, -32.1, -1.9, -104.8, 34.1), v=80, a=100) # above
movel(posx(596.4, -249.3, 376.8, 163.5, 176.5, 40.3), v=100, a=100) #release stud
set_digital_output(1, 0)
movel(posx(593.1, -244.0, 404.0, 29.4, -177.6, -94.1), v=100, a=100) # above
wait(1)
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
#in front
movej(wpa, v=100, a=100)


#alpha
movej(posj(99.7, -41.2, -42.9, -7.6, -108.5, 67.3), v=80, a=100) # top of speedhex
#movel(posx(81.8, -610.0, 344.0, 118.7, 161.4, 88.5), v=100, a=100)# grab the speedhex
movel(posx(90.8, -608.6, 346.2, 128.4, 161.6, 97.2), v=40, a=100)
set_digital_output(1, 1)
wait(1)
movej(posj(99.7, -41.2, -42.9, -7.6, -108.5, 67.3), v=80, a=100) # top of speedhex
# movej(posj(98.0, -21.5, -75.1, -2.2, -70.3, 68.6), v=80, a=100)  # waypoint 1
movej(wpa, v=100, a=100)

# front of machine speedhex
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex

# movel(posx(589.5, -246.8, 372.1, 103.1, 179.0, 163.4), v=25, a=100) #speedhex release
movel(posx(597.1, -244.4, 375.7, 16.7, -176.6, 76.1), v=100, a=100) # speed hex release
set_digital_output(1, 0)
wait(1)
movel(posx(595.6, -245.7, 372.2, 74.1, 178.9, 134.1), v=100, a=100) # #trick release speedhex
# movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100)
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex
set_digital_output(2, 1)
movej(wpa,  v=100, a=100)

################################################################################################################### 5


# turn it off
set_digital_output(2, 1)
# for safety measure
set_digital_output(1, 0)
set_digital_output(2, 0)
wait(0.5)

#grabbing the stud first

movej(stud5, v=70, a=100)# top of the stud
movel(stud5x, v=100, a=100) #grab the stud
set_digital_output(1, 1)
wait(1)
movel(stud5top, v=100, a=100) # top of the stud

#in front of machine stud

movej(posj(147.8, -14.2, -76.4, 0.1, -93.6, 23.8), v=80, a=100) # halfway
movej(posj(158.0, -44.6, -32.1, -1.9, -104.8, 34.1), v=80, a=100) # above
movel(posx(596.4, -249.3, 376.8, 163.5, 176.5, 40.3), v=100, a=100) #release stud
set_digital_output(1, 0)
movel(posx(593.1, -244.0, 404.0, 29.4, -177.6, -94.1), v=100, a=100) # above
wait(1)
movel(posx(597.4, -250.3, 427.0, 135.0, 176.3, 18.2), v=100, a=100) # the top of the machine
#in front
movej(wpa, v=100, a=100)

# BETA
movej(posj(100.2, -46.3, -35.9, -1.9, -121.6, -56.6), v=80, a=100)  # top of speedhex
# movel(posx(103.9, -599.2, 371.7, 104.1, 156.1, -52.0), v=100, a=100) # top of the speedhex
#movel(posx(105.2, -579.5, 357.5, 107.8, 160.4, -40.5), v=100, a=100) # grabbing the speedhex
movel(posx(111.9, -593.1, 344.8, 111.7, 153.3, -36.4), v=100, a=100)
set_digital_output(1, 1)
wait(1)
movel(posx(125.5, -581.4, 388.7, 117.4, 160.8, -32.3), v=100, a=100)  # top of speedhex
movej(wpa, v=100, a=100)

# front of machine speedhex
movej(posj(158.3, -43.0, -29.0, -1.5, -106.2, -142.8), v=80, a=100) #top of the machine speedhex
movel(posx(591.1, -248.6, 375.2, 95.4, 177.4, 155.8), v=25, a=100)
set_digital_output(1, 0)
wait(1)
movel(posx(595.6, -245.7, 372.2, 74.1, 178.9, 134.1), v=100, a=100) # #trick release speedhex
movel(posx(588.3, -243.4, 415.2, 168.0, -179.1, -132.1), v=100, a=100) # to of it maybe ?
set_digital_output(2, 1)
movej(wpa,  v=100, a=100)
