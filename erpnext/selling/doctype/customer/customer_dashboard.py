from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Customer. See timeline below for details'),
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