from invoiceExtractor import extract_data
from invoiceExtractor.extract.loader import read_templates

templates = read_templates('tpl')
result = extract_data('../invoices/inv2.pdf', templates=templates)

print(result)