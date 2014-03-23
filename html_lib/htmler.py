#coding: utf-8
import os

page_data=((1,"Лодка",200),(2,"Машина",4000),(3,"Самолёт",450))
html_header = '<html><head><title>{0}</title><link href="bs/css/bootstrap.min.css" rel="stylesheet"></head><body><table class="table">'
html_close = "</table></body></html>"
def htmler(page_data,page_name="Страница отсутствует",*args):
    
    return_table = '<th>ID</th><th>Name</th><th>Price</th>';
    for line in page_data:
        return_table+='<tr><td>'+str(line[0])+'</td><td>'+str(line[1])+'</td><td>'+str(line[2])+'</td></tr>'

    open("sample.html", "w").write(html_header.format(page_name)+return_table+'<script src="bs/js/bootstrap.min.js"></script>'+html_close)
    return html_header+return_table+html_close


#print htmler(page_name,page_data)
