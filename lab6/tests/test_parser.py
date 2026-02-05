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

def test_parse_availability_when_in_stock(valid_product):
    product = parse_availability(valid_product)
    if product["in_stock"] == True:
        assert True
    else: 
        assert False

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    product = parse_availability(product_out_of_stock)
    if product["in_stock"] == False:
        assert True
    else:
        assert False
