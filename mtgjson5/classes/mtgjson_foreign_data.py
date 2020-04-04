"""
MTGJSON container for foreign entries
"""

from typing import Any, Dict, Optional

from ..utils import to_camel_case


class MtgjsonForeignDataObject:
    """
    Foreign data rows
    """

    language: str
    multiverse_id: Optional[int]
    flavor_text: Optional[str]
    name: Optional[str]
    text: Optional[str]
    type: Optional[str]

    def __init__(self) -> None:
        self.multiverse_id = None
        self.flavor_text = None
        self.name = None
        self.text = None
        self.type = None

    def for_json(self) -> Dict[str, Any]:
        """
        Support json.dumps()
        :return: JSON serialized object
        """
        skip_keys = ("url", "number", "set_code")

        return {
            to_camel_case(key): value
            for key, value in self.__dict__.items()
            if "__" not in key
            and not callable(value)
            and value is not None
            and key not in skip_keys
        }
