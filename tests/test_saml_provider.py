import json
import uuid

import boto3
from botocore.exceptions import ClientError

from saml_provider import handler

metadata = '''<EntityDescriptor entityID="urn:mvanholsteijn.eu.auth0.com" xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
  <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <KeyDescriptor use="signing">
      <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">
        <X509Data>
          <X509Certificate>MIICsjCCAZqgAwIBAgIJaqWEM+WWXxFJMA0GCSqGSIb3DQEBBQUAMAAwHhcNMTYwMTA0MTQzNjQ3WhcNMjkwOTEyMTQzNjQ3WjAAMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtPbIvSsliCGVS3g++KcXwzAATBtHT5YN1bUbisW7n16Ri0IzXLWCyeGdEtvzMr78aCQQ5IfRx1LGJc3x4JTFRJY5x5vpQrkUfmpVdly3sPmpD4oo4Q6qQy8WDOmskplHRevbkVj6QXFp571JpNyzq6+s22Kjp01btA17OhJEBrrFlIYZIDfH/zm4EEABL5UBSpXCJEjkxBkXbmPRbyyfGWxX4vDVNFar7J8PdOg4D7Wvhunug8mWeMIHurs+ZzwEc/CW1yqE2d/J9SG7jJD5dXLeKZeasjtPDDbHqoNc4qk9kfc2pWiPByYG/1wx3QXY/0of0ENUvqg3lLcTSmYetwIDAQABoy8wLTAMBgNVHRMEBTADAQH/MB0GA1UdDgQWBBSHkjmCxyhXEn4IZX8PltaoZtN5VTANBgkqhkiG9w0BAQUFAAOCAQEAD9bcO+YYz8bluf6kx3k3MsnsbD5Vat2Q49l46mdMI+gfqI9Q0iHOSVLwYoPOHqO2a3wuNVyz5kTsAJfPWaZpuiTZt+bkp4ZUQU5bsdtNQfZOvIhI8sIvI+bYKGgU3Q4DH2HslubH3Wrw07rFHIbsRlf2eOhPgH4E9cOONNgivwCyT5YlNAbk5ZdRvFvtigX5O3voMiVZfU+B+RPPMe7owYIboDEPy9murdoaF2GnoP3TMDtkAsdbd/DvsHtHyKOfSWTr6Ls7x3wWJ6+T7YO+qpyMm5guffOfX4kahyi2akOdIb806CbZ+WGnKRsSvx0u9Ps3PkNNxjVDcNJqmeXWgQ==</X509Certificate>
        </X509Data>
      </KeyInfo>
    </KeyDescriptor>
    <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://mvanholsteijn.eu.auth0.com/samlp/SLeL10SEptRHmDPNXtKLXyHwZSGlrMZU/logout"/>
    <SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://mvanholsteijn.eu.auth0.com/samlp/SLeL10SEptRHmDPNXtKLXyHwZSGlrMZU/logout"/>
    <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
    <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>
    <NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
    <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://mvanholsteijn.eu.auth0.com/samlp/SLeL10SEptRHmDPNXtKLXyHwZSGlrMZU"/>
    <SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://mvanholsteijn.eu.auth0.com/samlp/SLeL10SEptRHmDPNXtKLXyHwZSGlrMZU"/>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="E-Mail Address" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="Given Name" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="Name" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="Surname" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>
    <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri" FriendlyName="Name ID" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"/>
  </IDPSSODescriptor>
</EntityDescriptor>
'''


def test_create_with_url():
    # create with url
    name = 'n%s' % uuid.uuid4()
    request = Request('Create', name, 'https://mvanholsteijn.eu.auth0.com/samlp/metadata/44dxGEx0lDr1cpPzBwr7jv9IyWcHGSiY')
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response
    physical_resource_id = response['PhysicalResourceId']

    # update
    request = Request('Update', name, metadata, physical_resource_id)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response

    # delete
    request = Request('Delete', {}, physical_resource_id)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']


def test_create_with_bad_url():
    name = 'n%s' % uuid.uuid4()
    request = Request('Create', name, 'http://does-not-exist')
    response = handler(request, {})
    assert response['Status'] == 'FAILED', response['Reason']
    assert 'PhysicalResourceId' in response
    assert response['PhysicalResourceId'] == 'could-not-create'


def test_create_with_bad_metadata():
    name = 'n%s' % uuid.uuid4()
    request = Request('Create', name, '<geen>' + (' ' * 1000) + '</geen>')
    response = handler(request, {})
    assert response['Status'] == 'FAILED', response['Reason']
    assert 'PhysicalResourceId' in response
    assert response['PhysicalResourceId'] == 'could-not-create'


def test_create_with_metadata():
    # create with metadata
    name = 'n%s' % uuid.uuid4()
    request = Request('Create', name, metadata)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response
    physical_resource_id = response['PhysicalResourceId']

    # update
    request = Request(
        'Update', name, 'https://mvanholsteijn.eu.auth0.com/samlp/metadata/44dxGEx0lDr1cpPzBwr7jv9IyWcHGSiY', physical_resource_id)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']
    assert 'PhysicalResourceId' in response

    # delete
    request = Request('Delete', {}, physical_resource_id)
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']


def test_delete_incorrect_physical_resource_id():
    request = Request('Delete', {}, 'devapi-consumeradmin-ManageOwnConsumersPermission-Y38O818GY2PV')
    response = handler(request, {})
    assert response['Status'] == 'SUCCESS', response['Reason']


class Request(dict):

    def __init__(self, request_type, name, metadata, physical_resource_id=None):
        request_id = 'request-%s' % uuid.uuid4()
        self.update({
            'RequestType': request_type,
            'ResponseURL': 'https://httpbin.org/put',
            'StackId': 'arn:aws:cloudformation:us-west-2:EXAMPLE/stack-name/guid',
            'RequestId': request_id,
            'ResourceType': 'Custom::SAMLProvider',
            'LogicalResourceId': 'MyCustom',
            'ResourceProperties': {
                'Name': name
            }})

        if metadata.startswith('http'):
            self['ResourceProperties']['URL'] = metadata
        else:
            self['ResourceProperties']['Metadata'] = metadata

        self['PhysicalResourceId'] = physical_resource_id if physical_resource_id is not None else 'initial-%s' % str(uuid.uuid4())
