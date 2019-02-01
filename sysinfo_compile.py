import json
import subprocess

configfile = open('sysinfo.json').read()
# print(configfile)

config = json.loads(configfile)
# print config["index"]["uptime"]["command"]
for category in config:
    pagenr = 0
    for page in config[category]:
        print("Processing " + str(pagenr) + " " + category + "/" + page)
        try:
            command = config[category][page]["command"]
            print("  Command: " + command)
            result = subprocess.run(command.split(), stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))
        except Exception as ex:
            print(ex)
        filename = category
        if pagenr != 0:
            filename = filename + "_" + page
        filename = filename + ".html"
        print("filename: " + filename)
        pagenr = pagenr + 1
