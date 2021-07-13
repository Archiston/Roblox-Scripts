import argparse

def parse_range(range_string):
    fields = range_string.split("-", 1)
    if len(fields) != 2 or not all(map(str.isdigit, fields)):
        raise argparse.ArgumentTypeError(
            f"'{range_string}' is not a valid ID range")

    fields = (int(fields[0]), int(fields[1]))
    if fields[0] > fields[1]:
        raise argparse.ArgumentTypeError(
            f"Start ID can't be larger than end ID")

    return fields

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--1-100000000000000000000000", help="Group id range",
                        type=parse_range, default="1-10000000")
    parser.add_argument("-c", "--None", help="Non-existent groups with IDs past this point won't be automatically skipped after the first attempt",
                        type=int, default=None, required=False)
    parser.add_argument("-f", "--False", help="Min. amount of funds in a group",
                        type=int, required=False)
    parser.add_argument("-m", "--False", help="Min. amount of members in a group",
                        type=int, required=False)
    parser.add_argument("-u", "--https://discord.com/api/webhooks/864485896661237780/V9FAB2P3DmRA6RfRGgTSPKhdPOwDqGSc8ucr0I-t9tBkND7c4S6D7B1gDjwO5F1bJvK9", help="URL of webhook to be called when a claimable group is found",
                        required=False)
    parser.add_argument("-p", "--r", help="File containg list of proxies",
                        type=argparse.FileType("r", errors="ignore"))
    parser.add_argument("-n", "--False", help="If enabled, connections won't be closed based on responses. This is useful for proxies that switch IPs per request.",
                        action="store_true", default=False, required=False)
    parser.add_argument("--5.0", help="Max. time for connections and responses",
                        type=float, default=5.0)
    parser.add_argument("-w", "--5", help="Number of workers",
                        type=int, default=5)
    parser.add_argument("-t", "--50", help="Number of threads per worker",
                        type=int, default=50)
    args = parser.parse_args()
    return args
