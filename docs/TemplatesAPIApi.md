# postmark.TemplatesAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template**](TemplatesAPIApi.md#delete_template) | **DELETE** /templates/{templateid} | Delete a Template
[**get_single_template**](TemplatesAPIApi.md#get_single_template) | **GET** /templates/{templateid} | Get a Template
[**list_templates**](TemplatesAPIApi.md#list_templates) | **GET** /templates | Get the Templates associated with this Server
[**send_email_with_template**](TemplatesAPIApi.md#send_email_with_template) | **POST** /email/withTemplate | Send an email using a Template
[**templates_post**](TemplatesAPIApi.md#templates_post) | **POST** /templates | Create a Template
[**test_template_content**](TemplatesAPIApi.md#test_template_content) | **POST** /templates/validate | Test Template Content
[**update_template**](TemplatesAPIApi.md#update_template) | **PUT** /templates/{templateid} | Update a Template


# **delete_template**
> TemplateDetailResponse delete_template(x_postmark_server_token, templateid)

Delete a Template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
templateid = 56 # int | The ID for the Template you wish to delete.

try: 
    # Delete a Template
    api_response = api_instance.delete_template(x_postmark_server_token, templateid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **templateid** | **int**| The ID for the Template you wish to delete. | 

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_template**
> TemplateDetailResponse get_single_template(x_postmark_server_token, templateid)

Get a Template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
templateid = 56 # int | The ID for the Template you wish to retrieve.

try: 
    # Get a Template
    api_response = api_instance.get_single_template(x_postmark_server_token, templateid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->get_single_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **templateid** | **int**| The ID for the Template you wish to retrieve. | 

### Return type

[**TemplateDetailResponse**](TemplateDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> TemplateListingResponse list_templates(x_postmark_server_token, count, offset)

Get the Templates associated with this Server

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
count = 3.4 # float | The number of Templates to return
offset = 3.4 # float | The number of Templates to \"skip\" before returning results.

try: 
    # Get the Templates associated with this Server
    api_response = api_instance.list_templates(x_postmark_server_token, count, offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **count** | **float**| The number of Templates to return | 
 **offset** | **float**| The number of Templates to \&quot;skip\&quot; before returning results. | 

### Return type

[**TemplateListingResponse**](TemplateListingResponse.md)

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
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.EmailWithTemplateRequest() # EmailWithTemplateRequest | 

try: 
    # Send an email using a Template
    api_response = api_instance.send_email_with_template(x_postmark_server_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->send_email_with_template: %s\n" % e)
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

# **templates_post**
> TemplateRecordResponse templates_post(x_postmark_server_token, body)

Create a Template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.CreateTemplateRequest() # CreateTemplateRequest | 

try: 
    # Create a Template
    api_response = api_instance.templates_post(x_postmark_server_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->templates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_template_content**
> TemplateValidationResponse test_template_content(x_postmark_server_token, body=body)

Test Template Content

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
body = postmark.TemplateValidationRequest() # TemplateValidationRequest |  (optional)

try: 
    # Test Template Content
    api_response = api_instance.test_template_content(x_postmark_server_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->test_template_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **body** | [**TemplateValidationRequest**](TemplateValidationRequest.md)|  | [optional] 

### Return type

[**TemplateValidationResponse**](TemplateValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> TemplateRecordResponse update_template(x_postmark_server_token, templateid, body)

Update a Template

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.TemplatesAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
templateid = 56 # int | The ID for the Template you wish to update.
body = postmark.EditTemplateRequest() # EditTemplateRequest | 

try: 
    # Update a Template
    api_response = api_instance.update_template(x_postmark_server_token, templateid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesAPIApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **templateid** | **int**| The ID for the Template you wish to update. | 
 **body** | [**EditTemplateRequest**](EditTemplateRequest.md)|  | 

### Return type

[**TemplateRecordResponse**](TemplateRecordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

