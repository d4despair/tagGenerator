# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 10:12

from taggen.tag import Tag

_KEP_HEADER_RAW = 'Tag Name,Address,Data Type,Respect Data Type,Client Access,Scan Rate,Scaling,Raw Low,Raw High,' \
                  'Scaled Low,' \
                  'Scaled High,Scaled Data Type,Clamp Low,Clamp High,Eng Units,Description,Negate Value '

KEP_HEADER = ('Tag Name', 'Address', 'Data Type', 'Respect Data Type', 'Client Access', 'Scan Rate', 'Scaling',
              'Raw Low', 'Raw High', 'Scaled Low', 'Scaled High', 'Scaled Data Type', 'Clamp Low', 'Clamp High',
              'Eng Units', 'Description', 'Negate Value')


class KepServerTag(Tag):
    __slots__ = (
        'tag_name',
        'address',
        'data_type',
        'respect_data_type',
        'client_access',
        'scan_rate',
        'scaling',
        'raw_low',
        'raw_high',
        'scaled_low',
        'scaled_high',
        'scaled_data_type',
        'clamp_low',
        'clamp_high',
        'eng_units',
        'description',
        'negate_value',
    )

    def __init__(self, tag_name=None, address=None, data_type=None, respect_data_type=1, client_access='R/W',
                 scan_rate=100, scaling=None, raw_low=None, raw_high=None, scaled_low=None, scaled_high=None,
                 scaled_data_type=None, clamp_low=None, clamp_high=None, eng_units=None, description=None,
                 negate_value=None):
        self.tag_name = tag_name
        self.address = address
        self.data_type = data_type
        self.respect_data_type = respect_data_type
        self.client_access = client_access
        self.scan_rate = scan_rate
        self.scaling = scaling
        self.raw_low = raw_low
        self.raw_high = raw_high
        self.scaled_low = scaled_low
        self.scaled_high = scaled_high
        self.scaled_data_type = scaled_data_type
        self.clamp_low = clamp_low
        self.clamp_high = clamp_high
        self.eng_units = eng_units
        self.description = description
        self.negate_value = negate_value
