import json
import csv

# function


def to_csv(list_param, filename_param):
    keys = list_param[0].keys()
    with open(filename_param, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_param)


def user_to_csv(data):
    list_user = []
    for row in data:
        list_user.append(row['user'])
    to_csv(list_user, 'user.csv')


def txs_to_csv(data):
    list_txs = []
    for row in data:
        for txs in row['txs']:
            list_txs.append(txs)
    to_csv(list_txs, 'txs.csv')


def usertx_to_csv(data):
    list_usertx = []
    for row in data:
        for txs in row['txs']:
            list_usertx.append(
                {'user_id': row['user']['id'], 'tx_id': txs['id']})
    to_csv(list_usertx, 'usertx.csv')


# main
with open('trx.json') as json_file:
    data = json.load(json_file)

user_to_csv(data)
txs_to_csv(data)
usertx_to_csv(data)
