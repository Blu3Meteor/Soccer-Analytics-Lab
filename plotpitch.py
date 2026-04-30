import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Create figure
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

# Pitch Outline & Centre Line
plt.plot([0,0],[0,90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")
plt.plot([65,65],[0,90], color="white")
plt.fill([0,0,130,130],[0,90,90,0],color="green",alpha=0.5)

# Left Penalty Area
plt.plot([16.5,16.5],[65,25],color="white")
plt.plot([0,16.5],[65,65],color="white")
plt.plot([16.5,0],[25,25],color="white")

# Centre Circle/Spot
centreCircle = plt.Circle((65,45),9.15,fill=False, color="white")
centreSpot = plt.Circle((65,45),0.8, color="white")
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)

# Right Penalty Area
plt.plot([113.5,113.5],[65,25],color="white")
plt.plot([130,113.5],[65,65],color="white")
plt.plot([113.5,130],[25,25],color="white")

# Left 6-yard Box
plt.plot([5.5,5.5],[54,36],color="white")
plt.plot([0,5.5],[54,54],color="white")
plt.plot([5.5,0],[36,36],color="white")

# Right 6-yard Box
plt.plot([124.5,124.5],[54,36],color="white")   
plt.plot([130,124.5],[54,54],color="white")
plt.plot([124.5,130],[36,36],color="white")

# Left Penalty Spot
leftPenSpot = plt.Circle((11,45),0.8, color="white")
ax.add_patch(leftPenSpot)

# Right Penalty Spot
rightPenSpot = plt.Circle((119,45),0.8, color="white")
ax.add_patch(rightPenSpot)

# Create Arc and add it to our plot
leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="white")
rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="white")

ax.add_patch(leftArc)
ax.add_patch(rightArc)

# Left Goal
plt.plot([0,0],[41.5,48.5],color="red")
# Right Goal
plt.plot([130,130],[41.5,48.5],color="red")

# Top Left Corner
corner1 = Arc((0,90),height=4,width=4,angle=0,theta1=270,theta2=360,color="white")
# Top Right Corner
corner2 = Arc((130,90),height=4,width=4,angle=0,theta1=180,theta2=270,color="white")
# Bottom Left Corner
corner3 = Arc((0,0),height=4,width=4,angle=0,theta1=0,theta2=90,color="white")
# Bottom Right Corner
corner4 = Arc((130,0),height=4,width=4,angle=0,theta1=90,theta2=180,color="white")
ax.add_patch(corner1)
ax.add_patch(corner2)
ax.add_patch(corner3)
ax.add_patch(corner4)

plt.axis('off')
plt.show()