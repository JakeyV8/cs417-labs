from parser import parse_product_basic, parse_availability

def test_parse_product_basic_extracts_id(valid_product):
    gather_id = parse_product_basic(valid_product)
    assert valid_product["id"] == gather_id["id"]
    

def test_parse_product_basic_extracts_name(valid_product):
    gather_name = parse_product_basic(valid_product)
    assert valid_product["name"] == gather_name["name"]

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    gather = parse_product_basic(valid_product)
    extract = ["id","name"]
    New_gather ={k:gather[k]for k in extract}
    New_prod ={k:valid_product[k]for k in extract}
    assert New_prod == New_gather

