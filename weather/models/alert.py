from dataclasses import dataclass


@dataclass
class Alert:
    area_desc: str=None
    sent: str=None
    effective: str=None
    ends: str=None
    status: str=None
    severity: str=None
    certainty: str=None
    urgency: str=None
    event: str=None
    sender_name: str=None
    headline: str=None
    description: str=None
    instructions: str=None

    def __str__(self):
        return f"""
[{self.severity}] - {self.event} - {self.urgency} - {self.certainty}
{self.sender_name} - {self.sent}

START: {self.effective}
END: {self.ends}

{self.area_desc}

[ DETAILS ]
{self.headline}


{self.description}

[ INSTRUCTIONS ]
{self.instructions}

"""
    def from_data(self, raw_data):
        self.area_desc = raw_data.get('areaDesc', None)
        self.sent = raw_data.get('sent', None)
        self.effective = raw_data.get('effective', None)
        self.ends = raw_data.get('ends', None)
        self.status = raw_data.get('status', None)
        self.severity = raw_data.get('severity', None)
        self.certainty = raw_data.get('certainty', None)
        self.urgency = raw_data.get('urgency', None)
        self.event = raw_data.get('event', None)
        self.sender_name = raw_data.get('senderName', None)
        self.headline = raw_data.get('headline', None)
        self.description = raw_data.get('description', None)
        self.instructions = raw_data.get('instructions', None)
        
        return self
            



