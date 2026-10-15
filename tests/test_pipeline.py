from src.modules.pipeline import validate_rows, transform_rows

SAMPLE = [
    {'household_id':'H001','panchayat':'Northpanchayat','indicator':'RainwaterSystems','value':'12'},
    {'household_id':'H005','panchayat':'Eastpanchayat','indicator':'TrainingPlaced','value':''},
    {'household_id':'H006','panchayat':'Westpanchayat','indicator':'RainwaterSystems','value':'8'}
]

def test_validate_rows():
    valid = validate_rows(SAMPLE)
    assert len(valid) == 2
    assert all('household_id' in r for r in valid)

def test_transform_rows():
    valid = validate_rows(SAMPLE)
    out = transform_rows(valid)
    assert out[0]['panchayat'] == 'Northpanchayat'
    assert out[0]['indicator'] == 'rainwatersystems'
    assert out[0]['value_per_100'] == '0.1200'
