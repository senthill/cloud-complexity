from src.providers.aws import AWSAnalyzer
from src.providers.gcp import GCPAnalyzer

def test():
    aws = AWSAnalyzer()
    print("Testing AWS:")
    res_aws = aws.analyze_service('ec2')
    print(res_aws)

    gcp = GCPAnalyzer()
    print("\nTesting GCP:")
    res_gcp = gcp.analyze_service('compute')
    print(res_gcp)

if __name__ == "__main__":
    test()
