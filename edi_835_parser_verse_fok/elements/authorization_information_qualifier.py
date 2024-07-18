from typing import Optional

from edi_835_parser_verse_fok.elements import Element


class AuthorizationInformationQualifier(Element):

	def parser(self, value: str) -> Optional[str]:
		if value == '00':
			value = None

		return value
