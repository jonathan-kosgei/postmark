# OutboundMessageDetailsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_body** | **str** |  | [optional] 
**html_body** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**to** | [**list[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**cc** | [**list[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**bcc** | [**list[EmailNameAddressPair]**](EmailNameAddressPair.md) |  | [optional] 
**recipients** | **list[str]** |  | [optional] 
**received_at** | **datetime** |  | [optional] 
**_from** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**attachments** | [**AttachmentCollection**](AttachmentCollection.md) |  | [optional] 
**status** | **str** |  | [optional] 
**track_opens** | **bool** |  | [optional] 
**track_links** | **str** |  | [optional] 
**message_events** | [**list[MessageEventDetails]**](MessageEventDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


