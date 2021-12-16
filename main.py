import mysql.connector as sql
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivymd.uix.list import OneLineAvatarIconListItem, OneLineListItem
from kivy.uix.button import Button
from kivymd.uix.list import IRightBody, OneLineAvatarIconListItem
from kivymd.uix.button import MDIconButton

# классы активностей
class StartWindow(Screen):
    pass

class ShelfWindow(Screen):
    pass

class PrintersWindow(Screen):
    def connection(self):
        self.conn = sql.connect( host="bgpkmaw7.beget.tech", user="bgpkmaw7_pospel", password="l5D&S7n0", database="bgpkmaw7_pospel")

    def get_shelf(self, *args):
        self.connection()
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM shelf")
        res = cur.fetchall()
        print(res)
        
        for item in res:
            di = str(item[1]) 
            self.ids.list_one.add_widget(
                ShelfItem(text=di))

    def on_enter(self):
        self.get_shelf()
    
    def on_leave(self):
        self.ids.list_one.clear_widgets()


class EditingWindow(Screen):
    pass

class SettingsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ItemWindow(Screen):
    pass

class ShelfItem(OneLineAvatarIconListItem):
    pass

class RightButton(IRightBody, MDIconButton):
    pass




class MainApp(MDApp):

    # само приложение
    def Builder(self):
        self.producer = ""
        sm = ScreenManager()
        sm.add_widget(StartWindow(name='Start'))
        sm.add_widget(ShelfWindow(name='Shelf'))
        sm.add_widget(PrintersWindow(name='Printers'))
        sm.add_widget(EditingWindow(name='Editing'))
        sm.add_widget(SettingsWindow(name='Settings'))
        sm.add_widget(ItemWindow(name='Item'))
        # self.theme_cls.theme_style="Dark"
        # self.theme_cls.primary_palette="DeepPurple"
        # self.theme_cls.accent_platte = "Teal"
        return Builder.load_file('main.kv')
    
    def update_label(self):
        self.prin.text = self.producer

    # подключение к бд
    def connection(self):
        self.conn = sql.connect( host="bgpkmaw7.beget.tech", user="bgpkmaw7_pospel", password="l5D&S7n0", database="bgpkmaw7_pospel")

    def shelf_inf(self, *args):
        self.connection()
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM shelf")
        res = cur.fetchall()
        print(res)

        for item in res:
            art = str(item[1])
            numb = str(item[2])
            prod = str(item[3])
            status = str(item[4])
            date_b = str(item[5])
            prin = str(item[6])
            shelf = str(item[7])
            self.root.ids.shelf_items.add_widget(
                Button(text="Артикуль: " + str(art) + "\n" + "Инвент_номер: " + str(numb) + "\n" + "Бренд: " +  str(prod) + "\n"+ "Статус картриджа: " +  str(status) + "\n"+ "Дата закупки: " +  str(date_b) + "\n" + "совместимый принтер: " +  str(prin) + "\n"+ "Номер полки: " +  str(shelf) + "\n",
                    size=[75,100],
                    background_color=[221/255, 247/255, 176/255, 1]
                ))


MainApp().run()
