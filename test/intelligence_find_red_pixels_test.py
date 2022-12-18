import intelligence as mi
import os


# Test if the function find_red_pixels() creates a file
# Functionally is tested in the test_find_pixels() function

def test_find_red_pixels():
    exists = os.path.exists("map-red-pixels.jpg")

    if exists:
        t = os.stat("map-red-pixels.jpg").st_ctime

        f = open("map-red-pixels.jpg", "rb")
        content = f.read()
        f.close()

        mi.find_red_pixels("data/map.png")

        t2 = os.stat("map-red-pixels.jpg").st_ctime
        assert t2 > t

        f = open("map-red-pixels.jpg", "wb")
        f.write(content)
        f.close()
    else:
        mi.find_red_pixels("data/map.png")
        assert os.path.exists("map-red-pixels.jpg")
        os.remove("map-red-pixels.jpg")
