from edi_835_parser_verse_fok.elements import Element
from edi_835_parser_verse_fok.elements.utilities import split_element


class ServiceQualifer(Element):

	def parser(self, value: str) -> str:
		value = split_element(value)
		qualifier, *_ = value
		return qualifier
