# CloudComplexity

CloudComplexity is a Command Line Interface (CLI) tool designed to compare cloud APIs across major cloud providers (AWS, GCP, Azure, and Alibaba). By analyzing API specifications, it provides insights into the complexity and scale of equivalent services across different cloud ecosystems.

The tool compares services based on:
- **Total APIs:** The number of distinct API operations available for a service.
- **Total Verbs:** The number of HTTP methods (GET, POST, PUT, etc.) or distinct actions.
- **Total Attributes:** The number of configurable parameters or request input attributes.

## Features

- **Cross-Provider Comparison:** Compare equivalent services (e.g., "compute" maps to AWS EC2, GCP Compute Engine, Azure Compute, and Alibaba ECS).
- **Extensible Architecture:** Providers are implemented as independent analyzers extending a common `ProviderAnalyzer` base class.
- **Dynamic Analysis:** 
  - AWS is analyzed dynamically utilizing `botocore` service models.
  - Other providers (GCP, Azure, Alibaba) utilize OpenAPI specification parsing.
- **Rich CLI Output:** Presents metrics in a beautiful, easy-to-read console table using the `rich` library.

## Project Structure

```
cloudcomplexity/
├── requirements.txt         # Project dependencies
├── specs/                   # Directory containing downloaded OpenAPI specs for GCP, Azure, and Alibaba
└── src/
    ├── main.py              # CLI entry point using Click and Rich
    ├── schema.py            # Pydantic data models for API metrics (APIMetrics, ServiceComparison)
    ├── mappings.py          # Dictionary mapping generic categories to provider-specific services
    └── providers/
        ├── base.py          # Abstract base class for all provider analyzers
        ├── aws.py           # AWS analyzer utilizing botocore
        ├── gcp.py           # Google Cloud Platform analyzer
        ├── azure.py         # Microsoft Azure analyzer
        ├── alibaba.py       # Alibaba Cloud analyzer
        └── openapi.py       # Utility for parsing standard OpenAPI specifications
```

## API Specification Sources

To ensure accuracy, CloudComplexity sources API specifications directly from the same machine-readable definitions used by the cloud providers to generate their official SDKs:

- **AWS (Amazon Web Services):** Uses `botocore` internal models, which are the exact structural JSON definitions used to power the AWS CLI and `boto3`.
- **GCP (Google Cloud Platform):** Fetches definitions from the official [Google API Discovery Service](https://developers.google.com/discovery), which Google uses to build their client libraries.
- **Azure (Microsoft Azure):** Parses OpenAPI (Swagger) specifications sourced from Microsoft's [azure-rest-api-specs](https://github.com/Azure/azure-rest-api-specs) GitHub repository.
- **Alibaba Cloud:** Evaluates proprietary `api-docs.json` specifications, which serve as the canonical source for their OpenAPI Explorer and SDK generation.

## Setup and Installation

1. **Clone the repository** and navigate to the project directory:
   ```bash
   cd cloudcomplexity
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Dependencies include `click`, `pydantic`, `requests`, `botocore`, and `rich`.*

4. **Prepare OpenAPI Specs:**
   For providers that rely on standard OpenAPI specifications (GCP, Azure, Alibaba), ensure you have downloaded the relevant `.json` spec files into the `specs/` directory.

5. **AWS Credentials:**
   The AWS analyzer requires valid AWS credentials in your environment (e.g., via `~/.aws/credentials` or environment variables) so `botocore` can load the service models.

## Usage

Run the CLI tool by passing a service category to compare.

```bash
python -m src.main <category>
```

### Examples

Compare **compute** services (AWS EC2, GCP Compute, Azure Compute, Alibaba ECS):
```bash
python -m src.main compute
```

Compare **storage** services (AWS S3, GCP Storage, Azure Storage, Alibaba OSS):
```bash
python -m src.main storage
```

### Output

The tool will output an `API Metrics Comparison` table in your terminal:

```
Comparing API metrics for category: Compute
Analyzing AWS (ec2)...
Analyzing GCP (compute)...
Analyzing AZURE (compute)...
Analyzing ALIBABA (ecs)...

                        API Metrics Comparison: Compute                         
┏━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Provider ┃ Service ┃ Total APIs ┃ Total Verbs ┃ Total Attributes ┃
┡━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ AWS      │ ec2     │        xxx │         xxx │              xxx │
│ GCP      │ compute │        xxx │         xxx │              xxx │
│ AZURE    │ compute │        xxx │         xxx │              xxx │
│ ALIBABA  │ ecs     │        xxx │         xxx │              xxx │
└──────────┴─────────┴────────────┴─────────────┴──────────────────┘
```

## Adding a New Provider

1. Create a new analyzer file in `src/providers/` (e.g., `digitalocean.py`).
2. Implement a class inheriting from `ProviderAnalyzer` in `src/providers/base.py`.
3. Override the `analyze_service` method to return an `APIMetrics` object.
4. If relying on OpenAPI, you can leverage the helper `parse_openapi_spec` in `src/providers/openapi.py`.
5. Register the new analyzer in the `analyzers` dict inside `src/main.py` and update `SERVICE_MAPPINGS` in `src/mappings.py`.
