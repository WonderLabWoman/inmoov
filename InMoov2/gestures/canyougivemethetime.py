
def canyougivemethetime():
  inMoov.startedGesture()
  inMoov.mouth.speak("sure")
  #inMoov.mouth.speak(u"конечно")
  fullspeed()
  inMoov.setHandVelocity("left", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  inMoov.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  inMoov.setArmVelocity("right", 59, 59, 59, 43.0)
  inMoov.setArmVelocity("left", 59, 59, 59, 43.0)
  inMoov.setHeadVelocity(31.0, 31.0)
  #1
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",47,86,41,14)
  inMoov.moveArm("right",5,82,28,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",20,40,40,30,30,72)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #2
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",47,86,41,14)
  inMoov.moveArm("right",60,82,28,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #3
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",47,86,41,14)
  inMoov.moveArm("right",67,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #4
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",14,86,55,14)
  inMoov.moveArm("right",67,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #5
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",14,71,62,14)
  inMoov.moveArm("right",67,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #6
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",20,66,66,14)
  inMoov.moveArm("right",73,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(1)
  #7
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",23,66,66,14)
  inMoov.moveArm("right",78,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(2)
  #8
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",23,60,66,14)
  inMoov.moveArm("right",78,40,47,15)
  inMoov.moveHand("left",180,180,180,180,180,119)
  inMoov.moveHand("right",138,40,180,145,139,156)
  inMoov.moveTorso(90,90,90)
  sleep(2)
  #9
  inMoov.mouth.speak("here can you see it yourself")
  #inMoov.mouth.speak(u"Здесь вы можете сами это увидеть")
  inMoov.moveHead(20,100,85,85,65)
  inMoov.moveArm("left",25,120,41,31)
  inMoov.moveArm("right",5,82,28,15)
  inMoov.moveHand("left",180,180,180,180,180,35)
  inMoov.moveHand("right",20,40,40,30,30,72)
  inMoov.moveTorso(90,90,90)
  sleep(3)
  inMoov.finishedGesture()
  relax()
   