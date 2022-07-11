# cfn-saml-provider
A CloudFormation custom resource provider for adding a SAML identity provider.  

## Syntax
To create a SAML provider using your AWS CloudFormation template, use a [Custom::SAMLProvider](docs/saml-provider.md) resource with reference
to the metadata URL:

```yaml
  SAMLProvider:
    Type: Custom::SAMLProvider
    Properties:
      Name: auth0
      URL: https://auth0.com/mytenant/providerurl
      ServiceToken: !Sub 'arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:cfn-saml-provider'
```
or with the metadata itself:

```yaml
  SAMLProvider:
    Type: Custom::SAMLProvider
    Properties:
      Name: auth0
      Metadata: |
        <EntityDescriptor entityID="urn:binxio.auth0.com" xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
                ....
        </EntityDescriptor>
      ServiceToken: !Sub 'arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:cfn-saml-provider'
```

On completion, it will return the ARN of the SAML Provider.

### Deploy the provider
To deploy the provider, type:

```sh
aws cloudformation create-stack \
        --capabilities CAPABILITY_IAM \
        --stack-name cfn-saml-provider \
        --template-body file://cloudformation/cfn-saml-provider.json

aws cloudformation wait stack-create-complete  --stack-name cfn-saml-provider
```

This CloudFormation template will use our pre-packaged provider from `s3://binxio-public-${AWS_REGION}/lambdas/cfn-saml-provider-1.0.0.zip`.

## Demo
To install the simple sample of the SAML provider, type:

```sh
aws cloudformation create-stack --stack-name cfn-saml-provider-demo \
        --template-body file://cloudformation/demo-stack.json
aws cloudformation wait stack-create-complete  --stack-name cfn-saml-provider-demo
```

to validate the result, type:

```sh
aws iam list-saml-providers
```

