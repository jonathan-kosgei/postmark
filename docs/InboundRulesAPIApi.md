# postmark.InboundRulesAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inbound_rule**](InboundRulesAPIApi.md#create_inbound_rule) | **POST** /triggers/inboundrules | Create an inbound rule trigger
[**delete_inbound_rule**](InboundRulesAPIApi.md#delete_inbound_rule) | **DELETE** /triggers/inboundrules/{triggerid} | Delete a single trigger
[**list_inbound_rules**](InboundRulesAPIApi.md#list_inbound_rules) | **GET** /triggers/inboundrules | List inbound rule triggers


# **create_inbound_rule**
> InlineResponse2008 create_inbound_rule(x_postmark_server_token, body=body)

Create an inbound rule trigger

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.InboundRulesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.CreateInboundRuleRequest() # CreateInboundRuleRequest |  (optional)

try: 
    # Create an inbound rule trigger
    api_response = api_instance.create_inbound_rule(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundRulesAPIApi->create_inbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**CreateInboundRuleRequest**](CreateInboundRuleRequest.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_rule**
> StandardPostmarkResponse delete_inbound_rule(x_postmark_server_token, triggerid)

Delete a single trigger

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.InboundRulesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
triggerid = 56 # int | The ID of the Inbound Rule that should be deleted.

try: 
    # Delete a single trigger
    api_response = api_instance.delete_inbound_rule(x_postmark_server_token, triggerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundRulesAPIApi->delete_inbound_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **triggerid** | **int**| The ID of the Inbound Rule that should be deleted. | 

### Return type

[**StandardPostmarkResponse**](StandardPostmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inbound_rules**
> InlineResponse2007 list_inbound_rules(x_postmark_server_token, count, offset)

List inbound rule triggers

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.InboundRulesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
count = 56 # int | Number of records to return per request.
offset = 56 # int | Number of records to skip.

try: 
    # List inbound rule triggers
    api_response = api_instance.list_inbound_rules(x_postmark_server_token, count, offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboundRulesAPIApi->list_inbound_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **count** | **int**| Number of records to return per request. | 
 **offset** | **int**| Number of records to skip. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

