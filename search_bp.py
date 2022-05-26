from flask import Blueprint, request
from UseSqlite import RiskQuery
from PIL import Image

#creating an object for a blueprint
search_bp= Blueprint("search_bp", __name__,static_folder="static")

#Code to search specific photo
def make_html_paragraph(s):
    if s.strip()=='':
        return ''
    lst=s.split(',')
    picture_path=lst[2].strip()
    picture_name=lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'jpeg')
    result='<p>'
    result+='<i>%s</i><br/>'%(lst[0])
    result+='<i>%s</i><br/>'%(lst[1])
    result+='<a href="%s"><img src="../static/figure/%s"alt="风景图"></a>'%(picture_path,picture_name)
    return result+'</p>'

#function to get all photos from the database
def get_database_photos(x):
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo WHERE description = '%s'"%(x))
    rq.do()
    record='<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record+='%s'%(make_html_paragraph(r))
    return record+'</table>\n'

@search_bp.route("/<search>")
def show(search):
    return get_database_photos(search)