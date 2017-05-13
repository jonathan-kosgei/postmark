# SendEmailRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | The sender email address. Must have a registered and confirmed Sender Signature. | [optional] 
**to** | **str** | Recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**cc** | **str** | Recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**bcc** | **str** | Bcc recipient email address. Multiple addresses are comma seperated. Max 50. | [optional] 
**subject** | **str** | Email Subject | [optional] 
**tag** | **str** | Email tag that allows you to categorize outgoing emails and get detailed statistics. | [optional] 
**html_body** | **str** | If no TextBody specified HTML email message | [optional] 
**text_body** | **str** | If no HtmlBody specified Plain text email message | [optional] 
**reply_to** | **str** | Reply To override email address. Defaults to the Reply To set in the sender signature. | [optional] 
**track_opens** | **bool** | Activate open tracking for this email. | [optional] 
**track_links** | **str** | Replace links in content to enable \&quot;click tracking\&quot; stats. Default is &#39;null&#39;, which uses the server&#39;s LinkTracking setting&#39;. | [optional] 
**headers** | [**HeaderCollection**](HeaderCollection.md) |  | [optional] 
**attachments** | [**AttachmentCollection**](AttachmentCollection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


