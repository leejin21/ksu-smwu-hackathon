from django.conf import settings
from django.db import models
from django.utils import timezone



    # 일단 할 것: 테마 제목, 장소들 쓰는 칸(1,2,3 정도만), 이름, 날짜 및 시간, 인원,
    # 예약자 이름, 선호언어, 날짜, 인원, 국적, 예약된 이동수단 유뮤(렌트유무), 특별 사항추가(와이파이, 베이비시트, 휠체어, 기타), 기타 요구사항

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
