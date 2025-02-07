import pytest
import pytest_asyncio

from typing import Union

from youtubesearchpython.__future__ import Hashtag, CustomSearch
from youtubesearchpython import VideoSortOrder

@pytest.mark.asyncio
async def test_custom_search(
    query = "cs2",
    search_limit = 100_000,
    iso_language = None,
    region = None,
    hashtag_search = False,
    search_type = "all",
    request_id: Union[str, None] = None,
):
    search_obj = CustomSearch(
            query, 
            VideoSortOrder.uploadDate, 
            language = "ru" if iso_language is None else iso_language,
            region = "RU" if region is None else region,
            limit = search_limit,
        )
    
    result_list = []
    results = await search_obj.next()
    result_list.extend(results["result"])
    total_count = 0
    
    unique_id_set = set()
    for result_dict in results.get("result", []):
        unique_id_set.add(result_dict.get("id", None))
    
    unique_id_set_last_len = len(unique_id_set)

    while len(results["result"])> 0:
        print(total_count, len(results["result"]), query)
        total_count += len(results["result"])

        results = await search_obj.next()
        result_list.extend(results["result"])
        for result_dict in results.get("result", []):
            unique_id_set.add(result_dict.get("id", None))
        
        if len(unique_id_set) == unique_id_set_last_len:
            # TODO может быть стоит несколько раз ретраить?(вроде как и так сойдёт)
            break
        
        unique_id_set_last_len = len(unique_id_set)
    
    if request_id is not None:
        for result_dict in result_list:
            result_dict["request_id"] = request_id

@pytest.mark.asyncio
async def test_hashtag_all(
    query = "cs2",
    search_limit = 100_000,
    iso_language = None,
    region = None,
    hashtag_search = False,
    search_type = "all",
    request_id: Union[str, None] = None,
):
    search_obj = Hashtag(
        query, 
        limit= search_limit, 
        language = "ru" if iso_language is None else iso_language,
        region = "RU" if region is None else region,
        search_type = search_type
    )
    
    result_list = []
    results = await search_obj.next()
    result_list.extend(results["result"])
    total_count = 0
    assert len(result_list) > 0, 'Получили пустую выдачу'
    
    unique_id_set = set()
    for result_dict in results.get("result", []):
        unique_id_set.add(result_dict.get("id", None))
    
    unique_id_set_last_len = len(unique_id_set)

    while len(results["result"])> 0:
        print(total_count, len(results["result"]), query)
        total_count += len(results["result"])

        results = await search_obj.next()
        result_list.extend(results["result"])
        for result_dict in results.get("result", []):
            unique_id_set.add(result_dict.get("id", None))
        
        if len(unique_id_set) == unique_id_set_last_len:
            # TODO может быть стоит несколько раз ретраить?(вроде как и так сойдёт)
            break
        
        unique_id_set_last_len = len(unique_id_set)
    
    if request_id is not None:
        for result_dict in result_list:
            result_dict["request_id"] = request_id