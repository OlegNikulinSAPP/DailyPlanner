import wx
import locale
from datetime import datetime


class DailyPlanner(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=wx.Size(800, 600))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Словарь для перевода дней недели
        weekdays_ru = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье'
        }

        # Получаем дату по-английски
        english_date = datetime.now().strftime('%A, %d.%m.%Y')
        # Заменяем день недели
        day_name_english = datetime.now().strftime('%A')
        current_date = english_date.replace(day_name_english, weekdays_ru[day_name_english])

        date_label = wx.StaticText(panel, label=f'📍 {current_date}')
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        date_label.SetFont(font)

        sizer.Add(date_label, 0, wx.ALL, 10)

        panel.SetSizer(sizer)

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    DailyPlanner(None, 'Мой ежедневник')
    app.MainLoop()
