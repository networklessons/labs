# CML to Containerlab Comparison Script

## Overview

This script (`compare_cml_containerlab.py`) identifies CML labs that don't have containerlab equivalents and suggests where the containerlab versions should be created.

## Usage

Run the script from the repository root:

```bash
python3 compare_cml_containerlab.py
```

## Output

The script generates two outputs:

1. **Console output**: Displays the comparison results directly in the terminal
2. **File output**: Saves the results to `cml_without_containerlab.txt`

### Output Format

The output shows:
- **CML Topology**: The path to the CML topology file (relative to repository root)
- **Suggested Containerlab Path**: The suggested path where the containerlab version should be created

Example:
```
CML Topology                                       Suggested Containerlab Path                       
--------------------------------------------------------------------------------
cml/BGP/bgp-4-byte-asn.yaml                        containerlab/labs/bgp/cisco/bgp-4-byte-asn/bgp-4-byte-asn.clab.yml
cml/OSPF/ospf-single-area.yaml                     containerlab/labs/ospf/cisco/ospf-single-area/ospf-single-area.clab.yml
```

## How It Works

1. **Scans CML directory**: Finds all `.yaml` topology files in the `cml/` directory
2. **Scans Containerlab directory**: Finds all `.clab.yml` files in the `containerlab/labs/` directory
3. **Normalizes names**: Converts topology names to a standard format for comparison
4. **Identifies gaps**: Finds CML labs that don't have matching containerlab versions
5. **Suggests paths**: Proposes where containerlab versions should be created based on the CML structure

## Path Mapping Convention

The script uses the following convention to suggest containerlab paths:

- CML structure: `cml/[Category]/[topology-name].yaml`
- Suggested containerlab structure: `containerlab/labs/[category]/cisco/[topology-name]/[topology-name].clab.yml`

Where:
- `[Category]` is converted to lowercase (e.g., "BGP" → "bgp")
- Spaces in category names are replaced with hyphens (e.g., "Quality of Service" → "quality-of-service")
- The vendor is assumed to be "cisco" for most labs

## Summary Statistics

The script shows:
- Total number of CML labs found
- Number of CML labs without containerlab equivalents

## Example Run

```
$ python3 compare_cml_containerlab.py
================================================================================
CML Labs without Containerlab Equivalents
================================================================================

Found 430 CML labs without containerlab equivalents
(out of 438 total CML labs)

--------------------------------------------------------------------------------
CML Topology                                       Suggested Containerlab Path                       
--------------------------------------------------------------------------------
cml/BGP/bgp-4-byte-asn.yaml                        containerlab/labs/bgp/cisco/bgp-4-byte-asn/bgp-4-byte-asn.clab.yml
...
```

## Notes

- The script performs case-insensitive name matching
- File extensions (`.yaml`, `.clab.yml`) are removed during comparison
- The `.virl.yaml` extension is also handled (legacy format)
- All suggested paths assume Cisco as the vendor; adjust as needed for other vendors
