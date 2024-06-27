
import time
from manim import *

def binarySearch(arr, x):
    settime = time.perf_counter()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            endtime = time.perf_counter()
            return mid, (endtime*1000.00 - settime*1000.00)
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    endtime = time.perf_counter()
    return -1, (endtime*1000.00 - settime*1000.00)

def sequentialSearch(arr, x):
    settime = time.perf_counter()
    for i in range(len(arr)):
        if arr[i] == x:
            endtime = time.perf_counter()
            return i, (endtime*1000.00 - settime*1000.00)
    endtime = time.perf_counter()
    return -1, (endtime*1000.00 - settime*1000.00)
class SequentialSearch(Scene):
    def construct(self):
        indeks = VGroup(Text("["))
        c = 12
        y = 9
        for i in range(0, c):
            indeks.add(Text(str(i), font_size=36,color="#F0F000")).arrange(buff=2/c)
        indeks.add(Text("]", font_size=36)).arrange(buff=0.2)
        self.add(indeks)
        ponit = Text("_", font_size=36).next_to(indeks[1], DOWN)
        self.add(ponit)
        array = [x for x in range(0, c)]
        a,Time = sequentialSearch(array, y)
        for i in range(2,a+2):
            self.play(ponit.animate.next_to(indeks[i], DOWN), run_time=20/c)
        box = SurroundingRectangle(indeks[a+1], buff=0.1, color="#F00000")
        self.play(ReplacementTransform(ponit, box), run_time=2,color="#00F000")
        Time = Text("Time it takes : " + str(f"{Time:.4f}") + " ms ",font_size=36).to_corner(UL)
        self.play(TransformFromCopy(indeks, Time), run_time=2)
        self.wait(10)
class BinarySearch(Scene):
    def construct(self):
        indeks = VGroup(Text("["))
        c = 30
        y = 29
        for i in range(0, c):
            indeks.add(Text(str(i), font_size=36,color="#F000F0")).arrange(buff=2/c)
        indeks.add(Text("]", font_size=36)).arrange(buff=0.2)
        self.add(indeks)
        
        ponit = Text("_", font_size=36).next_to(indeks[1], DOWN)
        self.add(ponit)
        
        array = [x for x in range(0, c)]
        a,Time = binarySearch(array, y)
        
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (high + low) // 2
            self.play(ponit.animate.next_to(indeks[mid+1], DOWN), run_time=20/c)
            if array[mid] == y:
                break
            elif array[mid] < y:
                low = mid + 1
            else:
                high = mid - 1
        
        box = SurroundingRectangle(indeks[a+1], buff=0.1, color="#F00000")
        self.play(ReplacementTransform(ponit, box), run_time=2,color="#00F000")
        Time = Text("Time it takes : " + str(f"{Time:.4f}") + " ms ",font_size=36).to_corner(UL)
        self.play(TransformFromCopy(indeks, Time), run_time=2)
        self.wait(10)