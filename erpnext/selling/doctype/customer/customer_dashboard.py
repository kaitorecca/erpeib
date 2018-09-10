from frappe import _

def get_data():
	return {
		'heatmap': True,
		'fieldname': 'customer',
		'transactions': [
			{
				'label': _('Pre Sales'),
				'items': ['Transaction Management']
			},
			{
				'label': _('Meeting'),
				'items': ['Call Report']
			}
		]
	}