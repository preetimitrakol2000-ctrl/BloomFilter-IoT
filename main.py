from security import extract_device_id
from filter import IoTBloomFilter

if __name__ == "__main__":
    print("🔒 Initializing BloomFilter-IoT Security Firewalls...")

    firewall_filter = IoTBloomFilter(size=128)
    
    # Authorize trusted edge node signatures
    firewall_filter.authorize_identity(extract_device_id("Sensor_Node_Alpha"))
    firewall_filter.authorize_identity(extract_device_id("Gateway_Beta"))

    # Test incoming device signatures
    test_device_A = "Sensor_Node_Alpha"
    test_device_B = "Rogue_Malicious_Device"

    match_A = firewall_filter.evaluate_membership(extract_device_id(test_device_A))
    match_B = firewall_filter.evaluate_membership(extract_device_id(test_device_B))

    print(f"\n📡 Testing Connection: Identity -> \"{test_device_A}\"")
    print(f"   🔮 Firewall Lookup Verdict: {'✅ MATCH FOUND (ALLOW CONNECT)' if match_A else '🚨 ACCESS DENIED'}")

    print(f"\n📡 Testing Connection: Identity -> \"{test_device_B}\"")
    print(f"   🔮 Firewall Lookup Verdict: {'✅ MATCH FOUND (ALLOW CONNECT)' if match_B else '🚨 COLD ACCESS DENIED (UNRECOGNIZED SIGNATURE)'}")
