# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterSentiment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lastSale',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Last Sale'),
        ),
        migrations.AlterField(
            model_name='company',
            name='marketCap',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Market Cap'),
        ),
        migrations.AlterField(
            model_name='companyaltmanzscore',
            name='zscore',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Altman Z-Score'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='current_assets',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Current Assets'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='current_liability',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Current Liability'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='ebitda',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='EBITDA'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='market_capital',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Market Capital'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='retained_earnings',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Retained Earnings'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='sales',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Sales'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='stockprice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Last Stock Price'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='total_assets',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Assets'),
        ),
        migrations.AlterField(
            model_name='companyfinancials',
            name='total_liability',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Liability'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='averagevolume',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Average Volume'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='averagevolume_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Average Volume Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='beta',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Beta'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='bookvaluepershare',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Book Value Per Share'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='bookvaluepershare_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Book Value Per Share Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='currentratio',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Current Ratio'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='currentratio_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Current Ratio Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='dilutedeps',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Diluted EPS'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='dilutedeps_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Diluted EPS Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='dividentrate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='dividentrate'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='ebitda',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Ebitda'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='ebitda_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Ebitda Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevalue',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevalue_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevalueebitda',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value Ebitda'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevalueebitda_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value Ebitda Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevaluerevenue',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value Revenue'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='enterprisevaluerevenue_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Enterprise Value Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='ex_dividentrate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='ex_dividentrate'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='fiscalyearends',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Fiscal Year Ends'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='forwardannualdividentrate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='forwardannualdividentrate'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='forwardannualdividentyield',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='forwardannualdividentyield'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='forwardpe',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Forward PE'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='forwardpe_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Forward PE Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='grossprofit',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Gross Profit'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='grossprofit_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Gross Profit Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='lastsplitdate',
            field=models.DateField(blank=True, null=True, verbose_name='lastsplitdate'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='lastsplitfactor',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='lastsplitfactor'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='lastsplitfactor_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='lastsplitfactor_term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='leveredfreecashflow',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Levered Free Cash Flow'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='leveredfreecashflow_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Levered Free Cash Flow Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='marketcap',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Market Cap'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='marketcap_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Market Cap Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='mostrecentquarter',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Most Recent Quarter'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='netincomeavltocommon',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Net Income Available to Common'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='netincomeavltocommon_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Net Income Available to Common Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='operatingcashflow',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Operating Cash Flow'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='operatingcashflow_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Operating Cash Flow Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='operatingmargin',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Operating Margin'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='operatingmargin_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Operating Margin Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p200daymovingaverage',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p200daymovingaverage'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p50daymovingaverage',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p50daymovingaverage'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p52weekchange',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p52weekchange'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p52weekhigh',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p52weekhigh'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p52weekhigh_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p52weekhigh Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p52weeklow',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p52weeklow'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p52weeklow_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p52weeklow Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='p_5yearaveragedivident',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='p_5yearaveragedivident'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='payoutratio',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='payoutratio'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pegratio',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='PEG Ratio'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pegratio_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='PEG Ratio Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='percenthldbyinsiders',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Percent Held by Insiders'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='percenthldbyinstitutions',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Percent Held by Institutions'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pricebook',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Price Book'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pricebook_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Price Book Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pricesales',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Price Sales'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='pricesales_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Price Sales Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='profitmargin',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Profit Margin'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='profitmargin_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Profit Margin Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='quarterlyearningsgrowth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Quarterly Earnings Growth'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='quarterlyearningsgrowth_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Quarterly Earnings Growth Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='quarterlyrevenuegrowth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Quarterly Revenue Growth'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='quarterlyrevenuegrowth_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Quarterly Revenue Growth Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='returnonassets',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Return On Assets'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='returnonassets_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Return on Assets Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='returnonequity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Return On Equity'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='returnonequity_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Return on Equity Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='revenue',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Revenue'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='revenue_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Revenue Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='revenuepershare',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Revenue Per Share'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='revenuepershare_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Revenue Per Share Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='sfloat',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Float'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='shareshort_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Shares Short Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='sharesoutstanding',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Shares Outstanding'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='sharesshort',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Shares Short'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='shortpercentfloat',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Short Percentage Float'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='shortpercentfloat_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Short Percentage Float Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='shortratio',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Short Ratio'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='shortratio_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Short Ratio Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='sp500p52weekchange',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='sp500p52weekchange'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totalcash',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Cash'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totalcash_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Cash Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totalcashpershare',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Cash per Share'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totalcashpershare_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Cash per Share Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totaldebt',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Debt'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totaldebt_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Debt Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totaldebtequity',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Debt Equity'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='totaldebtequity_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Total Debt Equity Term'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='trailingannualdividentrate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='trailingannualdividentrate'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='trailingannualdividentyield',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='trailingannualdividentyield'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='trailingpe',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Trailing PE'),
        ),
        migrations.AlterField(
            model_name='companykeystats',
            name='trailingpe_term',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Trailing Pe Term'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='adjs_close',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Adj Close'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='close',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Close'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='high',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='High'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='low',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Low'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='open',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Open'),
        ),
        migrations.AlterField(
            model_name='companyquotehistory',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Volume'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_prob_negative',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Negative Probability'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_prob_neutral',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Neutral Probability'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_prob_positive',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Positive Probability'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_prob_very_negative',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Very Negative Probability'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_prob_very_positive',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Very Positive Probability'),
        ),
        migrations.AlterField(
            model_name='companysentiment',
            name='sentiment_root_value',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Sentiment'),
        ),
        migrations.AlterField(
            model_name='companystockssentimenthistory',
            name='stockclose',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Stock Close'),
        ),
        migrations.AlterField(
            model_name='companystockssentimenthistory',
            name='stockopen',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=24, null=True, verbose_name='Stock Open'),
        ),
    ]