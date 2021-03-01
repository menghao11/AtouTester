from jinja2 import Environment, FileSystemLoader
import os

# 获取当前路径
THIS_DIR = os.getcwd()

def generate_test_paper(title):
    try:
        # 创建 jinja2 环境
        # Notice the use of trim_blocks, which greatly helps control
        # whitespace.
        paper_env = Environment(loader=FileSystemLoader(THIS_DIR),
                             trim_blocks=True)
        #选择题
        questions = ({'xx':1,'yyy':"(   )操作系统允许在一台主机上同时连接多台终端，多个用户可以通过各自的终端同时交互地使用计算机。",'answer1':'Windows','answer2':'Linux','answer3':'Mac OS X','answer4':'DOS'},
                    {'xx':2,'yyy':"以下哪种类型是B/S构架的正确描述？",'answer1':'需要安装客户端的软件','answer2':'不需要安装就可以使用的软件','answer3':'依托浏览器的网络系统','answer4':'依托outlook等软件的邮件系统'},
                    {'xx':3,'yyy':"下面哪个不是合法的SQL的归类函数？",'answer1':'AVG','answer2':'SUM','answer3':'MIN','answer4':'CURRENT_DATE()'},
                    {'xx':4,'yyy':"PHP是一种什么型的语言：（  ）",'answer1':'编译型','answer2':'解释型','answer3':'两者都是','answer4':'两者都不是'})
        #填空题
        fillins = ({'xx':1,'yyy':"操作系统是计算机系统中的一个___系统软件_______，它管理和控制计算机系统中的___资源_________。"},
                    {'xx':2,'yyy':"多道批处理系统的特点是_______和_______。"},
                    {'xx':3,'yyy':"处理机执行状态有 ______________ 和______________两种。"},
                    {'xx':4,'yyy':"实时系统应具有两个基本特征: _________和_________。"},)
        #判断题
        judgments = ({'xx':1,'yyy':"软件的开发与运行经常受到硬件的限制和制约。（  ）"},
                    {'xx':2,'yyy':"模块内的高内聚往往意味着模块间的松耦合。（  ）"},
                    {'xx':3,'yyy':"软件的质量好坏主要由验收人员负责，其他开发人员不必关心。（  ）"},
                    {'xx':4,'yyy':"判定覆盖不一定包含条件覆盖，条件覆盖也不一定包含判定覆盖。（  ）"},)
        paper = paper_env.get_template('template.xml').render(xx_title=title,questions=questions,fillins=fillins,judgments=judgments, encoding='utf-8')
        #简答题
        short_answers = ({'xx':1,'yyy':"SQL提供的基本数据类型有哪些？每种举两个例子。"},
                    {'xx':2,'yyy':"简述Where子句与Having子句的区别。"},
                    {'xx':3,'yyy':"简述视图的定义以及与基本表的区别。"},
                    {'xx':4,'yyy':"简述数据库系统如何实现应用程序与数据物理独立性和逻辑独立性。"},)
        # 从加载本地 template.xml 模板文件，并传入数据
        paper = paper_env.get_template('template.xml').render(xx_title=title,questions=questions,fillins=fillins,judgments=judgments,short_answers=short_answers, encoding='utf-8')
        return paper
    except Exception as e:
        print("Generate test paper failed!")
        raise e

def write_test_paper(title,paper_text):
    try:
        path = r'%s.xml' % title
        with open(path, 'w', encoding='utf-8') as test:
            test.write(paper_text)
        return path
    except Exception as e:
        print("Write test paper failed!")
        raise e

if __name__ == '__main__':
    title = '试卷'
    paper_text = generate_test_paper(title)
    write_test_paper(title,paper_text)
    print("Generate and write test paper successfully!")
