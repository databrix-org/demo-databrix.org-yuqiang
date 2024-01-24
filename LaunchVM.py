import boto3
import webbrowser  
import time

# Function to start VM

def launch_tljh():
    
    # Replace these with your AWS credentials and instance ID
    # for security, the credential is deleted
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_region = ''
    instance_id = ''
    
    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    
    # Start VM
    print(f"Starting instance '{instance_id}'...")
    ec2.start_instances(InstanceIds=[instance_id])
    print('successfully started')
    return 0


# After Starting the VM, User need the URL of TLJH
# Search and open the URL of TLJH
# After 1-2 min, User can successfully open the URL
def search_publicip():
    
    # for security, the credential is deleted
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_region = ''
    instance_id = ''
    
    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    
    # Retrieve the details of the VM
    response = ec2.describe_instances(InstanceIds=[instance_id])

    # Retrieve the details of the VM
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        
        # Search IP Address 
        public_ip_address = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
        
        # Format URL
        url = f'http://{public_ip_address}'
        
        # Open the URL in the default browser
        if not webbrowser.open(url):
            raise Exception("Web browser could not be opened.")
        
    except Exception as e:
        print(f'Error: {e}')
        return -1

    return 0

# Stop VM after using
def stop_tljh():

        
    
    # Replace these with your AWS credentials and instance ID
    # for security, the credential is deleted
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_region = ''
    instance_id = ''
    
    # Create an EC2 client
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    

    try:
    # Stop the instance
        print(f"Stopping instance '{instance_id}'...")
        ec2.stop_instances(InstanceIds=[instance_id])
        print('successfully stopped')
        
        
    except:
        print('error at stopping')

    return 0