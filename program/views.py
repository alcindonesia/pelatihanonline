from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from soal.models import Soal, Submission
from account.models import Membership
from .models import Event, Paket
from pelatihanonline.constants import get_full_subject


def index(request):
    events = Event.objects.filter(aktif=True).order_by('-id')
    userprofile = None
    if request.user and not request.user.is_anonymous:
        userprofile = request.user.userprofile

    return render(request, 'index.html', {'events': events,
                                          'userprofile': userprofile})


@login_required
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    pakets = Paket.objects.filter(event=event)
    userprofile = request.user.userprofile
    membership_set = userprofile.membership_set.filter(userprofile=userprofile,
                                                       event=event,
                                                       confirmed=True)
    if not membership_set:
        return HttpResponse('Unauthorized Access', status=401)
    return render(request, 'detail.html', {'event': event,
                                           'pakets': pakets,
                                           'bidang': userprofile.bidang})

@login_required
def daftar(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    userprofile = request.user.userprofile
    membership, created = Membership.objects.get_or_create(userprofile=userprofile,
                                                           event=event,
                                                           confirmed=False)
    return redirect(reverse('event_index'))

@login_required
def detail_paket(request, event_id, paket_id, bidang):
    userprofile = request.user.userprofile
    nama = userprofile.nama_lengkap
    guru = userprofile.role == 'GUR'
    event = get_object_or_404(Event, pk=event_id)
    paket = get_object_or_404(Paket, pk=paket_id)
    nomor_paket = paket.nomor_paket
    membership_set = userprofile.membership_set.filter(userprofile=userprofile,
                                                       event=event,
                                                       confirmed=True)

    if userprofile.bidang != bidang:
        return HttpResponse('Unauthorized Access', status=401)
    if paket.event != event:
        return HttpResponse('Unauthorized Access', status=401)
    if not membership_set:
        return HttpResponse('Unauthorized Access', status=401)

    soal = get_object_or_404(Soal,
                             bundel_soal=paket.bundel_soal,
                             bidang=userprofile.bidang)
    submission, created = Submission.objects.get_or_create(userprofile=userprofile,
                                                           bidang=userprofile.bidang,
                                                           paket=paket)

    if not paket.selesai():
        if request.method == 'POST':
            for i in range(1, 31):
                num = 'no' + str(i)
                setattr(submission, num, request.POST.get('no' + str(i), '-'))
            submission.save()
            submission.grade()

    soal_dict = model_to_dict(soal)
    submission_dict = model_to_dict(submission)
    nilai = submission.nilai

    ranking = Submission.objects.select_related('userprofile').filter(bidang=userprofile.bidang,
                                                                      paket__nomor_paket=nomor_paket,
                                                                      userprofile__role='SIS').order_by('-nilai')

    format = '%m/%d/%Y %I:%M %p'
    close_time = timezone.localtime(paket.close_time).strftime(format)
    site = request.META['HTTP_HOST']

    return render(request, 'detail_paket.html', {'event': event,
                                                 'paket': paket,
                                                 'bidang': bidang,
                                                 'bidang_full': get_full_subject(bidang),
                                                 'soal': soal,
                                                 'soal_dict': soal_dict,
                                                 'submission_dict': submission_dict,
                                                 'ranking': ranking,
                                                 'close_time': close_time,
                                                 'site': site,
                                                 'nama': nama,
                                                 'nilai': nilai,
                                                 'guru': guru,
                                                 'range10': range(10),
                                                 'range3': range(3)})
