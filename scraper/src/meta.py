from config import META_SHEET
from shared import clean_value, get_data, dump_data, number, youtube_link


def model_meta(row):
    # Transform a row into Meta (state) object
    # according to the schema in /schemas/meta.json
    # Make sure update /schemas/meta.json while changing here

    return {
        "name": clean_value(row[0]),
        "path": clean_value(row[1]),
        "number_of_hospitals": number(clean_value(row[2])),
        "state_summary": clean_value(row[3]),
        "state_logo": clean_value(row[4]),
        "pmu_summary": clean_value(row[5]),
        "state_donor_map": clean_value(row[6]),
        "lat": number(clean_value(row[7])),
        "lng": number(clean_value(row[8])),
        "north": number(clean_value(row[9])),
        "south": number(clean_value(row[10])),
        "west": number(clean_value(row[11])),
        "east": number(clean_value(row[12])),
        "youtube_link": youtube_link(clean_value(row[13])),
    }


csv_data = get_data(META_SHEET)

json_data = []

for row in csv_data:
    state = model_meta(row)
    if name := state["name"]:
        json_data.append(state)

dump_data("meta.json", json_data)

print(f"Dumped all {len(json_data)} Meta Data")
