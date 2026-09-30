if __name__ == "__main__":
    conf = load()
    print("service:", conf["service"])
    print("objective:", conf["objective"])
    print("window days:", conf["window_days"])
    print("error budget:", round(1 - conf["objective"], 4))
