from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

users2 = {"Clara": {"Blues Traveler": 4.75,"Norah Jones": 4.5, "Phoenix": 5.0,"The Strokes": 4.25, "Weird Al": 4.0},
         "Robert": {"Blues Traveler": 4.0,"Norah Jones": 3.0, "Phoenix": 5.0,"The Strokes": 2.0, "Weird Al": 1.0}
        }

def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1 #sin calificaciones en comun 
    
def euclidean(rating1, rating2):
    distance = 0
    total = 0
    for key in rating1:
        if key in rating2:
            distance += (pow(rating1[key]- rating2[key], 2))
            total += 1
    if total > 0:
        return sqrt (distance)
    else:
        return -1

def minkowski(rating1, rating2, r):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key]- rating2[key]), r)
            commonRatings = True
        if commonRatings:
            return pow(distance, 1/r)
        else:
            return 0

def coseno (rating1, rating2):
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x*y
            sum_x2 += x**2
            sum_y2 += y**2
  
    #print (sum_xy)
    #print (sum_x2)
    #print (sum_y2)
    if n == 0:
            return 0
    denominator = sqrt(sum_x2) * sqrt(sum_y2)
    if denominator == 0:
        return 0
    else:
        return (sum_xy) / denominator

def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)

    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator
            

def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
        distances.sort()
    return distances

def recommend(username, users):
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)


print ("_________________________DISTANCIA MANHATTAN_________________________")    
print ("Distancia euclideana entre Hailey y Veronica = " , manhattan(users['Hailey'], users['Veronica']))    
print ("Distancia euclideana entre Hailey y Jordyn = " , manhattan(users['Hailey'], users['Jordyn']))
print ("______________________________________________________________________")
print ("                                                                    ")
print ("_________________________DISTANCIA EUCLIDEANA_________________________")    
print ("Distancia euclideana entre Hailey y Veronica = " , euclidean(users['Hailey'], users['Veronica']))    
print ("Distancia euclideana entre Hailey y Jordyn = " , euclidean(users['Hailey'], users['Jordyn']))
print ("______________________________________________________________________")
print ("                                                                    ")
print ("_________________________DISTANCIA MINKOWSKI_________________________")    
print ("Distancia euclideana entre Hailey y Veronica = " , minkowski(users['Hailey'], users['Veronica'] ,2))    
print ("Distancia euclideana entre Hailey y Jordyn = " , minkowski(users['Hailey'], users['Jordyn'] ,2))
print ("______________________________________________________________________")
print ("                                                                    ")
print ("_________________________COMPUTENEARESTNEIGHBOR_________________________")    
print ("Vecinos mas cercanos de Hailey = " , computeNearestNeighbor("Hailey",users))    
print ("Vecinos mas cercanos de Angelica = " , computeNearestNeighbor("Angelica",users))
print ("______________________________________________________________________")
print ("                                                                    ")
print ("_________________________RECOMENDACIONES_________________________")    
print ("Recomendaciones para Hailey = " ,recommend('Hailey', users))
print ("Recomendaciones para Chan = " ,recommend('Chan', users))
print ("Recomendaciones para Angelica = " ,recommend('Angelica', users))
print ("Recomendaciones para Sam = " ,recommend('Sam', users))
print ("______________________________________________________________________")
print ("_________________________SIMILARIDAD DEL COSENO_________________________")    
print ("Similaridad del coseno entre Angelica y Veronica = " , coseno(users['Angelica'], users['Veronica']))    
print ("______________________________________________________________________")
print ("                                                                    ")
print ("_________________________PEARSON_________________________")    
print ("Distancia pearson entre Angelica y Bill = " , pearson(users['Angelica'], users['Bill']))    
print ("Distancia pearson entre Hailey y Angelica = " , pearson(users['Angelica'], users['Hailey']))
print ("______________________________________________________________________")

