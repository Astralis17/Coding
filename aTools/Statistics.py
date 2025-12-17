
def findAvg(iterable):
    try:
        total = 0
        for i in iterable:
            total += i
        avg = total/len(iterable)
    except:
        avg = 0
    return avg

def findCorrelationCoefficient(x, y):
        xAVG = findAvg(x)
        yAVG = findAvg(y)
        points = [(x[i], y[i]) for i,j in enumerate(x)]
        for point, in points:
                numerator += (point[0] - xAVG)*(point[1] - yAVG)
                denominatorPt1 += (point[0] - xAVG)**2
                denominatorPt2 += (point[1] - yAVG)**2

        denominator = (denominatorPt1*denominatorPt2)**0.5
        correlationCoeficient = numerator/denominator

        return correlationCoeficient