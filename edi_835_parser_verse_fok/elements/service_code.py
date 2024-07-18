from edi_835_parser_verse_fok.elements import Element
from edi_835_parser_verse_fok.elements.utilities import split_element


class ServiceCode(Element):

	def parser(self, value: str) -> str:
		value = split_element(value)
		_, code, *_ = value
		return code
