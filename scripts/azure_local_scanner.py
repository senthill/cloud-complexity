import os
import json
from collections import defaultdict

def count_in_spec(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            spec = json.load(f)
            
        paths = spec.get("paths", {})
        ops = 0
        attrs = 0
        
        for path, methods in paths.items():
            if not isinstance(methods, dict): continue
            for method, details in methods.items():
                if method.lower() in ["get", "post", "put", "delete", "patch"]:
                    ops += 1
                    params = details.get("parameters", [])
                    attrs += len(params)
                    
        return ops, attrs
    except:
        return 0, 0

def run_scanner(base_dir):
    print(f"Scanning {base_dir}...")
    summary = defaultdict(lambda: {"apis": 0, "attributes": 0})
    total_files = 0
    
    # Structure: specification/{category}/resource-manager/{service}/stable/{version}/*.json
    for root, dirs, files in os.walk(base_dir):
        if "stable" in root and "resource-manager" in root:
            # We are inside a stable folder. Root might be .../stable/2024-03-01
            # Or root is .../stable and dirs contains the versions.
            
            # If root ends in 'stable', we need to pick the latest dir
            if root.endswith("stable") and dirs:
                latest_version = sorted(dirs)[-1]
                version_path = os.path.join(root, latest_version)
                # Count everything in this version
                for f in os.listdir(version_path):
                    if f.endswith(".json") and "client" not in f.lower():
                        ops, attrs = count_in_spec(os.path.join(version_path, f))
                        # Identify provider from path
                        parts = root.split(os.sep)
                        # Expecting something like ['...', 'specification', 'compute', 'resource-manager', 'Microsoft.Compute', 'stable']
                        try:
                            spec_idx = parts.index("specification")
                            provider = parts[spec_idx + 1]
                        except:
                            provider = "unknown"
                            
                        summary[provider]["apis"] += ops
                        summary[provider]["attributes"] += attrs
                        total_files += 1
    
    print(f"\nScan Complete. Processed {total_files} active spec files.\n")
    print(f"{'Provider':<20} | {'APIs':<10} | {'Attributes':<10}")
    print("-" * 45)
    
    all_apis = 0
    all_attrs = 0
    for provider, stats in sorted(summary.items(), key=lambda x: x[1]["apis"], reverse=True):
        print(f"{provider:<20} | {stats['apis']:<10} | {stats['attributes']:<10}")
        all_apis += stats["apis"]
        all_attrs += stats["attributes"]
        
    print("-" * 45)
    print(f"{'TOTAL (ACTIVE)':<20} | {all_apis:<10} | {all_attrs:<10}")

if __name__ == "__main__":
    import sys
    base_path = sys.argv[1] if len(sys.argv) > 1 else "."
    run_scanner(base_path)
