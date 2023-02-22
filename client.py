import requests


def create_article(article_info, return_option):
    request_result = requests.post("http://0.0.0.0:9000/create/article", json=article_info)

    if return_option == 'json':
        return request_result.json()

    if return_option == 'json':
        return request_result.text

    else:
        return {"message": "return_option_error"}


def get_article(article_id, return_option):
    params = {'article_id': article_id}

    request_result = requests.get(f"http://0.0.0.0:9000/get/article", params=params)

    if return_option == 'json':
        return request_result.json()

    if return_option == 'json':
        return request_result.text

    else:
        return {"message": "return_option_error"}


def list_article(return_option):
    request_result = requests.get("http://0.0.0.0:9000/list/article")

    if return_option == 'json':
        return request_result.json()

    if return_option == 'json':
        return request_result.text

    else:
        return {"message": "return_option_error"}


def update_article(article_id, article_info, return_option):
    params = {'article_id': article_id}

    request_result = requests.put(f"http://0.0.0.0:9000/update/article", params=params, json=article_info)

    if return_option == 'json':
        return request_result.json()

    if return_option == 'json':
        return request_result.text

    else:
        return {"message": "return_option_error"}


def delete_article(article_id, return_option):
    params = {'article_id': article_id}

    request_result = requests.delete(f"http://0.0.0.0:9000/delete/article", params=params)

    if return_option == 'json':
        return request_result.json()

    if return_option == 'json':
        return request_result.text

    else:
        return {"message": "return_option_error"}


################ CREATE ################
### Create Article Example 1 ###
# print(create_article(article_info={'title': 'Deneme Yazısı', 'content': 'Bu bir deneme yazısıdır.', 'read_time': 10, 'is_active': True}, return_option='json'))
# ### Create Article Example 2 ###
# print(create_article(article_info={'title': 'Deneme Yazısı', 'content': 'Bu bir deneme yazısıdır.', 'read_time': 10, 'is_active': True}, return_option='text'))
# ########################################
#
# ################ GET ################
# ### Get Article Example 1 ###
# print(get_article(article_id=3, return_option='json'))
# ### Get Article Example 2 ###
# print(get_article(article_id=3, return_option='text'))
# ########################################
#
# ################ LİST ################
# ### List Article Example 1 ###
# print(list_article(return_option='json'))
# ### List Article Example 2 ###
# print(list_article(return_option='text'))
# ########################################
#
# ################ UPDATE ################
# ### Update Article Example 1 ###
# print(update_article(article_id=3, article_info={'title': 'Deneme Yazısı', 'content': 'Bu bir deneme yazısıdır.', 'read_time': 10, 'is_active': True}, return_option='json'))
# ### Update Article Example 2 ###
# print(update_article(article_id=3, article_info={'title': 'Deneme Yazısı', 'content': 'Bu bir deneme yazısıdır.', 'read_time': 10, 'is_active': True}, return_option='text'))
# ########################################
#
# ################ DELETE ################
# ### Delete Article Example 1 ###
# print(delete_article(article_id=3, return_option='json'))
# ### Delete Article Example 2 ###
# print(delete_article(article_id=3, return_option='text'))
########################################
