from itertools import chain

from django.db import models
from django.utils.translation import ugettext_lazy as _


class QueueItemManager(models.Manager):
    """
    Manager class for QueueItem
    """

    def get_active_urls(self):
        """
        Return the active urls in order
        """

        qs = QueueItem.objects.filter(active=True).order_by('-votes',
                                                            'post_time',
                                                            'vote_time')
        return [x for x in chain.from_iterable(qs.values_list('url'))]


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

    objects = QueueItemManager()

    def upvote(self):
        self.upvotes += 1
        self.votes += 1
        self.save()

    def downvote(self):
        self.downvotes += 1
        self.votes -= 1
        self.save()


