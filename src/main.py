from services.service import add_document, delete_document, update_document
from models.Transaction import Transaction, PaymentMethod

test = Transaction(
    CodCli=1,
    Cpf="12345678901",
    Name="Fabrizio",
    Price=10,
    Company="Apple",
    Product="Iphone X",
    PaymentMethod="Debit Card"
)

# update_document(140725041765080, {"Name": "Juju"})
# add_document(test)
# update_document(document=test, new_valor={"PaymentMethod": test.PaymentMethod})
delete_document(1)
