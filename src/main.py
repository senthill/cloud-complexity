import click
from rich.console import Console
from rich.table import Table
from src.mappings import SERVICE_MAPPINGS

from src.providers.aws import AWSAnalyzer
from src.providers.gcp import GCPAnalyzer
from src.providers.azure import AzureAnalyzer
from src.providers.alibaba import AlibabaAnalyzer
from src.providers.vmware import VMWareAnalyzer
from src.providers.nutanix import NutanixAnalyzer
from src.providers.vercel import VercelAnalyzer
from src.providers.netlify import NetlifyAnalyzer
from src.providers.heroku import HerokuAnalyzer
from src.providers.render import RenderAnalyzer
from src.providers.fly import FlyAnalyzer
from src.providers.digitalocean import DigitalOceanAnalyzer
from src.providers.railway import RailwayAnalyzer
from src.providers.vps import VPSAnalyzer

console = Console()

@click.command()
@click.argument('category', type=str)
def compare_api(category: str):
    """
    Compare cloud APIs for a given service category.
    Example categories: compute, storage
    """
    category = category.lower()
    
    if category == 'all':
        categories_to_run = list(SERVICE_MAPPINGS.keys())
    elif category not in SERVICE_MAPPINGS:
        console.print(f"[red]Error: Unknown category '{category}'. Available categories: {', '.join(SERVICE_MAPPINGS.keys())}, all[/red]")
        return
    else:
        categories_to_run = [category]

    # Initialize analyzers
    analyzers = {
        "aws": AWSAnalyzer(),
        "gcp": GCPAnalyzer(),
        "azure": AzureAnalyzer(),
        "alibaba": AlibabaAnalyzer(),
        "vmware": VMWareAnalyzer(),
        "nutanix": NutanixAnalyzer(),
        "vercel": VercelAnalyzer(),
        "netlify": NetlifyAnalyzer(),
        "heroku": HerokuAnalyzer(),
        "render": RenderAnalyzer(),
        "fly": FlyAnalyzer(),
        "digitalocean": DigitalOceanAnalyzer(),
        "railway": RailwayAnalyzer(),
        "vps": VPSAnalyzer()
    }

    for cat in categories_to_run:
        console.print(f"\n[blue]Comparing API metrics for category: {cat.title()}[/blue]")
        
        table = Table(title=f"API Metrics Comparison: {cat.title()}")
        table.add_column("Provider", style="cyan", no_wrap=True)
        table.add_column("Service", style="magenta")
        table.add_column("Total APIs", justify="right", style="green")
        table.add_column("Total Verbs", justify="right", style="green")
        table.add_column("Total Attributes", justify="right", style="green")
        
        mapping = SERVICE_MAPPINGS[cat]
        
        for provider_id, analyzer in analyzers.items():
            mapping_val = mapping.get(provider_id)
            
            if not mapping_val:
                # If provider is defined in the system but doesn't have this service category
                table.add_row(analyzer.get_name(), "N/A", "N/A", "N/A", "N/A")
                continue
                
            if isinstance(mapping_val, dict):
                service_name = mapping_val["service"]
                filter_keywords = mapping_val.get("filter_keywords")
            else:
                service_name = mapping_val
                filter_keywords = None
                
            console.print(f"Analyzing {analyzer.get_name()} ({service_name})...")
            metrics = analyzer.analyze_service(service_name, filter_keywords=filter_keywords)
            
            if metrics:
                table.add_row(
                    metrics.provider,
                    metrics.service_name,
                    str(metrics.total_apis),
                    str(metrics.total_verbs),
                    str(metrics.total_attributes)
                )
            else:
                table.add_row(analyzer.get_name(), service_name, "N/A", "N/A", "N/A")
                
        console.print(table)

if __name__ == '__main__':
    compare_api()
