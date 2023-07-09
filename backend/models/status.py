from enum import Enum

class status(Enum):
    APPROVED = 1
    DECLINED = 2
    PENDING = 3 # Set it to pending when a basic officer submits the docket for the first time and also when the make the relevant changes
    NEEDS_UPDATE= 4
