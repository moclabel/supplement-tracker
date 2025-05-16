from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.datepicker import DatePicker
import json
from datetime import datetime
import os

class SupplementTrackerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.data_file = 'supplements.json'
        self.config_file = 'supplements_config.json'
        self.selected_date = datetime.today().strftime('%Y-%m-%d')
        self.supplements = self.load_config()
        self.checkboxes = {}
        self.build_ui()
        self.load_data()

    def load_config(self):
        if os.path.exists(self.config_file):
            return json.load(open(self.config_file))
        return {
            'Sabah': ['Venatura D3K2 20000IU', 'Solgar B12', 'Magnezyum'],
            'Oglen': ['Zinc', 'ALA', 'Benfotiamin'],
            'Aksam': ['Omega3', 'Vitamin E', 'B Complex']
        }

    def save_config(self):
        json.dump(self.supplements, open(self.config_file, 'w'), indent=2)

    def build_ui(self):
        dp = DatePicker()
        dp.bind(on_submit=self.on_date_select)
        self.add_widget(dp)
        sc = ScrollView(size_hint=(1, 0.7))
        grid = GridLayout(cols=1, spacing=5, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        self.grid = grid
        sc.add_widget(grid)
        self.add_widget(sc)
        ctrl = BoxLayout(size_hint=(1, 0.2), spacing=5)
        for label, handler in [('Reset', self.reset_day), ('History', self.show_history),
                               ('Add', self.add_supplement), ('Delete', self.delete_supplement)]:
            btn = Button(text=label)
            btn.bind(on_release=handler)
            ctrl.add_widget(btn)
        self.add_widget(ctrl)
        self.render_checkboxes()

    def render_checkboxes(self):
        self.grid.clear_widgets()
        self.checkboxes.clear()
        for time, items in self.supplements.items():
            self.grid.add_widget(Label(text=time, size_hint_y=None, height=30))
            for supp in items:
                box = BoxLayout(size_hint_y=None, height=30)
                chk = CheckBox()
                self.checkboxes[supp] = chk
                box.add_widget(chk)
                box.add_widget(Label(text=supp))
                self.grid.add_widget(box)

    def on_date_select(self, instance, date):
        self.selected_date = date.strftime('%Y-%m-%d')
        self.load_data()

    def save_data(self):
        data = json.load(open(self.data_file)) if os.path.exists(self.data_file) else {}
        day = {supp: chk.active for supp, chk in self.checkboxes.items()}
        day['last_updated'] = datetime.now().isoformat()
        data[self.selected_date] = day
        json.dump(data, open(self.data_file, 'w'), indent=2)

    def load_data(self):
        self.render_checkboxes()
        if not os.path.exists(self.data_file):
            return
        data = json.load(open(self.data_file))
        day = data.get(self.selected_date, {})
        for supp, chk in self.checkboxes.items():
            chk.active = day.get(supp, False)

    def reset_day(self, *args):
        for chk in self.checkboxes.values():
            chk.active = False
        self.save_data()

    def show_history(self, *args):
        if not os.path.exists(self.data_file):
            return
        data = json.load(open(self.data_file))
        text = ''
        for date, vals in sorted(data.items()):
            text += f"{date}:\n"
            for k, v in vals.items():
                if k == 'last_updated':
                    continue
                text += f" - {k}: {'✓' if v else '✗'}\n"
        popup = Popup(title='History', content=Label(text=text), size_hint=(0.8, 0.8))
        popup.open()

    def add_supplement(self, *args):
        content = BoxLayout(orientation='vertical', spacing=10)
        ti = TextInput(hint_text='Supplement name')
        sp = Spinner(values=list(self.supplements.keys()))
        btn = Button(text='Add')
        content.add_widget(ti)
        content.add_widget(sp)
        content.add_widget(btn)
        popup = Popup(title='Add Supplement', content=content, size_hint=(0.7, 0.5))
        def on_add(instance):
            name, time = ti.text.strip(), sp.text
            if name and time and name not in self.supplements[time]:
                self.supplements[time].append(name)
                self.save_config()
                self.render_checkboxes()
            popup.dismiss()
        btn.bind(on_release=on_add)
        popup.open()

    def delete_supplement(self, *args):
        content = BoxLayout(orientation='vertical', spacing=10)
        sp_time = Spinner(values=list(self.supplements.keys()))
        sp_supp = Spinner(values=[])
        def on_time_change(spinner, text):
            sp_supp.values = self.supplements[text]
        sp_time.bind(text=on_time_change)
        btn = Button(text='Delete')
        content.add_widget(sp_time)
        content.add_widget(sp_supp)
        content.add_widget(btn)
        popup = Popup(title='Delete Supplement', content=content, size_hint=(0.7, 0.5))
        def on_del(instance):
            t, s = sp_time.text, sp_supp.text
            if s in self.supplements[t]:
                self.supplements[t].remove(s)
                self.save_config()
                if os.path.exists(self.data_file):
                    data = json.load(open(self.data_file))
                    for d in data:
                        data[d].pop(s, None)
                    json.dump(data, open(self.data_file, 'w'), indent=2)
                self.render_checkboxes()
            popup.dismiss()
        btn.bind(on_release=on_del)
        popup.open()

class SupplementTrackerApp(App):
    def build(self):
        Window.size = (360, 640)
        return SupplementTrackerUI()

if __name__ == '__main__':
    SupplementTrackerApp().run()
