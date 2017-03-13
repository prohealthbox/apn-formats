import time
from apn import lookup


def main():
    start = time.time()
    print lookup.lookup("washington", "adams")
    end = time.time()
    print end - start, "seconds"


if __name__ == "__main__":
    main()
