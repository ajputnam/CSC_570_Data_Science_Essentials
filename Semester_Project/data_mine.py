#  --------------------------------------------------------------------------
#  University of Illinois
#  CSC 570 - Data Science Essentials
#  Semester Project
#  Author: Arthur Putnam
#  --------------------------------------------------------------------------
import requests
import json
import csv
import datetime

# items of interest
PRAYER_POTION = {
    'prayer_potion_3': 139,
    'snape_grass': 231,
    'ranarr_weed': 257,
    'ranarr_seed': 5295,
    'vial': 229,
    'vial_of_water': 227,
    'super_restore': 3026
}

HERBS = {
    'herb1': 261,
    'herb2': 263,
    'herb3': 265,
    'herb4': 267,
    'herb5': 269,
    'herb6': 251,
    'herb7': 253,
    'herb8': 255,
    'herb9': 259,
    'herb10': 249,
}

def get(items):
    """Gets the data from the api for the passed item ids."""
    base_url = 'http://services.runescape.com/m=itemdb_oldschool/api/'
    prices_url = '{}graph/{}.json'
    detail_url = '{}catalogue/detail.json?item={}'
    data = []
    for item_id in items:
        r1 = requests.get(prices_url.format(base_url, item_id))
        r2 = requests.get(detail_url.format(base_url, item_id))
        item = {
            'prices': json.loads(str(r1.text)),
            'name': json.loads(str(r2.text))['item']['name'],
            'item_id': item_id
        }
        data.append(item)
    return data


def extract_features(data):
    """Extracts the pieces of the data we are interested in."""
    items = []

    # for each item get the daily price
    for item in data:
        # get list of tuples (timestamp, price)
        daily_values = [(float(key)/1000, value)
                        for key, value in item['prices']['daily'].items()]
        # sort by timestamp
        daily_values.sort(key=lambda tup: tup[0])

        item['prices'] = daily_values

        items.append(item)
    return items


def format_item_prices_by_date(items):
    """Formats the data so it can be easily wrote out to csv."""
    PRICE = 1
    item_prices_by_day = []

    # All items should have same amount of data points with the same timestamps
    # so we can just get the length of the prices from first item in the list
    for i in range(len(items[0]['prices'])):

        # convert timestamp to date
        date = datetime.datetime\
            .fromtimestamp(float(items[0]['prices'][i][0])).strftime("%m-%d-%Y")

        # get the data for each item
        prices_on_date = {
            'date': date
        }
        # for each item get items price
        for item in items:
            column_name = str(item['name'])+'_'+str(item['item_id'])
            prices_on_date[column_name] = str(item['prices'][i][PRICE])
        item_prices_by_day.append(prices_on_date)
    return item_prices_by_day


def write_data_to_csv(item_prices_by_day, file_name='default'):
    """Writes item prices to csv file."""
    keys = item_prices_by_day[0].keys()
    with open('{}.csv'.format(file_name), 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(item_prices_by_day)


def mine_data(item_ids, file_name):
    """Mine, format and export data for given ids."""
    print("Mining data...")
    raw_data = get(item_ids)
    print('Formatting data...')
    selected_features = extract_features(raw_data)
    item_prices_by_day = format_item_prices_by_date(selected_features)
    print('Writting to file...')
    write_data_to_csv(item_prices_by_day, file_name=file_name)
    print("Done! See prayer_pot.csv")


def main():
    """Create csvs for semester project."""
    a = [item_id for key, item_id in PRAYER_POTION.items()]
    b = a + [item_id for key, item_id in HERBS.items()]
    mine_data(a, 'prayer_pot')
    mine_data(b, 'herbs')


if __name__ == "__main__":
    main()