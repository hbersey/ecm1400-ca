import intelligence as mi
import os


# Test if the function find_cyan_pixels() creates a file
# Functionally is tested in the test_find_pixels() function

def test_find_cyan_pixels():
    exists = os.path.exists("map-cyan-pixels.jpg")

    if exists:
        t = os.stat("map-cyan-pixels.jpg").st_ctime

        f = open("map-cyan-pixels.jpg", "rb")
        content = f.read()
        f.close()

        mi.find_cyan_pixels("data/map.png")

        t2 = os.stat("map-cyan-pixels.jpg").st_ctime
        assert t2 > t

        f = open("map-cyan-pixels.jpg", "wb")
        f.write(content)
        f.close()
    else:
        mi.find_cyan_pixels("data/map.png")
        assert os.path.exists("map-cyan-pixels.jpg")
        os.remove("map-cyan-pixels.jpg")
