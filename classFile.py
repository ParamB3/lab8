#Param Butani
class deforestationYear:
    def __init__(self, year, area, legalAmzTotal):
        self.year = year
        self.area = area
        self.amz = legalAmzTotal

    def __repr__(self) -> str:
        return f"deforestationYear(year= {self.year}, area = {self.area}, amz = {self.amz})"

    def __eq__(self, other) -> bool:
        return (
                type(other) == deforestationYear
                and self.year == other.year
                and self.area == other.area
                and self.amz == other.amz)
#Param Butani
class amazonFires:
    def __init__(self, year, month, state, latitude, longitude, firespots):
        self.year = year
        self.month = month
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.firespots = firespots

    def __repr__(self) -> str:
        return f"amazonFires(year = {self.year}, month = {self.month}, state={self.state}, latitude = {self.latitude}, longitude = {self.longitude}, firespots = {self.firespots})"

    def __eq__(self,other) -> bool:
        return (
                type(other) == amazonFires
                and self.year == other.year
                and self.month == other.month
                and self.state == other.state
                and self.latitude == other.latitude
                and self.longitude == other.longitude
                and self.firespots == other.firespots
        )
#Jorge Sanchez
class climateEvent:
    def __init__(self, start,end, event, severity):
        self.start = start
        self.end = end
        self.event = event
        self.severity = severity

    def __repr__(self) -> str:
        return f"climateEvent(start = {self.start}, end = {self.end}, event = {self.event}, severity = {self.severity})"

    def __eq__(self,other) -> bool:
        return(
            type(other) == climateEvent
            and self.start == other.start
            and self.end == other.end
            and self.event == other.event
            and self.severity == other.severity
        )