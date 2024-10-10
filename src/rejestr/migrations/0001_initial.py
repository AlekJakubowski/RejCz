# Generated by Django 5.1.2 on 2024-10-08 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CzynnoscPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czn_active', models.BooleanField(default=True, null=True)),
                ('czn_nazwa', models.CharField(max_length=200)),
                ('czn_zrodlo_danych', models.CharField(choices=[('Osoba', 'Bezpośrednio od osoby, której dane dotyczą'), ('Inni', 'Od innej osoby, niż osoba której dane dotyczą'), ('Różne', 'Od osoby, której dane dotyczą lub od innych osób')], max_length=100, null=True)),
                ('czn_status_zatw', models.CharField(choices=[('-----------', '-----------'), ('OCZEKUJĄCA', 'Oczekuje na zatwierdzenie'), ('ZATWIERDZONA', 'Zatwierdzona i obowiązująca'), ('ODRZUCONA', 'Odrzucona po rozpatrzeniu'), ('ANULOWANA', 'Anulowana i nieobowiązująca')], max_length=20, null=True)),
                ('czn_pozycja_rej', models.IntegerField(null=True)),
                ('czn_przepis_wrazliwe', models.CharField(max_length=200)),
                ('czn_podstawa_prawna', models.CharField(max_length=300)),
                ('czn_opis_celu', models.CharField(max_length=200)),
                ('czn_data_zgloszenia', models.DateField(null=True)),
                ('czn_data_wyrejestrowania', models.DateField(null=True)),
                ('czn_data_obowazywania_od', models.DateField(null=True)),
                ('czn_data_obowazywania_do', models.DateField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupaZabezpieczen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gzb_active', models.BooleanField(default=True)),
                ('gzb_opis', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrupaZagrozen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gzg_active', models.BooleanField(default=True)),
                ('gzg_opis', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='iod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='KategoriaDanych',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kd_active', models.BooleanField(default=True)),
                ('kd_skrot', models.CharField(max_length=100)),
                ('kd_opis', models.TextField(max_length=300)),
                ('kd_dane_szczegolne', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='KategoriaOdbiorcow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kto_active', models.BooleanField(default=True)),
                ('kto_skrot', models.CharField(max_length=100)),
                ('kto_opis', models.TextField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='KategoriaOsob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ko_active', models.BooleanField(default=True)),
                ('ko_skrot', models.CharField(max_length=100)),
                ('ko_opis', models.TextField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OkresRetencji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okr_active', models.BooleanField(default=True)),
                ('okr_nazwa', models.CharField(max_length=255)),
                ('okr_opis_okresu', models.CharField(max_length=200)),
                ('okr_lat_max', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperacjaPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opp_active', models.BooleanField(default=True, null=True)),
                ('opp_opis', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_active', models.BooleanField(default=True)),
                ('org_skrot', models.CharField(max_length=30)),
                ('org_nazwa', models.CharField(max_length=155)),
                ('org_adres', models.CharField(max_length=100)),
                ('org_email', models.EmailField(max_length=50)),
                ('org_www', models.URLField(max_length=100)),
                ('org_tel', models.CharField(max_length=100)),
                ('org_iod_name', models.CharField(max_length=100)),
                ('org_iod_email', models.EmailField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodmiotPrzetwarzajacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prz_active', models.BooleanField(default=True)),
                ('prz_skrot', models.CharField(max_length=30)),
                ('prz_nazwa', models.CharField(max_length=155)),
                ('prz_adres', models.CharField(max_length=100)),
                ('prz_email', models.EmailField(max_length=50)),
                ('prz_www', models.URLField(max_length=100)),
                ('prz_tel', models.CharField(max_length=100)),
                ('prz_iod_name', models.CharField(max_length=100)),
                ('prz_iod_email', models.EmailField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodstawaPrawnaPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppw_active', models.BooleanField(default=True)),
                ('ppw_skrot', models.CharField(max_length=100)),
                ('ppw_opis', models.TextField(max_length=500)),
                ('ppw_tresc', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrzeslankaLegalnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prl_active', models.BooleanField(default=True, null=True)),
                ('prl_skrot', models.CharField(max_length=100)),
                ('prl_art_rodo', models.CharField(max_length=100)),
                ('prl_przepis_rodo', models.CharField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SposobPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_active', models.BooleanField(default=True)),
                ('sp_skrot', models.CharField(max_length=100)),
                ('sp_opis', models.CharField(max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WysokieRyzyko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wr_active', models.BooleanField(default=True)),
                ('wr_skrot', models.CharField(max_length=100)),
                ('wr_opis', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZakresOddzialywania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zao_Poufnosc', models.BooleanField(default=True)),
                ('zao_Integralnosc', models.BooleanField(default=True)),
                ('zao_Dostepnosc', models.BooleanField(default=True)),
                ('zao_Rozliczalnosc', models.BooleanField(default=True)),
                ('zao_CiagloscDzialania', models.BooleanField(default=True)),
                ('zao_StratyWizerunkowe', models.BooleanField(default=True)),
                ('zao_NaruszeniePrIW', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CzynnosciPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czp_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='czp_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
            ],
        ),
        migrations.CreateModel(
            name='Administratorzy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adm_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('adm_organizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adm_organizacja_f', to='rejestr.organizacja')),
            ],
        ),
        migrations.CreateModel(
            name='CzynnoscPrzetwarzaniaDODO',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rejestr.czynnoscprzetwarzania',),
        ),
        migrations.CreateModel(
            name='CzynnoscPrzetwarzaniaRODO',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rejestr.czynnoscprzetwarzania',),
        ),
        migrations.CreateModel(
            name='KategoriaCzynnosciPrzetwarzaniaDODO',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rejestr.czynnoscprzetwarzania',),
        ),
        migrations.CreateModel(
            name='KategoriaCzynnosciPrzetwarzaniaRODO',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('rejestr.czynnoscprzetwarzania',),
        ),
        migrations.CreateModel(
            name='KategorieDanych',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktd_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ktd_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('ktd_dane', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ktd_dane_p', to='rejestr.kategoriadanych')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='KategorieDanych',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_KategoriaDanych', through='rejestr.KategorieDanych', to='rejestr.kategoriadanych'),
        ),
        migrations.CreateModel(
            name='KategorieOdbiorcow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kob_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kob_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('kob_odbiorcy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kob_odbiorcy_p', to='rejestr.kategoriaodbiorcow')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='KategorieOdbiorcow',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_KategoriaOdbiorcow', through='rejestr.KategorieOdbiorcow', to='rejestr.kategoriaodbiorcow'),
        ),
        migrations.CreateModel(
            name='KategorieOsob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kos_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kos_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('kos_kosoby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kos_kosoby_p', to='rejestr.kategoriaosob')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='KategorieOsob',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_KategoriaOsob', through='rejestr.KategorieOsob', to='rejestr.kategoriaosob'),
        ),
        migrations.CreateModel(
            name='Komorka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kom_active', models.BooleanField(default=True)),
                ('kom_symbol', models.CharField(max_length=10)),
                ('kom_nazwa', models.CharField(max_length=255)),
                ('kom_adres', models.CharField(max_length=255)),
                ('kom_tel', models.CharField(max_length=100)),
                ('kom_email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('CzynnosciRealizowane', models.ManyToManyField(related_name='Komorki_CzynnosciPrzetwarzania', through='rejestr.CzynnosciPrzetwarzania', to='rejestr.czynnoscprzetwarzania')),
                ('Organizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.organizacja')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='KomorkiRealizujace',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_Komorki', through='rejestr.CzynnosciPrzetwarzania', to='rejestr.komorka'),
        ),
        migrations.AddField(
            model_name='czynnosciprzetwarzania',
            name='czp_komorka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='czp_komorka_p', to='rejestr.komorka'),
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='OkresRetencji',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.okresretencji'),
        ),
        migrations.CreateModel(
            name='OperacjePrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opp_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opp_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('opp_operacjap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opp_operacjap_p', to='rejestr.operacjaprzetwarzania')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='OperacjePrzetwarzania',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_OperacjePrzetwarzania', through='rejestr.OperacjePrzetwarzania', to='rejestr.operacjaprzetwarzania'),
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='Administratorzy',
            field=models.ManyToManyField(related_name='Organizacja_Administratorzy', through='rejestr.Administratorzy', to='rejestr.organizacja'),
        ),
        migrations.CreateModel(
            name='PodmiotyPrzetwarzajace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pod_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('pod_organizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pod_pprzetw_p', to='rejestr.podmiotprzetwarzajacy')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='PodmiotyPrzetwarzajace',
            field=models.ManyToManyField(related_name='PodmiotPrzetw_PodmiotyPrzetwarzajace', through='rejestr.PodmiotyPrzetwarzajace', to='rejestr.podmiotprzetwarzajacy'),
        ),
        migrations.CreateModel(
            name='PrzeslankiLegalnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppl_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ppl_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('ppl_przeslankap', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ppl_przeslanka_p', to='rejestr.przeslankalegalnosci')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='PrzeslankiLegalnosci',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_PrzeslankaLegalnosci', through='rejestr.PrzeslankiLegalnosci', to='rejestr.przeslankalegalnosci'),
        ),
        migrations.CreateModel(
            name='Rejestr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rej_active', models.BooleanField(default=True)),
                ('rej_nazwa', models.CharField(max_length=200)),
                ('rej_opis', models.TextField(max_length=200)),
                ('rej_zakres', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('Organizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.organizacja')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='Rejestr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.rejestr'),
        ),
        migrations.CreateModel(
            name='SposobyPrzetwarzania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spp_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spp_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('spp_sposobp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spp_sposob_p', to='rejestr.sposobprzetwarzania')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='SposobyPrzetwarzania',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_SposobyPrzetwarzania', through='rejestr.SposobyPrzetwarzania', to='rejestr.sposobprzetwarzania'),
        ),
        migrations.CreateModel(
            name='Wspoladministratorzy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wad_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wad_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('wad_organizacja', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wad_organizacja_f', to='rejestr.organizacja')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='Wspoladministratorzy',
            field=models.ManyToManyField(related_name='Organizacja_Wspoladministratorzy', through='rejestr.Wspoladministratorzy', to='rejestr.organizacja'),
        ),
        migrations.CreateModel(
            name='WysokieRyzyka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrr_czynnoscp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wrr_czynnosc_p', to='rejestr.czynnoscprzetwarzania')),
                ('wrr_wryzyka', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wrr_wryzyka_p', to='rejestr.wysokieryzyko')),
            ],
        ),
        migrations.AddField(
            model_name='czynnoscprzetwarzania',
            name='WysokieRyzyka',
            field=models.ManyToManyField(related_name='CzynnoscPrzetwarzania_WysokieRyzyko', through='rejestr.WysokieRyzyka', to='rejestr.wysokieryzyko'),
        ),
        migrations.CreateModel(
            name='Zabezpieczenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zab_active', models.BooleanField(default=True, null=True)),
                ('zab_skrot', models.CharField(max_length=30)),
                ('zab_opis', models.CharField(max_length=300)),
                ('zab_waga', models.IntegerField(null=True)),
                ('komorka', models.CharField(max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('GrupyZabezpieczen', models.ManyToManyField(to='rejestr.grupazabezpieczen')),
                ('Odpowiedzialni', models.ManyToManyField(to='rejestr.organizacja')),
            ],
        ),
        migrations.CreateModel(
            name='Zagrozenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zag_active', models.BooleanField(default=True)),
                ('zag_skrot', models.CharField(max_length=30)),
                ('zag_opis', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('GrupaZagrozen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.grupazagrozen')),
            ],
        ),
        migrations.CreateModel(
            name='Podatnosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdt_active', models.BooleanField(default=True, null=True)),
                ('pdt_skrot', models.CharField(max_length=30)),
                ('pdt_opis', models.CharField(max_length=300)),
                ('pdt_waga', models.IntegerField(default=0)),
                ('Zagrozenia', models.ManyToManyField(to='rejestr.zagrozenie')),
            ],
        ),
        migrations.CreateModel(
            name='Ryzyko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rr_SkalaPodatnosci', models.IntegerField(default=0)),
                ('rr_prawdopodobienstwo_bp', models.IntegerField(default=0)),
                ('rr_prawdopodobienstwo', models.IntegerField(default=0)),
                ('rr_odzialywanie', models.IntegerField(default=0)),
                ('rr_ryzyko', models.IntegerField(default=0)),
                ('rr_redukcja', models.IntegerField(default=0)),
                ('rr_szczatkowe', models.IntegerField(default=0)),
                ('rr_postepowanie', models.CharField(default='M', max_length=30)),
                ('rr_uzasadnieniePrawdopodobienstwa', models.CharField(max_length=500)),
                ('rr_uzasadnienieOddzialywania', models.CharField(max_length=500)),
                ('rr_uzasadnienieOddzialywania_atr', models.CharField(max_length=500)),
                ('rr_uzasadnieniePostepowania', models.CharField(max_length=500)),
                ('rr_analizaRyzyka', models.CharField(max_length=500)),
                ('Zabezpieczenia', models.ManyToManyField(to='rejestr.zabezpieczenie')),
                ('Zagrozenie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rejestr.zagrozenie')),
                ('ZakresOddzialywania', models.ManyToManyField(to='rejestr.zakresoddzialywania')),
            ],
        ),
    ]