# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rca', '0011_auto_20150930_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventitem',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA'), (b'alumnirca', b'AlumniRCA')]),
        ),
        migrations.AlterField(
            model_name='eventitemrelatedarea',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA'), (b'alumnirca', b'AlumniRCA')]),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, editable=False, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='newsitemarea',
            name='area',
            field=models.CharField(help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='pressrelease',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, editable=False, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='pressreleasearea',
            name='area',
            field=models.CharField(help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='rcablogpage',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, editable=False, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='rcablogpagearea',
            name='area',
            field=models.CharField(help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='rcanowpage',
            name='area',
            field=models.CharField(blank=True, help_text=b"Select an area of the College only if it's relevant to your post", max_length=255, editable=False, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='rcanowpagearea',
            name='area',
            field=models.CharField(help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='researchinnovationpage',
            name='news_carousel_area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='school',
            field=models.CharField(blank=True, help_text=b'Please complete this field for academic and administrative staff only', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
        migrations.AlterField(
            model_name='staffpagerole',
            name='area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA'), (b'performance', b'Performance'), (b'moving-image', b'Moving image')]),
        ),
        migrations.AlterField(
            model_name='standardindex',
            name='events_feed_area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA'), (b'alumnirca', b'AlumniRCA')]),
        ),
        migrations.AlterField(
            model_name='standardindex',
            name='news_carousel_area',
            field=models.CharField(blank=True, help_text=b'', max_length=255, choices=[(b'administration', b'Administration'), (b'alumnirca', b'AlumniRCA'), (b'communicationsmarketing', b'Communications & Marketing'), (b'development', b'Development'), (b'drawingstudio', b'Drawing Studio'), (b'executiveeducation', b'Executive Education'), (b'fuelrca', b'Fuel RCA'), (b'helenhamlyn', b'The Helen Hamlyn Centre for Design'), (b'informationlearningtechnicalservices', b'Information, Learning & Technical Services'), (b'innovationrca', b'InnovationRCA'), (b'reachoutrca', b'ReachOutRCA'), (b'rectorate', b'Rectorate'), (b'research-knowledgeexchange', b'Research, Knowledge Exchange & Innovation'), (b'schoolofarchitecture', b'School of Architecture'), (b'schoolofcommunication', b'School of Communication'), (b'schoolofdesign', b'School of Design'), (b'schooloffineart', b'School of Fine Art'), (b'schoolofhumanities', b'School of Humanities'), (b'schoolofmaterial', b'School of Material'), (b'showrca', b'Show RCA'), (b'support', b'Support'), (b'sustainrca', b'SustainRCA')]),
        ),
    ]