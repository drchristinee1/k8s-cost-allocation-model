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

### 3. Proportional allocation

Shared cost is distributed based on each namespace’s share of total direct cost:

```text
namespace_share = namespace_direct_cost / total_direct_cost
allocated_shared_cost = namespace_share × total_shared_cost
