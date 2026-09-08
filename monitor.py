# ========================================================================
# MONGODB TOOLKIT: AUTOMATED PYTHON HEALTH CHECK
# Requires: pip install pymongo
# ========================================================================
import pymongo
from pprint import pprint

def check_mongodb_health(connection_string, db_name):
    try:
        client = pymongo.MongoClient(connection_string, serverSelectionTimeoutMS=2000)
        db = client[db_name]
        
        # Pull overall server telemetry
        status = db.command("serverStatus")
        
        print(f"=== MongoDB Health Summary: {db_name} ===")
        print(f"Active Client Connections: {status['connections']['current']}")
        print(f"Uptime: {status['uptime']} seconds")
        
        # Check WiredTiger configuration memory allocation
        wt_cache = status['wiredTiger']['cache']
        max_bytes = wt_cache['maximum bytes configured']
        used_bytes = wt_cache['bytes currently in the cache']
        print(f"WiredTiger Cache Efficiency: {round((used_bytes / max_bytes) * 100, 2)}% utilized")
        
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    # Example usage
    check_mongodb_health("mongodb://localhost:27017/", "production_db")
