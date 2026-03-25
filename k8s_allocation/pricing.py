def get_pricing():
    """
    Sample pricing model for Kubernetes resource usage.

    These are simplified rates for modeling purposes.
    In a real system, these would be derived from:
    - node instance costs
    - storage pricing
    - networking / platform overhead
    """

    return {
        # Cost per CPU hour
        "cpu_per_hour": 0.05,

        # Cost per GB RAM hour
        "memory_per_gb_hour": 0.01,

        # Cost per GB storage (monthly simplified to unit rate)
        "storage_per_gb": 0.02,

        # Total shared cluster overhead
        # (control plane, networking, idle capacity, etc.)
        "shared_cluster_cost": 5000
    }
