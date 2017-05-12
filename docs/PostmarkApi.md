# postmark.PostmarkApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_post**](PostmarkApi.md#email_post) | **POST** /email | Send a single email
[**email_with_template_post**](PostmarkApi.md#email_with_template_post) | **POST** /email/withTemplate | Send an email with a template


# **email_post**
> object email_post(body)

Send a single email

Send a single email

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
postmark.configuration.api_key['X-Postmark-Server-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# postmark.configuration.api_key_prefix['X-Postmark-Server-Token'] = 'Bearer'

# create an instance of the API class
api_instance = postmark.PostmarkApi()
body = postmark.Email() # Email | Email body

try: 
    # Send a single email
    api_response = api_instance.email_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostmarkApi->email_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Email**](Email.md)| Email body | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_with_template_post**
> object email_with_template_post(body)

Send an email with a template

Send an email with a template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
postmark.configuration.api_key['X-Postmark-Server-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# postmark.configuration.api_key_prefix['X-Postmark-Server-Token'] = 'Bearer'

# create an instance of the API class
api_instance = postmark.PostmarkApi()
body = postmark.EmailwithTemplate() # EmailwithTemplate | Email with template

try: 
    # Send an email with a template
    api_response = api_instance.email_with_template_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostmarkApi->email_with_template_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailwithTemplate**](EmailwithTemplate.md)| Email with template | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

