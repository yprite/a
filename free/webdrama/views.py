from django.shortcuts import render


# Create your views here.
from django.views import View
from datetime import datetime, date, time, timezone




# def index(request):
#     return  render(request, 'index.html')

class index(View):
    def __init__(self):
        self.title_nm = "메인페이지입니다."
        self.ogImgUrl = ""
        self.descript = "메인페이지입니다."
        self.template_name = "index.html"

    def get(self, request, *args, **kwargs):

        standardTime = 1626785580.0
        standardDebt = 926238589490618
        debtPerSeconds = 3244065


        d = date(2021, 7, 21)
        t = time(21, 52, 00)
        dt = datetime.combine(d, t)
        totalSeconds = datetime.now(timezone.utc).timestamp() - standardTime
        totalDebt = round(standardDebt + (totalSeconds * debtPerSeconds))

        self.content = {"descript": self.descript,
                        "title_nm": self.title_nm,
                        "ogImgUrl": self.ogImgUrl,
                        "data": totalDebt}

        return render(request, self.template_name, self.content)