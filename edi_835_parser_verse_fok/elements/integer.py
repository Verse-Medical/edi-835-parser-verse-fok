from typing import Optional, Union

from edi_835_parser_verse_fok.elements import Element


class Integer(Element):

	def parser(self, value: str) -> Optional[Union[int, str]]:
		if value == '':
			return None

		try:
			value = int(value)
		except:
			pass

		return value
