import json, sys

# Just load and reference these as json
data = {
    'names': json.loads(open('./classes/card/names.json', "r", encoding="utf-8").read()),
    'suites': json.loads(open('./classes/card/suites.json', "r", encoding="utf-8").read())
}

sys.modules[__name__] = data