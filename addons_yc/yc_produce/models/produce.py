# -*- coding: utf-8 -*-


from odoo import models, fields, api


<<<<<<< HEAD

class YcWeight(models.Model):
    _name = "yc.weight"

    driver_id = fields.Many2one("yc.driver", string="司機名稱")
    name = fields.Char("過磅單號")
    date = fields.Date("過磅日期")
    time = fields.Char("過磅時間")
    person = fields.Many2one("hr.main", string="過磅員")
    car_no = fields.Char("車次序號")
    in_out = fields.Selection([('i', '進貨'), ('o', '出貨')], '進出貨')
    factory = fields.Many2one("yc.factory", string="所屬工廠")
    import_times = fields.Char("進貨次數")
    export_times = fields.Char("出貨次數")
    # 進出貨次數要改成自動記錄
    plate_no = fields.Char("車號")
    total_weight = fields.Char("總重 (KG)")
    curb_weight = fields.Char("空車重 (KG)")
    ept_buc_weight = fields.Char("空桶重 (KG)")
    net_weight = fields.Char("淨重 (KG)")
    refine_weight = fields.Char("調質重量 (KG)")
    carburize_weight = fields.Char("滲碳單價")
    other1 = fields.Char("其他1")
    other2 = fields.Char("其他2")

    # 一張過磅單 上面的貨物可能含有多家客戶

    customer_detail_ids = fields.One2many("yc.weight.details", "name", "客戶資料")

    #def form_time(self):
        # 檢查欄位的形式是否符合 XX:XX

class YcWeightDetails(models.Model):
    _name = "yc.weight.details"

    name = fields.Many2one("yc.weight", "訂單編號", ondelete="cascade")
    customer_id = fields.Many2one("yc.customer", "客戶名稱")
    processing_id = fields.Many2one("yc.processing", "加工廠名稱")
    note = fields.Char("備註")
=======
class Produce(models.Model):
    _name = "produce.main"

    name = fields.Char("過磅單號")
    weight_date = fields.Date("過磅日期")
    weight_time = fields.Char("過磅時間")
    cargo_driver = fields.Char("過磅司機")
    weight_person = fields.Char("過磅員")
    car_no = fields.Char("車次序號")
    in_out = fields.Selection([('i', '進貨'), ('o', '出貨')], '進出貨')
    factory = fields.Char("所屬工廠")
>>>>>>> c83cdbda13a1b5bb42e23b74b7722b8c324c3a98
