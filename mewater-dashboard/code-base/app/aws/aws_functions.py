import boto3
from app import config


# AWS SDK config
ddb_client = boto3.client('dynamodb', region_name="us-east-1",
                          aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)


def get_items():

    result = ddb_client.scan(
        TableName='mewater-ddb-processed'
    )

    items_list = []
    items = result["Items"]
    for item in items:
        item_dict = {}
        keys = item.keys()
        for key in keys:
            item_dict[key] = list(item[key].values())[0]

        items_list.append(item_dict)

    return items_list


def get_leakage_info():
    items_list = get_items()

    # TODO: Sort to get most up to date leakage info
    recent_item = items_list[0]

    leaked_volume = int(recent_item['leaked_volume'])

    return leaked_volume


def get_consumption_info():
    items_list = get_items()

    # TODO: Sort to get most up to date leakage info
    recent_item = items_list[0]

    consumption = {
        "outlet_1": int(recent_item['outlet1_volume']),
        "outlet_2": int(recent_item['outlet2_volume'])
    }

    return consumption


def get_hourly_usage():
    items_list = get_items()
    print(items_list)

    # TODO: Get every 60th minute item = hourly item for 8 iterations (8 hours)
    hours = []
    tracked_hours = 8

    for index, i in enumerate(items_list):
        if len(hours) == tracked_hours:
            break
        if index % tracked_hours == 0:
            hours.append(i)

    return hours
