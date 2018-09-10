from frappe import _

def get_data():
	return {
		'fieldname': 'transaction_management',
		'transactions': [
			{
				'label': _('Call report'),
				'items': ['Call Report']
			}
		]
	}