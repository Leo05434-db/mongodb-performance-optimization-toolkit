# MongoDB Production Performance & Diagnostic Toolkit

A collection of production-safe, non-destructive diagnostic tools designed to audit MongoDB cluster performance, isolate query bottlenecks, and tune WiredTiger storage parameters.

## 🚀 The Core Problem
This repository provides an automated, production-safe diagnostic gateway to audit NoSQL document databases in under 60 seconds without installing heavy, invasive monitoring agents.

---

## 🎁 Free Teaser: Python MongoDB Cache & Connection Monitor
Copy and save this read-only Python script. It utilizes `pymongo` to safely connect to your cluster and print out real-time client connection footprints and WiredTiger memory utilization.

```python
import pymongo

def check_mongodb_health(connection_string="mongodb://localhost:27017/", db_name="production_db"):
    try:
        client = pymongo.MongoClient(connection_string, serverSelectionTimeoutMS=2000)
        db = client[db_name]
        
        status = db.command("serverStatus")
        
        print(f"=== MongoDB Health Summary: {db_name} ===")
        print(f"Active Client Connections: {status['connections']['current']}")
        print(f"Uptime: {status['uptime']} seconds")
        
        wt_cache = status['wiredTiger']['cache']
        max_bytes = wt_cache['maximum bytes configured']
        used_bytes = wt_cache['bytes currently in the cache']
        print(f"WiredTiger Cache Utilization: {round((used_bytes / max_bytes) * 100, 2)}%")
        
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    check_mongodb_health()
```

---

## ⚡ Unlock the Full Automation Bundle ($39)
While basic memory footprints highlight global cluster health, isolating the exact shapes of queries forcing full collection scans requires the complete utility suite.

The complete, production-ready toolkit includes the critical scripts required to fully optimize your infrastructure:

### 📦 What's Included in the Full Premium Kit:
*   **01_mongodb_index_and_collscan_inspector.js:** Locates queries causing massive collection scans (COLLSCAN) on disk and flags dead custom indexes wasting RAM.
*   **02_mongodb_wiredtiger_cache_health.js:** Evaluates deep internal memory data states to track pages read/written to storage media.
*   **03_mongodb_storage_compactor_fragmentation.js:** Calculates wasted storage page overhead from updates and deletions so you can run target compactions and shrink your host server bill.
*   **04_mongodb_slow_operation_profiler_aggregator.js:** Ranks your top 5 heaviest query shapes and aggregation pipelines by cumulative running runtime.

👉 [Download the Full Production MongoDB Toolkit on Gumroad for $39](https://leonova027.gumroad.com/l/mongodb-performance-toolkit)

---
*Maintained by @Leo05434-db. For NoSQL architecture optimization, aggregation pipeline tuning, or scale cluster layout support, contact: leo05434@proton.me.*
