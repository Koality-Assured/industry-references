import json
path = r'C:\Code\KA\_wt\industry-references-fixes\schemas\federal_state.schema.json'
with open(path, 'r') as f:
    schema = json.load(f)
schema['properties']['sources']['items']['properties']['http_status']['type'] = ['integer', 'null']
with open(path, 'w') as f:
    json.dump(schema, f, indent=2)
