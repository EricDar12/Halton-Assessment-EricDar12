# Data Exploration
*Adding context to a large dataset.*

##### [Table of Contents](../README.md) | [Next Page](02-cleaning.md)
---

## Defining the Data:
- Contains **Government of Canada** contract disclosure records.
- Federal departments and agencies publish these records as part of government transparency requirements.
- Provides accountability and visibility into government spending.
- Contracts over $10,000, the disclosure threshold for federal contracts.
- Each record represents a single contract award:
    - Descriptive information about the vendor.
    - Contracting government organization.
    - Initial value of the contract and amendments.
    - Category of goods/services being purchased.

---

## The Dataset:

The provided dataset contains over **1.2 million** entries. With **43** database columns including:
- **Vendor name:** The company awarded the contract.
- **Buyer name:** The government organization or department issuing the contract.
- **Contract Value:** The monetary value of the contract including amendments.
- **Contract Date:** The date the contract was awarded.
- **Commodity Code:** Classification code (GSIN) describing the type of goods or services provided.
- And many, many more columns.

---

## Focus:

Because of the sheer size of this dataset, many different valuable perspectives can be explored. Attepting to prepare every column for every possible question would introduce unnecessary complexity and slow the analytical process.

Instead, the analysis follows a **question-driven approach**: the insights being explored determine which parts of the dataset require preparation and cleaning.

Before transforming the data, I first explored the dataset at a high level to understand what kinds of questions it could answer. From that exploration, several areas of interest emerged, such as:

- How federal procurement spending is distributed across vendors.
- Which organizations issue the most contracts.
- How contract counts compare to total contract value.
- What categories of goods and services appear most frequently.
- What percentage of total contracts are awarded to indigenous businesses.

