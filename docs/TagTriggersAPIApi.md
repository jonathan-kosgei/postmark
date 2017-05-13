# postmark.TagTriggersAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag_trigger**](TagTriggersAPIApi.md#create_tag_trigger) | **POST** /triggers/tags | Create a trigger for a tag
[**delete_tag_trigger**](TagTriggersAPIApi.md#delete_tag_trigger) | **DELETE** /triggers/tags/{triggerid} | Delete a single trigger
[**edit_tag_trigger**](TagTriggersAPIApi.md#edit_tag_trigger) | **PUT** /triggers/tags/{triggerid} | Edit a single trigger
[**get_single_tag_trigger**](TagTriggersAPIApi.md#get_single_tag_trigger) | **GET** /triggers/tags/{triggerid} | Get a single trigger
[**searcg_tag_triggers**](TagTriggersAPIApi.md#searcg_tag_triggers) | **GET** /triggers/tags | Search triggers


# **create_tag_trigger**
> InlineResponse2006Tags create_tag_trigger(x_postmark_server_token, body=body)

Create a trigger for a tag

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TagTriggersAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.EditTagTriggerRequest() # EditTagTriggerRequest |  (optional)

try: 
    # Create a trigger for a tag
    api_response = api_instance.create_tag_trigger(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTriggersAPIApi->create_tag_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**EditTagTriggerRequest**](EditTagTriggerRequest.md)|  | [optional] 

### Return type

[**InlineResponse2006Tags**](InlineResponse2006Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_trigger**
> StandardPostmarkResponse delete_tag_trigger(x_postmark_server_token, triggerid)

Delete a single trigger

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TagTriggersAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
triggerid = 56 # int | The ID for the Tag Trigger that should be deleted.

try: 
    # Delete a single trigger
    api_response = api_instance.delete_tag_trigger(x_postmark_server_token, triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTriggersAPIApi->delete_tag_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **triggerid** | **int**| The ID for the Tag Trigger that should be deleted. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_tag_trigger**
> InlineResponse2006Tags edit_tag_trigger(x_postmark_server_token, triggerid, body=body)

Edit a single trigger

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TagTriggersAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
triggerid = 56 # int | The ID of the Tag Trigger that should be modified by this request.
body = postmark.EditTagTriggerRequest() # EditTagTriggerRequest |  (optional)

try: 
    # Edit a single trigger
    api_response = api_instance.edit_tag_trigger(x_postmark_server_token, triggerid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTriggersAPIApi->edit_tag_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **triggerid** | **int**| The ID of the Tag Trigger that should be modified by this request. | 
 **body** | [**EditTagTriggerRequest**](EditTagTriggerRequest.md)|  | [optional] 

### Return type

[**InlineResponse2006Tags**](InlineResponse2006Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_tag_trigger**
> InlineResponse2006Tags get_single_tag_trigger(x_postmark_server_token, triggerid)

Get a single trigger

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TagTriggersAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
triggerid = 56 # int | The ID for the Tag Trigger for which data should be retrieved.

try: 
    # Get a single trigger
    api_response = api_instance.get_single_tag_trigger(x_postmark_server_token, triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTriggersAPIApi->get_single_tag_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **triggerid** | **int**| The ID for the Tag Trigger for which data should be retrieved. | 

### Return type

[**InlineResponse2006Tags**](InlineResponse2006Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searcg_tag_triggers**
> InlineResponse2006 searcg_tag_triggers(x_postmark_server_token, count, offset, match_name=match_name)

Search triggers

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TagTriggersAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
count = 56 # int | Number of records to return per request.
offset = 56 # int | Number of records to skip.
match_name = 'match_name_example' # str | Filter by delivery tag (optional)

try: 
    # Search triggers
    api_response = api_instance.searcg_tag_triggers(x_postmark_server_token, count, offset, match_name=match_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTriggersAPIApi->searcg_tag_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **count** | **int**| Number of records to return per request. | 
 **offset** | **int**| Number of records to skip. | 
 **match_name** | **str**| Filter by delivery tag | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

