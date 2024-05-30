import os
import registries
from parser import parse


def lookup(query, registry=registries.RADB, custom_server=""):
    if registry == registries.CUSTOM:
        if custom_server == "" or custom_server is None:
            raise ValueError("Custom server must be specified when using the CUSTOM registry")

    command = "whois {} {} {}".format(registry, custom_server, query)
    results = os.popen(command).read()
    parsed_results = parse(results, registry)
    return parsed_results[0]


if __name__ == "__main__":
    whois_result = lookup("34.160.38.1", registries.CUSTOM, "whois.radb.net")
    print(whois_result.dict())
