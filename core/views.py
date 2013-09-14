from json import dumps

from django.http.response import HttpResponse

from musics.core.models import QueueItemManager
from musics.core.models import QueueItem

def get_queue(request):
    return HttpResponse(dumps(list(QueueItemManager.get_active_urls())),
                        mimetype="application/json")


def add(request):
    if request.method != 'POST':
        raise TypeError("Must be a POST request")
    url = request.POST.get('url')

    try:
        QueueItem(url=url).save()
        status = "success"
    except ValueError:
        status = "invalid url"
    except:
        status = "error"
    finally:
        return HttpResponse(dumps({'status': status}),
                            mimetype="application/json")


def dequeue(request):
    if request.method != 'POST':
        raise TypeError("Must be a POST request")

    status = QueueItemManager.dequeue()
    return HttpResponse(dumps({'status': status}),
                        mimetype="application/json")


def downvote(request):
    if request.method != 'POST':
        raise TypeError("Must be a POST request")
    
    item_id = request.POST.get('id')

    try:
        QueueItem.objects.get(id=item_id).downvote()
        status = "success"
    except:
        status = "error"
    finally:
        return HttpResponse(dumps({'status': status}),
                            mimetype="application/json")
 
 
def upvote(request):
    if request.method != 'POST':
        raise TypeError("Must be a POST request")
    
    item_id = request.POST.get('id')

    try:
        QueueItem.objects.get(id=item_id).upvote()
        status = "success"
    except:
        status = "error"
    finally:
        return HttpResponse(dumps({'status': status}),
                            mimetype="application/json")

