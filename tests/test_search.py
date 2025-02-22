import pytest

from youtubesearchpython.search import CustomSearch, VideosSearch
from youtubesearchpython import CustomSearch, VideoSortOrder, Hashtag

iso_language = None
region = None
search_limit = 10_000
query="cs2"

def test_custom_search():
    result_list = []
    customSearch = CustomSearch(
        query, 
        VideoSortOrder.uploadDate, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        limit = search_limit
        )
    
    result_list.extend(customSearch.result()["result"])
    assert len(result_list) > 0 , "Получили пустую выдачу"
    while customSearch._next():
        print(len(result_list))
        currient_result = customSearch.result()["result"]
        
        if currient_result is None:
            break
        
        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
        break
        # if currient_result[-1].get("publishedTime","").find(query_early_stop) != -1:
    
    result_list = []
    customSearch = CustomSearch(
        query, 
        VideoSortOrder.uploadDate, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        limit = search_limit,
        short_component = True,
        )
    
    result_list.extend(customSearch.result()["result"])
    assert len(result_list) > 0 , "Получили пустую выдачу"
    while customSearch._next():
        print(len(result_list))
        currient_result = customSearch.result()["result"]
        
        if currient_result is None:
            break
        
        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
        break
        # if currient_result[-1].get("publishedTime","").find(query_early_stop) != -1:
        #     break

    # return True

def test_hashtag_search_all():
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        search_type = "all"
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        search_type = "all",
        short_component = True,
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
def test_hashtag_search_shorts():
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        search_type = "shorts"
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        short_component = True,
        search_type = "shorts"
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
def test_hashtag_search_default():
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        # search_type = None
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
    hastag_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        # search_type = None
        short_component = True
        )
    result_list = []

    while hastag_obj.next():
        print(len(result_list))
        currient_result = hastag_obj.result()["result"]

        result_list.extend(currient_result)
        if len(currient_result) == 0:
            break    
    
    assert len(result_list) > 0 , "Получили пустую выдачу"
    
    