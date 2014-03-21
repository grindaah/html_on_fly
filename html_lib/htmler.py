#coding: utf-8
import os

page_data=((1,"Лодка",200),(2,"Машина",4000),(3,"Самолёт",450))

def htmler(page_data,page_name="Страница отсутствует",*args):
    
    return_table = '';
    for line in page_data:
        return_table+='<tr><td>'+str(line[0])+'</td><td>'+str(line[1])+'</td><td>'+str(line[2])+'</td></tr>'

    open("sample.html", "w").write('<html><head><title>'+page_name+'</title></head><body><table style="border:solid 1px #000, width: 100px;">'+return_table+'</table></body></html>')
    return '<html><head><title>'+page_name+'</title></head><body><table>'+return_table+'</table></body></html>'


#print htmler(page_name,page_data)
