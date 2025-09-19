import pygame, aTools, math

deltaX = 0.01
k = 1
m = 1
gFunc = lambda t: (-k/m)*t
#gFunc = math.sin
x = aTools.Math.fRange(0, 10, deltaX)
xproper = [0,0]
h = [1]
f = [5]
g = [gFunc(0)]

for j, xj in enumerate(x):
        h.append(h[j] + (deltaX * gFunc(f[j])))
        f.append(f[j] + (deltaX * h[j]))
        g.append(gFunc(h[j]))

# print(f"H: {h}")
# print(f"F: {f}")


pygame.init()
windowDimensions = (1080, 640)
window = pygame.display.set_mode(windowDimensions)

offset = 100
graphPlot = tuple([windowDimensions[i]-(offset*2) for i in range(2)])
graphPlotRect = pygame.Rect(offset, offset, graphPlot[0], graphPlot[1])
#scale = (graphPlot[0]/x[-1], graphPlot[1]/f[-1])
xScale = graphPlot[0]/max(x)
if max(h)==0:
        yScale = graphPlot[1]/min(h)/2
else:
        yScale = graphPlot[1]/max(h)/2
def scalePoints(points, NegativeOffset=graphPlot[1]/2):
        p = []
        for j, xj in enumerate(x):
                p.append((
                        offset + (xj * xScale),
                        graphPlotRect.bottom - (points[j] * yScale) - NegativeOffset
                        ))
        return p

divisorLength = 5
ylineCount = 20
xlineCount = 40
yDivisors = [((offset - divisorLength/2, offset + i*graphPlot[1]/ylineCount), (offset + divisorLength/2, offset + i*graphPlot[1]/ylineCount)) for i in range(ylineCount)]
xDivisors = [((offset + i*graphPlot[0]/xlineCount, windowDimensions[1] - offset -graphPlot[1]/2 - divisorLength/2), (offset + i*graphPlot[0]/xlineCount, windowDimensions[1] - offset -graphPlot[1]/2 + divisorLength/2)) for i in range(xlineCount)]
divisorLines = xDivisors + yDivisors

hPoints = scalePoints(h)
fPoints = scalePoints(f)
gPoints = scalePoints(g)
xPoints = scalePoints(x)
#xproperPoints = scalePoints(xproper)

lines = False

window.fill("white")
pygame.draw.rect(window, "black", graphPlotRect, 1)
pygame.draw.line(window, "black", graphPlotRect.midleft, graphPlotRect.midright)


pygame.draw.lines(window, "red", False, fPoints, 2)
pygame.draw.lines(window, "yellow", False, hPoints, 2)

# pygame.draw.lines(window, "green", False, gPoints, 2)
#pygame.draw.lines(window, "orange", False, xproperPoints, 3)
#for point in fPoints:
#        pygame.draw.circle(window, "blue", point, 2)
for start, end in divisorLines:
        pygame.draw.line(window, "black", start, end, 1)
pygame.display.update()

display = True
while display:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        display = False
        pygame.time.delay(1000)