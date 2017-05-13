# TemplateValidationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject content to validate. Must be specified if HtmlBody or TextBody are not. See our template language documentation for more information on the syntax for this field.  | [optional] 
**html_body** | **str** | The html body content to validate. Must be specified if Subject or TextBody are not. See our template language documentation for more information on the syntax for this field.  | [optional] 
**text_body** | **str** | The text body content to validate. Must be specified if HtmlBody or Subject are not. See our template language documentation for more information on the syntax for this field.  | [optional] 
**text_render_model** | **object** | The model to be used when rendering test content. | [optional] 
**inline_css_for_html_test_render** | **bool** | When HtmlBody is specified, the test render will have style blocks inlined as style attributes on matching html elements. You may disable the css inlining behavior by passing false for this parameter.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


