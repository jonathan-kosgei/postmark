# postmark.BouncesAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_bounce**](BouncesAPIApi.md#activate_bounce) | **PUT** /bounces/{bounceid}/activate | Activate a bounce
[**bounces_bounceid_dump_get**](BouncesAPIApi.md#bounces_bounceid_dump_get) | **GET** /bounces/{bounceid}/dump | Get bounce dump
[**get_bounced_tags**](BouncesAPIApi.md#get_bounced_tags) | **GET** /bounces/tags | Get bounced tags
[**get_bounces**](BouncesAPIApi.md#get_bounces) | **GET** /bounces | Get bounces
[**get_delivery_stats**](BouncesAPIApi.md#get_delivery_stats) | **GET** /deliverystats | Get delivery stats
[**get_single_bounce**](BouncesAPIApi.md#get_single_bounce) | **GET** /bounces/{bounceid} | Get a single bounce


# **activate_bounce**
> BounceActivationResponse activate_bounce(x_postmark_server_token, bounceid)

Activate a bounce

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
bounceid = 789 # int | The ID of the Bounce to activate.

try: 
    # Activate a bounce
    api_response = api_instance.activate_bounce(x_postmark_server_token, bounceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->activate_bounce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **int**| The ID of the Bounce to activate. | 

### Return type

[**BounceActivationResponse**](BounceActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bounces_bounceid_dump_get**
> BounceDumpResponse bounces_bounceid_dump_get(x_postmark_server_token, bounceid)

Get bounce dump

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
bounceid = 789 # int | The ID for the bounce dump to retrieve.

try: 
    # Get bounce dump
    api_response = api_instance.bounces_bounceid_dump_get(x_postmark_server_token, bounceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->bounces_bounceid_dump_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **int**| The ID for the bounce dump to retrieve. | 

### Return type

[**BounceDumpResponse**](BounceDumpResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounced_tags**
> list[str] get_bounced_tags(x_postmark_server_token)

Get bounced tags

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.

try: 
    # Get bounced tags
    api_response = api_instance.get_bounced_tags(x_postmark_server_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->get_bounced_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bounces**
> BounceSearchResponse get_bounces(x_postmark_server_token, count, offset, type=type, inactive=inactive, email_filter=email_filter, message_id=message_id, tag=tag, todate=todate, fromdate=fromdate)

Get bounces

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
count = 56 # int | Number of bounces to return per request. Max 500.
offset = 56 # int | Number of bounces to skip.
type = 'type_example' # str | Filter by type of bounce (optional)
inactive = true # bool | Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn't specified it will return both active and inactive. (optional)
email_filter = 'email_filter_example' # str | Filter by email address (optional)
message_id = 'message_id_example' # str | Filter by messageID (optional)
tag = 'tag_example' # str | Filter by tag (optional)
todate = '2013-10-20' # date | Filter messages up to the date specified. e.g. `2014-02-01` (optional)
fromdate = '2013-10-20' # date | Filter messages starting from the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get bounces
    api_response = api_instance.get_bounces(x_postmark_server_token, count, offset, type=type, inactive=inactive, email_filter=email_filter, message_id=message_id, tag=tag, todate=todate, fromdate=fromdate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->get_bounces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **count** | **int**| Number of bounces to return per request. Max 500. | 
 **offset** | **int**| Number of bounces to skip. | 
 **type** | **str**| Filter by type of bounce | [optional] 
 **inactive** | **bool**| Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn&#39;t specified it will return both active and inactive. | [optional] 
 **email_filter** | **str**| Filter by email address | [optional] 
 **message_id** | **str**| Filter by messageID | [optional] 
 **tag** | **str**| Filter by tag | [optional] 
 **todate** | **date**| Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 
 **fromdate** | **date**| Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**BounceSearchResponse**](BounceSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_stats**
> DeliveryStatsResponse get_delivery_stats(x_postmark_server_token)

Get delivery stats

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.

try: 
    # Get delivery stats
    api_response = api_instance.get_delivery_stats(x_postmark_server_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->get_delivery_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 

### Return type

[**DeliveryStatsResponse**](DeliveryStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_bounce**
> BounceInfoResponse get_single_bounce(x_postmark_server_token, bounceid)

Get a single bounce

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.BouncesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
bounceid = 789 # int | The ID of the bounce to retrieve.

try: 
    # Get a single bounce
    api_response = api_instance.get_single_bounce(x_postmark_server_token, bounceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BouncesAPIApi->get_single_bounce: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **bounceid** | **int**| The ID of the bounce to retrieve. | 

### Return type

[**BounceInfoResponse**](BounceInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

