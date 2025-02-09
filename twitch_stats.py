import sys
import os
clear = lambda: os.system('clear')
import time
import requests
sys.path.append("..")
import treasure
# curl -X GET 'https://api.twitch.tv/helix/streams' \
# -H 'Authorization: Bearer ' \
# -H 'Client-Id:  '

def authorizer(details:dict):

    response = requests.post(url = details["url"], params = details["body"])
    
    def api_call(details:dict):
        nonlocal response
        details["headers"]["Authorization"] =  f"Bearer {response.json()['access_token']}"
        api_response = requests.get(url = details["url"], headers = details["headers"])
        return api_response.json()["data"]
        
    if response.status_code != 200:
        raise Exception(f"Authorizer recived bad status code, {response}")
                
    return response.status_code , api_call


# user_id user_login viewer_count
# def viewer_changes_track(track_data, authorizer):
#     data = []
#     processed_data = []
#     track_data["recived_at"] = time.time()
#     data.append(track_data)
#     one_minute = 60
#     five_minutes = one_minute*5
#     fifteen_minutes = one_minute*15
#     # current unix - past_time_stick > *_minutes
#     
#     
# 
#     def process_data(data):
#         staticisized_data = []
#         for data_point in data:
#             
# 
#         return staticisized_data
#    for data_point in data:
#        if (data["recived_at"] - time.time()) < one_minute
#            for stream in data:
#
#    data.append(track_data)
#    # a time stick is like marks a period of time of intrest, a time stick of 15m will mean we are intrested in the last 15m of data
#    time_stick = 


def main():
    twitch_client_id = treasure.twitch_client_id
    twitch_client_secret = treasure.twitch_client_secret

    get_token_dict ={
            "url":"https://id.twitch.tv/oauth2/token",
            "body":{"client_id":twitch_client_id, 
                   "client_secret":twitch_client_secret,
                    "grant_type":"client_credentials"}
            }
    get_streams_dict ={
            "url":"https://api.twitch.tv/helix/streams",
            "headers":{"Client-Id": f"{twitch_client_id}"}
            }
    status_code, caller = authorizer(get_token_dict)
    streams_data = caller(get_streams_dict)
#    for stream in streams_data:
#        print(f"{stream['user_login']}: {stream['viewer_count']}")
    streams_data = caller(get_streams_dict)
    while True:
        for stream in streams_data:
            print(f"{stream['user_login']}: {stream['viewer_count']}")
        streams_data = caller(get_streams_dict)
        time.sleep(2)
        clear()
        #response = requests.get(url, headers = request_headers)



if __name__ == "__main__":
    main()

