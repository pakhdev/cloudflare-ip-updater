import requests
import json


def read_config():
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)
    return config_data


def save_ip(new_ip, config_data):
    config_data["last_ip"] = new_ip

    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file, indent=4)


def retrieve_ip():
    response = requests.get('https://checkip.amazonaws.com')
    if response.status_code == 200:
        return response.text.replace("\n", "")
    else:
        return False


def update_record(new_ip, zone_id, record_id, record_type, domain_name, bearer):
    bearer = bearer.replace("Bearer ", "")
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/json"
    }
    data = {
        "type": record_type,
        "name": domain_name,
        "content": new_ip
    }
    requests.put(url, json=data, headers=headers)


if __name__ == "__main__":
    current_ip = retrieve_ip()
    config = read_config()
    if current_ip != config["last_ip"]:
        save_ip(current_ip, config)
        for domain in config["domains"]:
            update_record(
                current_ip,
                domain["zone_id"],
                domain["record_id"],
                domain["type"],
                domain["name"],
                domain["bearer"]
             )
