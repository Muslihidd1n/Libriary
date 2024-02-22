from django.shortcuts import render , redirect
from .forms import *
from .models import *

def hamma_kitoblar(request):
    if request.method == "POST":
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        # Kitob.objects.create(
        #     nom=request.POST.get("nomi"),
        #     janr=request.POST.get("janr"),
        #     sahifa=request.POST.get("sahifa"),
        #     muallif=Muallif.objects.get(id=request.POST.get("muallif"))
        # )
        return redirect('/kitoblar/')

    natija1 = Kitob.objects.all()
    kiritilgan_nom = request.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija1 = Kitob.objects.filter(nom__contains=kiritilgan_nom)
    context = {
        "books": natija1,
        "mualliflar" : Muallif.objects.all(),
        "forma": KitobForm
    }
    return render(request, "Kitoblar.html",context)



def hamma_studentlar(request):
    if request.method == "POST":
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            data = forma.cleaned_data
            Talaba.objects.create(
                ism=data.get("i"),
                kurs=data.get("k"),
                kitob_soni=data.get("k_s")
            )

        # Talaba.objects.create(
        # ism = request.POST.get("ismi"),
        # kurs = request.POST.get("kurs"),
        # kitob_soni = request.POST.get("kitoblar_soni")

        return redirect("/talabalar/")

    natija = Talaba.objects.all()
    kiritilgan_ism = request.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Talaba.objects.filter(ism__contains=kiritilgan_ism)

    context = {
        "studentlar": natija,
        "forma": TalabaForm()
    }
    return render(request,"Students.html",context)


def hamma_mualliflar(req):
    if req.method == 'POST':
        forma = MuallifForm(req.POST)
        if forma.is_valid():
            forma.save()
        # Muallif.objects.create(
        #     ism = req.POST.get("ismi"),
        #     jins = req.POST.get("jinsi"),
        #     tugilgan_sana = req.POST.get("t_sana"),
        #     kitoblar_soni = req.POST.get("k_soni"),
        #     tirik = req.POST.get("Holat"),
        # )

        return redirect('/h_mualliflar/')
    data = {
        "mualliflar": Muallif.objects.all(),
        "forma": MuallifForm()
    }
    return render(req,"Muallif.html" , data)



def hamma_recordlar(req):
    if req.method=="POST":
        forma = RecordForm(req.POST)
        if forma.is_valid():
            forma.save()
        # Record.objects.create(
        #     talaba = Talaba.objects.get(id=req.POST.get("studentlar")),
        #     kitob = Kitob.objects.get(id=req.POST.get("books")),
        #     kutubxonachi = Kutubxonachi.objects.get(id=req.POST.get("kutubxonachi")),
        #     olinagan_sana = req.POST.get("t_sana"),
        #     qaytardi = False,
        #     qaytarish_sana = req.POST.get("q_sana")
        # )
        return redirect("/hamma_recordlar/")

    data = {
        "record": Record.objects.all(),
        "books": Kitob.objects.all(),
        "studentlar": Talaba.objects.all(),
        "kutubxonachi": Kutubxonachi.objects.all(),
        "forma": RecordForm
    }
    return render(req,"Record.html",data)



def hamma_kutubxonachilar(req):
    if req.method=="POST":
        forma = KutubxonachiForm(req.POST)
        if forma.is_valid():
            forma.save()
        # Kutubxonachi.objects.create(
        #     ism = req.POST.get("ismi"),
        #     ish_vaqti = req.POST.get(id=req.POST.get("ish_vaqti"))
        # )
        # return redirect('/hamma_kutubxonachilar/')

    natijjja = Kutubxonachi.objects.all()
    kiritilgan_ism=req.GET.get('ismi')
    if kiritilgan_ism is not None:
        natijjja=Kutubxonachi.objects.filter(ism__contains=kiritilgan_ism)

    data = {
        "kutubxonachi": natijjja,
        "forma": KutubxonachiForm
    }
    return render(req,"Kutubxonachi.html",data)





def bitta_talaba(req,pk):
    data = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(req, 'bitta_talaba.html',data)


def bitta_kitob(req,pk):
    data = {
        "kitob": Kitob.objects.get(id=pk)
    }
    return render(req, 'bitta_kitob.html',data)


"Mslumot ochirish "

def talaba_ochir(req,pk):
    Talaba.objects.get(id=pk).delete()
    return redirect("/talabalar/")


def kitob_ochir(req,pk):
    Kitob.objects.get(id=pk).delete()
    return redirect('/kitoblar/')


def muallif_ochir(req,pk):
    Muallif.objects.get(id=pk).delete()
    return redirect('/h_mualliflar/')


def record_ochir(req,pk):
    Record.objects.get(id=pk).delete()
    return redirect('/hamma_recordlar/')



"Malumotni taxrirlash"


def talaba_update(request , pk):
    if request.method == "POST":
        Talaba.objects.filter(id=pk).update(
            ism = request.POST.get("ismi"),
            kurs = request.POST.get("kurs"),
            kitob_soni = request.POST.get("kitoblar_soni")
        )
        return redirect('/talabalar/')

    content = {
        "talaba": Talaba.objects.get(id=pk)
    }
    return render(request, "talaba_taxrirlash.html",content)



def kitob_update(request,pk):
    if request.method == "POST":
        Kitob.objects.filter(id=pk).update(
            nom = request.POST.get("nomi"),
            janr = request.POST.get("janr"),
            sahifa = request.POST.get("sahifa"),
            muallif = Muallif.objects.get(id=request.POST.get("muallif"))
        )
        return redirect('/kitoblar/')
    content = {
        "kitob": Kitob.objects.get(id=pk),
        "muallif": Muallif.objects.all()
    }
    return render(request,"kitob_update.html",content)

"1 masala"

def kutubxonachi_update(request,pk):
    if request.method == "POST":
        Kutubxonachi.objects.filter(id=pk).update(
            ism = request.POST.get("ismi"),
            ish_vaqti = request.POST.get("ish_vaqti")
        )
        return redirect('/hamma_kutubxonachilar')
    content = {
        "kutubxonachi": Kutubxonachi.objects.get(id=pk)
    }
    return render(request,"kutubxonachi_update.html",content)

"2 masala"

def muallif_update(request,pk):
    if request.method == "POST":
        Muallif.objects.filter(id=pk).update(
        ism = request.POST.get("ismi"),
        jins = request.POST.get("jinsi"),
        tugilgan_sana = request.POST.get("tugilgan_sana"),
        kitoblar_soni = request.POST.get("kitoblar_soni"),
        tirik = request.POST.get("tirik")
        )
        return redirect('/h_mualliflar/')
    content = {
        "muallif": Muallif.objects.get(id=pk)
    }
    return render( request,"muallif_update.html",content)

"3 masala"


def record_update(request, pk):
    if request.method == "POST":
        Record.objects.filter(id=pk).update(
            qaytardi = request.POST.get("qaytardi"),
            qaytarish_sana =request.POST.get("olingan_sana")
        )
        return redirect("/hamma_recordlar")
    content = {
        "talaba": Talaba.objects.all(),
        "kitob": Kitob.objects.all(),
        "kutubxonachi": Kutubxonachi.objects.all(),
        "record": Record.objects.filter(id=pk)
    }
    return render(request,"record_update.html",content)



