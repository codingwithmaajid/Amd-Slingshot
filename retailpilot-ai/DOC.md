# RetailPilot AI - System Documentation

## Overview
RetailPilot AI is an autonomous decision engine for retail operations. It eliminates manual intervention by automatically determining fulfillment paths based on real-time inventory states.

## Decision Logic (Deterministic Engine)
1. **Request Received**: System accepts a product ID or Name.
2. **Inventory Lookup**: Checks `data/sample.json`.
3. **Branching Logic**:
   - **Scenario A: In Stock (Stock > 0)**
     - Result: `FULFILLED`
     - Action: Decrement inventory, generate invoice.
   - **Scenario B: Out of Stock (Stock == 0)**
     - Result: `OUT_OF_STOCK`
     - Action: Trigger `RESTOCK_PROCEDURE` (Supplier API notification), search for `SUBSTITUTE_ID`.
   - **Scenario C: Missing Item**
     - Result: `ERROR`
     - Action: Request manual catalog update.

## Data Schema
```json
{
  "product_id": "string",
  "name": "string",
  "stock": 0,
  "substitute_id": "string",
  "restock_threshold": 5
}
```