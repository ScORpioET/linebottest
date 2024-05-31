import boto3
fraudDetector = boto3.client('frauddetector')
            
response = fraudDetector.get_detectors()
print(response)
