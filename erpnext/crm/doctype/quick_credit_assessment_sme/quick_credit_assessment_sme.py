# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class QuickCreditAssessmentSME(Document):
	def on_submit(self):
		final_score = frappe.db.sql("""SELECT sum(a.score*a.weight) as final_score FROM
			(
				SELECT 'doanh_thu' as criteria, doanh_thu as criteria_mark from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL 
				SELECT 'loi_nhuan_sau_thue', loi_nhuan_sau_thue from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'lo_luy_ke', lo_luy_ke from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'he_so_no_vay', he_so_no_vay from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'no_qua_han_cic', no_qua_han_cic from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'register_capital', register_capital from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'own_capital', own_capital from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'asset_guarantor_percentage', asset_guarantor_percentage from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'guarantor_liquidity', guarantor_liquidity from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'other_banks_relationship', other_banks_relationship from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'kinh_doanh_nhieu_nganh', kinh_doanh_nhieu_nganh from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'lich_su_qhtd_eib', lich_su_qhtd_eib from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'so_nam_hoat_dong', so_nam_hoat_dong from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'kinh_nghiem_gd', kinh_nghiem_gd from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'education_level_director', education_level_director from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'transaction_office_ownership', transaction_office_ownership from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_ty_trong_sx', pla_ty_trong_sx from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_loan_interest', pla_loan_interest from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_ty_trong_xuat_khau', pla_ty_trong_xuat_khau from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_nganh_kinh_doanh', pla_nganh_kinh_doanh from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_so_nam_hoat_dong', pla_so_nam_hoat_dong from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_vehicle_number', pla_vehicle_number from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'local_lc_at_local_bank', local_lc_at_local_bank from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pe_so_luong_cua_hang', pe_so_luong_cua_hang from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pe_additional_facilities', pe_additional_facilities from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pe_total_pumper', pe_total_pumper from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'fb_loan_interest', fb_loan_interest from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'fb_phan_loai_dai_ly', fb_phan_loai_dai_ly from `tabQuick Credit Assessment SME` WHERE name = '{rcd}'
			) d
			LEFT JOIN `tabQuick Credit Assessment SME Criteria` a ON a.criteria_value = d.criteria_mark AND a.criteria_name = d.criteria 
			WHERE a.criteria_product = '{prd}'
		""".format(rcd=self.name,prd=self.loai_nganh_nghe))[0][0]

		if final_score < 10:
			self.credit_scoring_result = "Loai ho so"
		else:
			self.credit_scoring_result = str(final_score)





