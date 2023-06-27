# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 10:11
import csv

from taggen.tag import HMITag, TagList
from taggen.utils.tagtype import TagTypes
from .kepservertag import KepServerTag, KEP_HEADER

KEP_TAG_TYPE = {
    TagTypes.TYPE_BOOL.type: 'Boolean',
    TagTypes.TYPE_INT.type: 'Short',
    TagTypes.TYPE_DINT.type: 'Long',
    TagTypes.TYPE_REAL.type: 'Float',
    TagTypes.TYPE_WORD.type: 'Short',
}

KEP_CLIENT_ACCESS = ('R/W', 'RO')

_KEP_CLIENT_ACCESS = {
    'Yes': KEP_CLIENT_ACCESS[1],
    'No': KEP_CLIENT_ACCESS[0],
}


def output_csv(tag_list: TagList, output_path, group_enable=False):
    temp_list = [tag_list.disc_list, tag_list.int_list, tag_list.real_list]
    with open(output_path, 'w', newline='', encoding='ANSI') as f:
        writer = csv.writer(f)
        writer.writerow(KEP_HEADER)
        for hmi_tag_list in temp_list:
            for hmi_tag in hmi_tag_list:
                # if isinstance(tg, HMITag):
                kep_tag = KepServerTagFromHMITag(hmi_tag, group_enable)
                writer.writerow(kep_tag.to_list())
        f.close()
    print('生成KepServer导入csv文件: ' + output_path)


def KepServerTagFromHMITag(tag: HMITag, group_enable=False):
    if group_enable:
        tag_name = '{}.{}'.format(tag.group, tag.name)
    else:
        tag_name = tag.name
    address = tag.item_name
    data_type = KEP_TAG_TYPE[tag.type.lower()]
    try:
        client_access = _KEP_CLIENT_ACCESS[tag.read_only]
    except KeyError:
        client_access = _KEP_CLIENT_ACCESS['No']
    description = tag.comment
    return KepServerTag(
        tag_name=tag_name,
        address=address,
        data_type=data_type,
        client_access=client_access,
        description=description
    )
