from re import match

from bs4 import BeautifulSoup
from django.db import models
from django.utils.translation import ugettext_lazy as _
from requests import get


class QueueItemManager(models.Manager):
    """
    Manager class for QueueItem
    """

    @staticmethod
    def dequeue():
        """
        Remove the top url
        """
        try:
            item = QueueItem.objects.filter(active=True).order_by('-votes',
                                                                'post_time',
                                                                'vote_time')[0]
            item.active = False
            item.save()
            status = "success"
        except IndexError:
            status = "no active items in queue"
        except:
            status = "error"
        finally:
            return status


    @staticmethod
    def get_active_urls():
        """
        Return the active urls in order
        """

        qs = QueueItem.objects.filter(active=True).order_by('-votes',
                                                            'post_time',
                                                            'vote_time')
        return qs.values('id', 'title', 'url', 'votes', )


class QueueItem(models.Model):

    url = models.URLField(
        _('youtube link'),
    )

    upvotes = models.IntegerField(
        _('number of upvotes'),
        default=0,
    )

    downvotes = models.IntegerField(
        _('number of downvotes'),
        default=0,
    )

    votes = models.IntegerField(
        _('number of votes'),
        default=0,
    )

    post_time = models.DateTimeField(
        _('post time'),
        auto_now_add=True,
    )

    vote_time = models.DateTimeField(
        _('most recent vote time'),
        auto_now=True,
    )

    active = models.BooleanField(
        _('currently in the queue'),
        default=True,
    )

    title = models.CharField(
        _('video name'),
        max_length=100,
    )

    objects = QueueItemManager()

    def upvote(self):
        self.upvotes += 1
        self.votes += 1
        self.save()

    def downvote(self):
        self.downvotes += 1
        self.votes -= 1
        self.save()

    def __init__(self, *args, **kwargs):
        url = kwargs.get('url', '')

        template = r'^http://www\.youtube\.com/watch\?[^/]+$'
        if not match(template, url):
            raise ValueError('Invalid URL')

        soup = BeautifulSoup(get(url).content)
        title = soup.find('span', {'id': 'eow-title'}).text.strip()
        kwargs['title'] = title

        super(QueueItem, self).__init__(*args, **kwargs)

