def Features(start="\033[1m", mid="\033[93m", end="\033[0;0m", arrow=" --> "):
    func_dict = {
        "URL scan": "!urlscan <URL-TO-SCAN>",
        "File scan": "!filescan <PATH-TO-FILE>",
    }

    for item in func_dict.keys():
        print("{}{}".format(start, mid, item, arrow, end, func_dict[item]))
