# postmark.SendingAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](SendingAPIApi.md#send_email) | **POST** /email | Send a single email
[**send_email_batch**](SendingAPIApi.md#send_email_batch) | **POST** /email/batch | Send a batch of emails
[**send_email_with_template**](SendingAPIApi.md#send_email_with_template) | **POST** /email/withTemplate | Send an email using a Template


# **send_email**
> SendEmailResponse send_email(x_postmark_server_token, body=body)

Send a single email

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.SendingAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.SendEmailRequest() # SendEmailRequest |  (optional)

try: 
    # Send a single email
    api_response = api_instance.send_email(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendingAPIApi->send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**SendEmailRequest**](SendEmailRequest.md)|  | [optional] 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_batch**
> SendEmailBatchResponse send_email_batch(x_postmark_server_token, body=body)

Send a batch of emails

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.SendingAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.SendEmailBatchRequest() # SendEmailBatchRequest |  (optional)

try: 
    # Send a batch of emails
    api_response = api_instance.send_email_batch(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendingAPIApi->send_email_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**SendEmailBatchRequest**](SendEmailBatchRequest.md)|  | [optional] 

### Return type

[**SendEmailBatchResponse**](SendEmailBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_with_template**
> SendEmailResponse send_email_with_template(x_postmark_server_token, body)

Send an email using a Template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.SendingAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.EmailWithTemplateRequest() # EmailWithTemplateRequest | 

try: 
    # Send an email using a Template
    api_response = api_instance.send_email_with_template(x_postmark_server_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SendingAPIApi->send_email_with_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**EmailWithTemplateRequest**](EmailWithTemplateRequest.md)|  | 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

