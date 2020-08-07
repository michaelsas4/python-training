import logging
logging.getLogger("kivy").disabled = True

from kivy.app import App
from kivy.uix.listview import ListView

from cmd import Cmd
from threading import Thread

class MyApp(App):
    def build(self):
        self.lv = ListView()
        return self.lv  

    def update(self, line):
        self.lv.adapter.data.append(line)
        return "list updated"

class MyCmd(Cmd, object):
    def __init__(self, app, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.app = app

    def do_EOF(self, line):
        self.app.stop()
        return True

    def default(self, line):
        ret = self.app.update(line)
        print(ret)

if __name__ == '__main__':
    app = MyApp()
    Thread(target=app.run).start()
    MyCmd(app).cmdloop()