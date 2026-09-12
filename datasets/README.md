# Public Datasets & Data Repositories

This directory contains datasets, statistics, and public records from Australian federal government agencies.

## Available Datasets

| Dataset | Source | Format | Updated | Description |
|---------|--------|--------|---------|-------------|
| [Add datasets here] | Department | CSV | YYYY-MM-DD | Brief description |

## Dataset Categories

- **Budgets & Finances** — Spending, revenue, allocations
- **Personnel** — Staffing levels, demographics, salaries
- **Performance Metrics** — Agency KPIs, service delivery stats
- **Public Statistics** — National statistics, surveys
- **Administrative Records** — Decisions, approvals, permits issued
- **Historical Data** — Time-series, trend analysis

## Dataset Template

Each dataset should include:

```
my-dataset/
├── README.md                 # Overview and usage
├── data.csv                 # Actual data file
├── data-dictionary.md       # Field definitions
└── metadata.json            # Machine-readable metadata
```

### README.md Template

```markdown
# Dataset Name

**Source**: [[Department]]
**Collection Period**: YYYY-MM-DD to YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Update Frequency**: Daily | Weekly | Monthly | Annual
**Format**: CSV | JSON | Parquet | [Other]

## Overview
What this dataset contains and why it's important.

## How to Use
- Download instructions
- Loading examples (Python, R, SQL)
- Key fields to focus on

## Fields & Definitions
See [data-dictionary.md](./data-dictionary.md)

## Data Quality
- Known limitations
- Data gaps
- Collection methodology
- Reliability notes

## License
Public domain (CC0) unless otherwise noted.

## Contact
Questions about this dataset: [Contact info]
```

### data-dictionary.md Template

```markdown
# Data Dictionary

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| date | date | Collection date | 2026-09-12 |
| value | number | Measured value | 1234 |
| category | text | Classification | Type A |
```

### metadata.json Template

```json
{
  "name": "Dataset Name",
  "description": "Brief description",
  "source": "Department Name",
  "created": "2026-09-12",
  "updated": "2026-09-12",
  "frequency": "monthly",
  "format": "csv",
  "fields": [
    {
      "name": "field_name",
      "type": "string | number | date",
      "description": "Field description"
    }
  ],
  "license": "CC0-1.0"
}
```

## Contributing Data

To add a dataset:
1. Create a folder: `dataset-name/`
2. Include README, data files, data dictionary
3. Add metadata.json
4. Submit PR with [DATA] label

## Data Access

- **Public**: All datasets available without restriction
- **Attribution**: Please cite [[Department]] when using
- **Commercial use**: Permitted under CC0
- **API**: Future releases will include API access

---

**Last Updated**: 2026-09-12
