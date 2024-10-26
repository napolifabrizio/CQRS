from services.service import add_document, delete_document, update_document
from models.Transaction import Transaction, PaymentMethod

test = Transaction(
    CodCli=id(10),
    Cpf="12345678901",
    Name="Fabrizio",
    Price=10,
    Company="Apple",
    Product="Iphone X",
    PaymentMethod="Credit Card"
)

update_document(140725041765080, {"Name": "Juju"})
# add_document(test)
# delete_document(2)
