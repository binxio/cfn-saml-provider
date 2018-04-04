# Custom::SAMLProvider
The `Custom::SAMLProvider` creates IAM SAM Provider.

## Syntax
To declare this entity in your AWS CloudFormation template, use the following syntax:

```yaml
  Type : Custom::SAMLProvider
  Properties
    Name: String
    Metadata: String
    URL: url
    ServiceToken" : !Sub 'arn:aws:lambda:${AWS::Region}:${AWS::AccountId}:function:cfn-saml-provider'
```

It will create a SAML provider named `Name` using the `Metadata` literal or the content
of the metadata `URL`.

## Properties
You can specify the following properties:

    "Name" - of the SAML provider (required)
    "Metadata" - for the SAML Provider (required if URL is missing)
    "URL" - serving the metadata of the SAML Provider (required if Metadaga is missing)
    "ServiceToken" - pointing to the function implementing this (required)

## Return values
The physical resource id is the ARN of the provider. There are no additional return attributes.



