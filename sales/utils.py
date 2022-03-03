import uuid

# generate sales_id
def generate_transaction_id():
    return str(uuid.uuid4()).replace('-', '').upper()[:12] #remove the dash