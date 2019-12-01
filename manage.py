from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app,db
from info import models
# 导入生成 csrf_token 值的函数
from flask_wtf.csrf import generate_csrf
from info.utils.common import do_index_class


app = create_app('development')
# Flask-script
@app.after_request
def after_request(response):
    # 调用函数生成 csrf_token
    csrf_token = generate_csrf()
    # 通过 cookie 将值传给前端
    response.set_cookie("csrf_token", csrf_token)
    return response

manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)

# # 添加自定义过滤器
app.add_template_filter(do_index_class, "index_class")




if __name__ == '__main__':
    manager.run()