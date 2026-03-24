from src.providers.azure import AzureAnalyzer

def test():
    az = AzureAnalyzer()
    print("Testing Azure:")
    res = az.analyze_service('compute')
    print(res)

if __name__ == "__main__":
    test()
