from django.db import models
import os
# Create your models here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chart.settings")

class ratings(models.Model):
    company = models.CharField(max_length=30)
    FB_likes = models.IntegerField(default=1)
    FB_likes_score = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    senior_leadership_rating = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    work_life_balance_rating = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    recommend_to_friend_rating = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    culture_and_values_rating = models.DecimalField(max_digits=3, decimal_places=2, default=1)

    # reference: https://whyhireme.wordpress.com/2012/04/29/django-python-models-base-py-indexerror-list-index-out-of-range/
    def __str__(self):
        return [self.company, self.FB_likes, self.FB_likes_score, self.overall_rating, self.senior_leadership_rating,
                self.work_life_balance_rating, self.recommend_to_friend_rating, self.culture_and_values_rating]
    class Meta:
        app_label = 'comp'

class review_summary(models.Model):
    company = models.CharField(max_length=30)
    company_id = models.IntegerField(default=0)
    word = models.CharField(max_length=30)
    part_of_speech = models.CharField(max_length=30)
    frequency = models.IntegerField(default=1)

    # extremely important to define str method and class meta!!
    # whenever console does not reflect the latest changes, just reboot console.
    def __str__(self):
        freq_str = str(self.frequency)
        list1 = [self.company, self.word, self.part_of_speech, freq_str]
        str1 = ','.join(list1)
        return str1

    class Meta:
        app_label = 'comp'