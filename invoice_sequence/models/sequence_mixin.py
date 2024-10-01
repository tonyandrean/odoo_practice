from odoo import api, models
import re



class SequenceMixin(models.AbstractModel):
    _inherit = 'sequence.mixin'


    _sequence_year_range_regex = r'^(?P<prefix1>.*?)(?P<branch_code>\w+)(?P<year>(19|20|21)?\d{2})(?P<prefix2>\D)(?P<year_end>(19|20|21)?\d{2})(?P<prefix3>\D+?)(?P<seq>\d+)(?P<suffix>\D*?)$'
    _sequence_monthly_regex = r'^(?P<prefix1>.*?)(?P<branch_code>\w+)(?P<year>(19|20|21)?\d{2})(?P<prefix2>\D*?)(?P<month>(0[1-9]|1[0-2]))(?P<prefix3>\D+?)(?P<seq>\d+)(?P<suffix>\D*?)$'
    _sequence_yearly_regex = r'^(?P<prefix1>.*?)(?P<branch_code>\w+)(?P<year>(19|20|21)?\d{2})(?P<prefix2>\D+?)(?P<seq>\d+)(?P<suffix>\D*?)$'


    def _get_sequence_format_param(self, previous):
        """Get the python format and format values for the sequence.

        :param previous: the sequence we want to extract the format from
        :return tuple(format, format_values):
            format is the format string on which we should call .format()
            format_values is the dict of values to format the `format` string
            ``format.format(**format_values)`` should be equal to ``previous``
        """
        sequence_number_reset = self._deduce_sequence_number_reset(previous)
        regex = self._sequence_fixed_regex
        if sequence_number_reset == 'year':
            regex = self._sequence_yearly_regex
        elif sequence_number_reset == 'year_range':
            regex = self._sequence_year_range_regex
        elif sequence_number_reset == 'month':
            regex = self._sequence_monthly_regex

        format_values = re.match(regex, previous).groupdict()
        format_values['branch_code'] = self.env.user.branch_id.code
        format_values['seq_length'] = len(format_values['seq'])
        format_values['year_length'] = len(format_values.get('year') or '')
        format_values['year_end_length'] = len(format_values.get('year_end') or '')
        if not format_values.get('seq') and 'prefix1' in format_values and 'suffix' in format_values:
            # if we don't have a seq, consider we only have a prefix and not a suffix
            format_values['prefix1'] = format_values['suffix']
            format_values['suffix'] = ''

        for field in ('seq', 'year', 'month', 'year_end'):
            format_values[field] = int(format_values.get(field) or 0)

        placeholders = re.findall(r'\b(prefix\d|seq|suffix\d?|year|year_end|month|branch_code)\b', regex)
        format = ''.join(
            "{branch_code}/" if s == 'branch_code' else
            "{seq:0{seq_length}d}" if s == 'seq' else
            "{month:02d}" if s == 'month' else
            "{year:02d}" if s == 'year' else
            "{year_end:0{year_end_length}d}" if s == 'year_end' else
            "{%s}" % s
            for s in placeholders
        )

        return format, format_values