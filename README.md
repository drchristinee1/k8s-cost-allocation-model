# Kubernetes Cost Allocation Model

A FinOps modeling prototype that allocates Kubernetes cluster cost to namespaces based on resource usage and shared infrastructure overhead.

---

## Purpose

Kubernetes introduces a fundamental FinOps challenge:

> Infrastructure is shared, but accountability must be assigned.

Unlike traditional cloud services, Kubernetes clusters pool compute, memory, and storage across multiple teams and workloads.

This project answers a critical question:

**How do we translate shared cluster cost into fair, actionable, namespace-level ownership?**

---

## What this model does

This model:

- ingests namespace-level usage data (CPU, memory, storage)
- applies pricing assumptions to estimate cost
- calculates direct cost per namespace
- allocates shared cluster overhead proportionally
- outputs total cost by namespace

---

## Why this matters

Without proper allocation:

- teams cannot see the cost of their workloads  
- shared infrastructure becomes invisible spend  
- optimization responsibility is unclear  

With allocation:

- cost becomes attributable  
- engineering teams gain visibility  
- FinOps enables accountability and optimization  

---

## Allocation approach

The model follows a simple but practical approach:

### 1. Direct cost calculation

Each namespace is charged for:

- CPU usage (CPU hours)
- Memory usage (GB-hours)
- Storage usage (GB)

---

### 2. Shared cluster overhead

Cluster-level costs such as:

- control plane
- networking
- idle capacity
- platform tooling

are treated as **shared cost**

---

### 3A. Allocation rule for shared idle capacity

Idle capacity represents unused cluster resources such as underutilized nodes or over-provisioned capacity.

In this model, idle capacity is treated as part of shared cluster overhead and is allocated proportionally across namespaces based on their share of direct resource consumption.

```text
idle_share = namespace_direct_cost / total_direct_cost
allocated_idle_cost = idle_share × total_idle_cost

```text
This approach ensures:

all workloads share responsibility for unused capacity
cost remains fully distributed (no unassigned spend)
the model remains simple and explainable
Alternative approaches (future enhancement)

In more advanced models, idle capacity can be:

separated as a platform cost (not allocated to teams)
charged as a fixed “platform tax”
exposed as unallocated spend to highlight inefficiency

This allows organizations to choose between:

fairness (proportional allocation)
visibility (explicit idle cost tracking)

### 4. Final cost
namespace_share = namespace_direct_cost / total_direct_cost
allocated_shared_cost = namespace_share × total_shared_cost

### Architecture
Namespace Usage → Pricing Model → Direct Cost → Shared Cost Allocation → Namespace Cost

Example input
[
  {
    "namespace": "payments",
    "cpu_hours": 1200,
    "memory_gb_hours": 2400,
    "storage_gb": 500
  },
  {
    "namespace": "analytics",
    "cpu_hours": 800,
    "memory_gb_hours": 1800,
    "storage_gb": 300
  }
]
Example output
{
  "payments": 8420,
  "analytics": 5580
}
Repository structure
k8s-cost-allocation-model/
├── README.md
├── main.py
├── k8s_allocation/
│   ├── __init__.py
│   ├── loader.py
│   ├── pricing.py
│   └── allocator.py
├── data/
│   └── sample_namespace_usage.json
├── outputs/
│   └── namespace_allocation_output.json

Current scope

Version 1 focuses on:

namespace-level allocation

CPU, memory, and storage cost modeling
proportional shared cost distribution

Future enhancements

integration with Prometheus / Kubernetes metrics
node-level and pod-level allocation
idle capacity tracking
cost per workload / per service
integration with Kubecost or cloud billing data
multi-cluster cost aggregation

Key takeaway

Kubernetes shifts cloud cost from:

isolated services
to
shared infrastructure systems

FinOps must therefore shift from:

cost visibility
to
cost attribution and ownership

This model represents that transition.
