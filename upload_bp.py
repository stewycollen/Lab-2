from flask import Blueprint, request
from UseSqlite import InsertQuery, RiskQuery
from datetime import datetime

#creating an object for a blueprint
upload_bp= Blueprint("upload_bp", __name__,static_folder="static")

#Code to upload photos
@upload_bp.route('/upload',methods=['POST','GET'])
def main():
    if request.method=='POST':
        uploaded_file=request.files['file']
        time_str=datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename=time_str+'.jpg'
        uploaded_file.save('./static/upload/'+new_filename)
        time_info=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        description=request.form['description']
        path='./static/upload/'+new_filename
        iq=InsertQuery('./static/RiskDB.db')
        iq.instructions("INSERT INTO photo Values('%s','%s','%s','%s')"%(time_info,description,path,new_filename))
        iq.do()
        return '<p>You have uploaded %s.<br/> <a href="/">Return</a>.'%(uploaded_file.filename)
    else:
        page='''<form action="/upload"method="post"enctype="multipart/form-data">
        <input type="file"name="file"><input name="description"><input type="submit"value="Upload"></form>'''        
        return page