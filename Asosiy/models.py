from django.db import models


gender = [
    ("Erkak" , "Erkak"),
    ("Ayol" , "Ayol")
]

tirik = [
    ("Tirik" , "Tirik"),
    ("Vafot etgan" , "Vafot etgan")
]

daraja = [
    ("Bakalavr" , "Bakalavr" ),
    ("Magistr" , "Magistr")]




ish_vaqti = [
    ("8 dan 17 gacha" , "8 dan 17 gacha"),
    ("18 dan 7 gacha" , "18 dan 7 gacha"),
]


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveIntegerField( blank=True , null=True)



    def __str__(self):
        return f"{self.ism}"



class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30, choices=gender)
    tugilgan_sana = models.DateField()
    kitoblar_soni = models.PositiveIntegerField()
    tirik = models.CharField(max_length=30 , choices=tirik)

    def __str__(self):
        return f"{self.ism}"


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=39)
    sahifa = models.PositiveIntegerField()
    muallif = models.ForeignKey(Muallif , on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nom}"


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30,choices=ish_vaqti)

    def __str__(self):
        return f"{self.ism}"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba , on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olinagan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateField(null=True,blank=True)






