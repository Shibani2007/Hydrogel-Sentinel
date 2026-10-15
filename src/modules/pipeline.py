from typing import List, Dict

# Required fields for COSSEN monitoring rows
REQUIRED = ['household_id','panchayat','indicator','value']

def validate_rows(rows: List[Dict]) -> List[Dict]:
    """Keep rows that have all required fields non-empty."""
    out = []
    for r in rows:
        if all(r.get(k) not in (None,'') for k in REQUIRED):
            out.append(r)
    return out

def transform_rows(rows: List[Dict]) -> List[Dict]:
    """Normalize and enrich rows for simple reporting."""
    result = []
    for r in rows:
        try:
            v = float(r['value'])
        except Exception:
            # skip rows with non-numeric values
            continue
        r2 = {
            'household_id': r['household_id'].strip(),
            'panchayat': r['panchayat'].strip().title(),
            'indicator': r['indicator'].strip().lower(),
            'value': f"{v:.2f}",
            # simple normalized metric: value per 100 households (example)
            'value_per_100': f"{(v/100):.4f}"
        }
        result.append(r2)
    return result
