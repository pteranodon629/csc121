import sys

def main():
    coordinate_tuple = (43.376, -71.115)
    coordinate_list = [43.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()
