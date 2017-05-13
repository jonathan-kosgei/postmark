# postmark.ServerConfigurationAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_current_server_configuration**](ServerConfigurationAPIApi.md#edit_current_server_configuration) | **PUT** /server | Edit Server Configuration
[**get_current_server_configuration**](ServerConfigurationAPIApi.md#get_current_server_configuration) | **GET** /server | Get Server Configuration


# **edit_current_server_configuration**
> ServerConfigurationResponse edit_current_server_configuration(x_postmark_server_token, body=body)

Edit Server Configuration

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.ServerConfigurationAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.EditServerConfigurationRequest() # EditServerConfigurationRequest | The settings that should be modified for the current server. (optional)

try: 
    # Edit Server Configuration
    api_response = api_instance.edit_current_server_configuration(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerConfigurationAPIApi->edit_current_server_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**EditServerConfigurationRequest**](EditServerConfigurationRequest.md)| The settings that should be modified for the current server. | [optional] 

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_server_configuration**
> ServerConfigurationResponse get_current_server_configuration(x_postmark_server_token)

Get Server Configuration

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.ServerConfigurationAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.

try: 
    # Get Server Configuration
    api_response = api_instance.get_current_server_configuration(x_postmark_server_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerConfigurationAPIApi->get_current_server_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

