import pyspark
from invoiceExtractor import extract_data
from invoiceExtractor.main import analize_data
from invoiceExtractor.extract.loader import read_templates
import re, os

CURRENT_DIR = os.path.dirname(__file__)
TPL_DIR = os.path.join(CURRENT_DIR, 'tpl')
INVOICES_DIR = os.path.join(CURRENT_DIR, 'invoices')
TEMPLATES = read_templates(TPL_DIR)

ANALIZED_DATA = []

for invoice in os.listdir(INVOICES_DIR):
    result = extract_data(os.path.join(INVOICES_DIR, invoice), templates=TEMPLATES)
    ANALIZED_DATA.append(analize_data(result))

print(ANALIZED_DATA)
