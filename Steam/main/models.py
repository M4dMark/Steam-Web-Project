from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hodnoceni(models.Model):
    idhodnoceni = models.AutoField(db_column='idHodnoceni', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(db_column='Nazev', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doporuceni = models.IntegerField(db_column='Doporuceni', blank=True, null=True)  # Field name made lowercase.
    text_recenze = models.TextField(db_column='Text_recenze', blank=True, null=True)  # Field name made lowercase.
    uzivatele_iduzivatele = models.ForeignKey('Uzivatele', models.DO_NOTHING, db_column='Uzivatele_idUzivatele')  # Field name made lowercase.
    hry_idhry = models.ForeignKey('Hry', models.DO_NOTHING, db_column='Hry_idHry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hodnoceni'


class Hry(models.Model):
    idhry = models.AutoField(db_column='idHry', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(db_column='Nazev', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cena_v_eur = models.FloatField(db_column='Cena_v_eur', blank=True, null=True)  # Field name made lowercase.
    trzby_v_eur = models.FloatField(db_column='Trzby_v_eur', blank=True, null=True)  # Field name made lowercase.
    prodanych_kusu = models.IntegerField(db_column='Prodanych_kusu', blank=True, null=True)  # Field name made lowercase.
    publisher_idpublisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_idPublisher')  # Field name made lowercase.
    vyvojar_idvyvojar = models.ForeignKey('Vyvojar', models.DO_NOTHING, db_column='Vyvojar_idVyvojar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hry'


class HryHasUzivatele(models.Model):
    hry_idhry = models.OneToOneField(Hry, models.DO_NOTHING, db_column='Hry_idHry', primary_key=True)  # Field name made lowercase.
    uzivatele_iduzivatele = models.ForeignKey('Uzivatele', models.DO_NOTHING, db_column='Uzivatele_idUzivatele')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hry_has_uzivatele'
        unique_together = (('hry_idhry', 'uzivatele_iduzivatele'),)


class HryHasZanr(models.Model):
    hry_idhry = models.OneToOneField(Hry, models.DO_NOTHING, db_column='Hry_idHry', primary_key=True)  # Field name made lowercase.
    zanr_idzanr = models.ForeignKey('Zanr', models.DO_NOTHING, db_column='Zanr_idZanr')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hry_has_zanr'
        unique_together = (('hry_idhry', 'zanr_idzanr'),)


class Publisher(models.Model):
    idpublisher = models.AutoField(db_column='idPublisher', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(db_column='Nazev', max_length=128, blank=True, null=True)  # Field name made lowercase.
    popis = models.TextField(db_column='Popis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher'


class Uzivatele(models.Model):
    iduzivatele = models.AutoField(db_column='idUzivatele', primary_key=True)  # Field name made lowercase.
    nick = models.CharField(db_column='Nick', max_length=45, blank=True, null=True)  # Field name made lowercase.
    heslo = models.CharField(db_column='Heslo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vlastneno_her = models.IntegerField(db_column='Vlastneno_her', blank=True, null=True)  # Field name made lowercase.
    uzivatelske_jmeno = models.CharField(db_column='Uzivatelske_jmeno', max_length=64, blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uzivatele'


class Vyvojar(models.Model):
    idvyvojar = models.AutoField(db_column='idVyvojar', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(db_column='Nazev', max_length=45, blank=True, null=True)  # Field name made lowercase.
    popis = models.TextField(db_column='Popis', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vyvojar'


class Zanr(models.Model):
    idzanr = models.AutoField(db_column='idZanr', primary_key=True)  # Field name made lowercase.
    nazev = models.CharField(db_column='Nazev', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zanr'
