from typing import Optional

from edi_835_parser_verse_fok.elements import Element


class Dollars(Element):

	def parser(self, value: str) -> Optional[float]:
		if value != '':
			return float(value)
