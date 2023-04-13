{
    'name': '2pdf',
    'version': '1.0',
    'depends': ['base', 'stock', 'mail', 'contacts'],
    'author': 'A.Petrushin',
    'category': 'Uncategorized',
    'description' : """ 
    Creating PDF report from warehouse/movements via xml:
    """,
    'data': ['report/2pdf_report.xml', 'report/2pdf_group_movement_report.xml', 'views/mail_sender.xml', 'data/params.xml', 'data/mail_template.xml', 'report/2pdf_total_movements.xml',],
}