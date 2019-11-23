import time
import threading

def calc_square(numbers):
    print("calculator square number")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculator cube of number")
    for n in numbers:
        time.sleep(0.2)
        print('cube',n*n*n)

arr = [2,3,8,9]

t = time.time()
#calc_square(arr)
#calc_cube(arr)

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

#.join work for wait untill the programme is done
t1.join()
t2.join()

print("done in :",time.time()-t)
print("Hah.......I am Done with all my work now")