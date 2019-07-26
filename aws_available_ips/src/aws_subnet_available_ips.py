"""
Create an EC2 resource and determine the number of IPs available on a given subnet
"""
import boto3

EC2_RESOURCE = boto3.resource('ec2')

def get_available_ips(subnet_id):
    """Return the number of available IPs"""
    return EC2_RESOURCE.Subnet(subnet_id).available_ip_address_count
