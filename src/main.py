from services.service import add_document, delete_document
from models.Transaction import Transaction, PaymentMethod

test = Transaction(
    Cpf="12345678901",
    Name="Fabrizio",
    Price=10,
    Company="Apple",
    Product="Iphone X",
    PaymentMethod="Credit Card"
)

add_document(test)
# delete_document("s")