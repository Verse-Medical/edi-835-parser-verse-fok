from edi_835_parser_verse_fok.elements.identifier import Identifier
from edi_835_parser_verse_fok.elements.payment_method import PaymentMethod
from edi_835_parser_verse_fok.elements.dollars import Dollars
from edi_835_parser_verse_fok.elements.integer import Integer
from edi_835_parser_verse_fok.elements.date import Date
from edi_835_parser_verse_fok.segments.utilities import split_segment


class FinancialInformation:
	identification = 'BPR'

	identifier = Identifier()
	amount_paid = Dollars()
	payment_method = PaymentMethod()
	routing_number = Integer()
	transaction_date = Date()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.amount_paid = segment[2]
		self.payment_method = segment[4]
		self.routing_number = segment[13]
		self.transaction_date = segment[16]

	def __repr__(self):
		return self.segment


if __name__ == '__main__':
	pass
