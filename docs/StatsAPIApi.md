# postmark.StatsAPIApi

All URIs are relative to *https://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bounce_counts**](StatsAPIApi.md#get_bounce_counts) | **GET** /stats/outbound/bounces | Get bounce counts
[**get_outbound_click_counts**](StatsAPIApi.md#get_outbound_click_counts) | **GET** /stats/outbound/clicks | Get click counts
[**get_outbound_click_counts_by_browser_family**](StatsAPIApi.md#get_outbound_click_counts_by_browser_family) | **GET** /stats/outbound/clicks/browserfamilies | Get browser usage by family
[**get_outbound_click_counts_by_location**](StatsAPIApi.md#get_outbound_click_counts_by_location) | **GET** /stats/outbound/clicks/location | Get clicks by body location
[**get_outbound_click_counts_by_platform**](StatsAPIApi.md#get_outbound_click_counts_by_platform) | **GET** /stats/outbound/clicks/platforms | Get browser plaform usage
[**get_outbound_open_counts**](StatsAPIApi.md#get_outbound_open_counts) | **GET** /stats/outbound/opens | Get email open counts
[**get_outbound_open_counts_by_email_client**](StatsAPIApi.md#get_outbound_open_counts_by_email_client) | **GET** /stats/outbound/opens/emailclients | Get email client usage
[**get_outbound_open_counts_by_platform**](StatsAPIApi.md#get_outbound_open_counts_by_platform) | **GET** /stats/outbound/opens/platforms | Get email platform usage
[**get_outbound_open_counts_by_reading_time**](StatsAPIApi.md#get_outbound_open_counts_by_reading_time) | **GET** /stats/outbound/opens/readtimes | Get email read times
[**get_outbound_overview_statistics**](StatsAPIApi.md#get_outbound_overview_statistics) | **GET** /stats/outbound | Get outbound overview
[**get_sent_counts**](StatsAPIApi.md#get_sent_counts) | **GET** /stats/outbound/sends | Get sent counts
[**get_spam_complaints**](StatsAPIApi.md#get_spam_complaints) | **GET** /stats/outbound/spam | Get spam complaints
[**get_tracked_email_counts**](StatsAPIApi.md#get_tracked_email_counts) | **GET** /stats/outbound/tracked | Get tracked email counts


# **get_bounce_counts**
> InlineResponse200 get_bounce_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get bounce counts

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get bounce counts
    api_response = api_instance.get_bounce_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_bounce_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_click_counts**
> DynamicResponse get_outbound_click_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get click counts

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get click counts
    api_response = api_instance.get_outbound_click_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_click_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**DynamicResponse**](DynamicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_click_counts_by_browser_family**
> object get_outbound_click_counts_by_browser_family(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get browser usage by family

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get browser usage by family
    api_response = api_instance.get_outbound_click_counts_by_browser_family(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_click_counts_by_browser_family: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_click_counts_by_location**
> DynamicResponse get_outbound_click_counts_by_location(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get clicks by body location

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get clicks by body location
    api_response = api_instance.get_outbound_click_counts_by_location(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_click_counts_by_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**DynamicResponse**](DynamicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_click_counts_by_platform**
> DynamicResponse get_outbound_click_counts_by_platform(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get browser plaform usage

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get browser plaform usage
    api_response = api_instance.get_outbound_click_counts_by_platform(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_click_counts_by_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**DynamicResponse**](DynamicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_open_counts**
> InlineResponse2003 get_outbound_open_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get email open counts

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get email open counts
    api_response = api_instance.get_outbound_open_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_open_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_open_counts_by_email_client**
> InlineResponse2005 get_outbound_open_counts_by_email_client(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get email client usage

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get email client usage
    api_response = api_instance.get_outbound_open_counts_by_email_client(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_open_counts_by_email_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_open_counts_by_platform**
> InlineResponse2004 get_outbound_open_counts_by_platform(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get email platform usage

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get email platform usage
    api_response = api_instance.get_outbound_open_counts_by_platform(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_open_counts_by_platform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_open_counts_by_reading_time**
> DynamicResponse get_outbound_open_counts_by_reading_time(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get email read times

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get email read times
    api_response = api_instance.get_outbound_open_counts_by_reading_time(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_open_counts_by_reading_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**DynamicResponse**](DynamicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_overview_statistics**
> OutboundOverviewStatsResponse get_outbound_overview_statistics(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get outbound overview

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get outbound overview
    api_response = api_instance.get_outbound_overview_statistics(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_outbound_overview_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**OutboundOverviewStatsResponse**](OutboundOverviewStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_counts**
> SentCountsResponse get_sent_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get sent counts

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get sent counts
    api_response = api_instance.get_sent_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_sent_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**SentCountsResponse**](SentCountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spam_complaints**
> InlineResponse2001 get_spam_complaints(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get spam complaints

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats up to the date specified. e.g. `2014-02-01` (optional)

try: 
    # Get spam complaints
    api_response = api_instance.get_spam_complaints(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_spam_complaints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracked_email_counts**
> InlineResponse2002 get_tracked_email_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)

Get tracked email counts

### Example 
```python
from __future__ import print_statement
import time
import postmark
from postmark.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postmark.StatsAPIApi()
x_postmark_server_token = 'x_postmark_server_token_example' # str | The token associated with the Server on which this request will operate.
tag = 'tag_example' # str | Filter by tag (optional)
fromdate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)
todate = '2013-10-20' # date | Filter stats starting from the date specified. e.g. `2014-01-01` (optional)

try: 
    # Get tracked email counts
    api_response = api_instance.get_tracked_email_counts(x_postmark_server_token, tag=tag, fromdate=fromdate, todate=todate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsAPIApi->get_tracked_email_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_postmark_server_token** | **str**| The token associated with the Server on which this request will operate. | 
 **tag** | **str**| Filter by tag | [optional] 
 **fromdate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 
 **todate** | **date**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

