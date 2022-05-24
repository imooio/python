# Calcolare l'orbita di un pianeta 

def calcolo_orbita(dt):
    x0 = [1,0,0]
    v0 = [0,0.1,0]
    r = 1
    y0 = [0,0,0]
    t = 0
    dt = 0.0001
    N = int(10/dt)+1
    for i in range(N):

        #aggiorno l'accelerazione al tempo t

        r[2] = r[0]*r[0]+r[1]*r[1]+r[2]*r[2]
        r[3] = 
        a[0] = 
        a[1] =
        a[2] =

        #aggiorno la velocità al tempo t

        

        #aggiorno la posizione al tempo t

        




     print(i,f"{t:.5f},{r:.5f},{v0:.5f}")
        t += dt 

calcolo_orbita(0.0001)
