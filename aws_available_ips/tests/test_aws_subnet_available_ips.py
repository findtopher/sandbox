"""
Test the aws_subnet_available_ips module
"""
# pylint: disable=redefined-outer-name
from botocore.stub import Stubber
import src.aws_subnet_available_ips as app
from src.aws_subnet_available_ips import EC2_RESOURCE

SUBNET_ID = "subnet-12345678"

RESPONSE = {
    "Subnets": [
        {
            "AvailabilityZone": "us-east-1a",
            "AvailabilityZoneId": "use1-az4",
            "AvailableIpAddressCount": 326,
            "CidrBlock": "10.1.1.0/23",
            "DefaultForAz": False,
            "MapPublicIpOnLaunch": True,
            "State": "available",
            "SubnetId": SUBNET_ID,
            "VpcId": "vpc-12345678",
            "OwnerId": "123456789123",
            "AssignIpv6AddressOnCreation": False,
            "Ipv6CidrBlockAssociationSet": [],
            "Tags": [{"Key": "Name", "Value": "topher-test"}],
            "SubnetArn": "arn:aws:ec2:us-east-1:123456789123:subnet/subnet-12345678",
        }
    ]
}


def test_getting_available_ips():
    """Test, using Stubber, to validate that we get the expected number of available IPs"""
    expected_params = {"SubnetIds": [SUBNET_ID]}
    with Stubber(EC2_RESOURCE.meta.client) as stubber:
        stubber.add_response("describe_subnets", RESPONSE, expected_params)
        available_ips = app.get_available_ips(SUBNET_ID)

        assert available_ips == 326
