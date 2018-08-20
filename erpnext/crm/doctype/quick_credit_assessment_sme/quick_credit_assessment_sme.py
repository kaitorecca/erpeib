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
				SELECT 'he_so_no_vay', he_so_no_vay from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'kinh_nghiem_gd', kinh_nghiem_gd from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'fb_kinh_doanh_nhieu_nganh', fb_kinh_doanh_nhieu_nganh from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_ty_trong_sx', pla_ty_trong_sx from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_so_nam_hoat_dong', pla_so_nam_hoat_dong from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pe_so_luong_cua_hang', pe_so_luong_cua_hang from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pha_trung_thau', pha_trung_thau from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pha_doanh_thu', pha_doanh_thu from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'loi_nhuan_sau_thue', loi_nhuan_sau_thue from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'no_qua_han_cic', no_qua_han_cic from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'fb_phan_loai_dai_ly', fb_phan_loai_dai_ly from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_nganh_kinh_doanh', pla_nganh_kinh_doanh from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pla_he_so_no_vay_ngan_han', pla_he_so_no_vay_ngan_han from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pe_loai_hinh_so_huu', pe_loai_hinh_so_huu from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'pha_thoi_gian_hop_tac', pha_thoi_gian_hop_tac from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'lo_luy_ke', lo_luy_ke from `tabQuick Credit Assessment SME` WHERE name = '{rcd}' UNION ALL
				SELECT 'so_nam_hoat_dong', so_nam_hoat_dong from `tabQuick Credit Assessment SME` WHERE name = '{rcd}'
			) d
			LEFT JOIN `tabQuick Credit Assessment SME Criteria` a ON a.criteria_value = d.criteria_mark AND a.criteria_name = d.criteria
		""".format(rcd=self.name), as_dict=True)

		self.credit_scoring_result = final_score[0]

		# if final_score[0][0] < 10:
		# 	self.credit_scoring_result = "Loai ho so"
		# else:
		# 	self.credit_scoring_result = "Diem tin dung la " + str(final_score[0][0])





