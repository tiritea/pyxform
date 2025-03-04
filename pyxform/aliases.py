"""
Aliases for elements which could mean the same element in XForm but is represented
differently on the XLSForm.
"""

from pyxform import constants

# Aliases:
# Ideally aliases should resolve to elements in the json form schema

# select, control and settings alias keys used for parsing,
# which is why self mapped keys are necessary.

control = {
    "group": constants.GROUP,
    "lgroup": constants.REPEAT,
    "repeat": constants.REPEAT,
    "loop": constants.LOOP,
    "looped group": constants.REPEAT,
}
select_from_file = {
    "select_one_from_file": constants.SELECT_ONE,
    "select_multiple_from_file": constants.SELECT_ALL_THAT_APPLY,
    "select one from file": constants.SELECT_ONE,
    "select multiple from file": constants.SELECT_ALL_THAT_APPLY,
}
select = {
    "add select one prompt using": constants.SELECT_ONE,
    "add select multiple prompt using": constants.SELECT_ALL_THAT_APPLY,
    "select all that apply from": constants.SELECT_ALL_THAT_APPLY,
    "select one from": constants.SELECT_ONE,
    "select1": constants.SELECT_ONE,
    "select_one": constants.SELECT_ONE,
    "select one": constants.SELECT_ONE,
    "select_multiple": constants.SELECT_ALL_THAT_APPLY,
    "select all that apply": constants.SELECT_ALL_THAT_APPLY,
    "select_one_external": constants.SELECT_ONE_EXTERNAL,
    **select_from_file,
    "rank": constants.RANK,
}
cascading = {
    "cascading select": constants.CASCADING_SELECT,
    "cascading_select": constants.CASCADING_SELECT,
}
settings_header = {
    "form_title": constants.TITLE,
    "set form title": constants.TITLE,
    "form_id": constants.ID_STRING,
    "sms_keyword": constants.SMS_KEYWORD,
    "sms_separator": constants.SMS_SEPARATOR,
    "sms_allow_media": constants.SMS_ALLOW_MEDIA,
    "sms_date_format": constants.SMS_DATE_FORMAT,
    "sms_datetime_format": constants.SMS_DATETIME_FORMAT,
    "prefix": constants.COMPACT_PREFIX,
    "delimiter": constants.COMPACT_DELIMITER,
    "set form id": constants.ID_STRING,
    "public_key": constants.PUBLIC_KEY,
    "submission_url": constants.SUBMISSION_URL,
    "auto_send": constants.AUTO_SEND,
    "auto_delete": constants.AUTO_DELETE,
    "allow_choice_duplicates": constants.ALLOW_CHOICE_DUPLICATES,
}
# TODO: Check on bind prefix approach in json.
# Conversion dictionary from user friendly column names to meaningful values
survey_header = {
    "Label": "label",
    "Name": "name",
    "SMS Field": constants.SMS_FIELD,
    "SMS Option": constants.SMS_OPTION,
    "SMS Separator": constants.SMS_SEPARATOR,
    "SMS Allow Media": constants.SMS_ALLOW_MEDIA,
    "SMS Date Format": constants.SMS_DATE_FORMAT,
    "SMS DateTime Format": constants.SMS_DATETIME_FORMAT,
    "SMS Response": constants.SMS_RESPONSE,
    "compact_tag": "instance::odk:tag",  # used for compact representation
    "Type": "type",
    "List_name": constants.LIST_NAME_U,
    # u"repeat_count": u"jr:count",  duplicate key
    "read_only": "bind::readonly",
    "readonly": "bind::readonly",
    "relevant": "bind::relevant",
    "caption": constants.LABEL,
    "appearance": "control::appearance",  # TODO: this is also an issue
    "relevance": "bind::relevant",
    "required": "bind::required",
    "constraint": "bind::constraint",
    "constraining message": "bind::jr:constraintMsg",
    "constraint message": "bind::jr:constraintMsg",
    "constraint_message": "bind::jr:constraintMsg",
    "calculation": "bind::calculate",
    "calculate": "bind::calculate",
    "command": constants.TYPE,
    "tag": constants.NAME,
    "value": constants.NAME,
    "image": "media::image",
    "big-image": "media::big-image",
    "audio": "media::audio",
    "video": "media::video",
    "image-description": "media::image-description",
    "count": "control::jr:count",
    "repeat_count": "control::jr:count",
    "jr:count": "control::jr:count",
    "autoplay": "control::autoplay",
    "rows": "control::rows",
    # New elements that have to go into itext elements:
    "noAppErrorString": "bind::jr:noAppErrorString",
    "no_app_error_string": "bind::jr:noAppErrorString",
    "requiredMsg": "bind::jr:requiredMsg",
    "required_message": "bind::jr:requiredMsg",
    "required message": "bind::jr:requiredMsg",
    "body": "control",
    "parameters": "parameters",
    constants.ENTITIES_SAVETO: "bind::entities:saveto",
}

entities_header = {constants.LIST_NAME_U: "dataset"}

# Key is the pyxform internal name, Value is the name used in error/warning messages.
TRANSLATABLE_SURVEY_COLUMNS = {
    constants.LABEL: constants.LABEL,
    # Per ODK Spec, could include "short" once pyxform supports it.
    constants.HINT: constants.HINT,
    "guidance_hint": "guidance_hint",
    "image": survey_header["image"],
    "big-image": survey_header["big-image"],
    "audio": survey_header["audio"],
    "video": survey_header["video"],
    "jr:constraintMsg": "constraint_message",
    "jr:requiredMsg": "required_message",
}
TRANSLATABLE_CHOICES_COLUMNS = {
    "label": constants.LABEL,
    "image": "media::image",
    "big-image": "media::big-image",
    "audio": "media::audio",
    "video": "media::video",
}
list_header = {
    "caption": constants.LABEL,
    constants.LIST_NAME_U: constants.LIST_NAME_S,
    "value": constants.NAME,
    "image": "media::image",
    "big-image": "media::big-image",
    "audio": "media::audio",
    "video": "media::video",
    "image-description": "media::image-description",
}
# Note that most of the type aliasing happens in all.xls
_type_alias_map = {
    "imei": "deviceid",
    "image": "photo",
    "add image prompt": "photo",
    "add photo prompt": "photo",
    "add audio prompt": "audio",
    "add video prompt": "video",
    "add file prompt": "file",
}
yes_no = {
    "yes": True,
    "Yes": True,
    "YES": True,
    "true": True,
    "True": True,
    "TRUE": True,
    "true()": True,
    "no": False,
    "No": False,
    "NO": False,
    "false": False,
    "False": False,
    "FALSE": False,
    "false()": False,
}
label_optional_types = [
    "calculate",
    "deviceid",
    "end",
    "phonenumber",
    "simserial",
    "start",
    "start-geopoint",
    "today",
    "username",
]
osm = {"osm": constants.OSM_TYPE}
BINDING_CONVERSIONS = {
    "yes": "true()",
    "Yes": "true()",
    "YES": "true()",
    "true": "true()",
    "True": "true()",
    "TRUE": "true()",
    "no": "false()",
    "No": "false()",
    "NO": "false()",
    "false": "false()",
    "False": "false()",
    "FALSE": "false()",
}
