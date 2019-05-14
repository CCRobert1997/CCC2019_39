#Shangyu Chen 743125
#Xiangxue Li 762925
#Xiyue Wang 683843
#Yuemin Huang 752563
#Zhixin Lin 971382
import json
from flask import Flask, render_template
from collections import OrderedDict

# from pprint import pprint

# import db
app = Flask(__name__)

percen_data = {
    'name': 'Percentage',
    'type': 'column',
    'yAxis': 1,
    'data': [],
    'tooltip': {
        'valueSuffix': ' %'
    }}
norm_data = {
    'name': 'Normalized num of tweets',
    'type': 'spline',
    'data': [],
    'tooltip': {
        'valueSuffix': ''
    }}


@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html")


@app.route('/member')
def memberpage():
    return render_template("member.html")


@app.route('/analysis')
def analysistest():
    return render_template('dataanalysis.html')

@app.route('/graph1.js')
def timeline1():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    vic_place = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne', 'Average of all areas']
    nsw_place = ['Newcastle', 'Sydney', 'Wollongong', 'Average of all areas']
    qld_place = ['Brisbane', 'Townsville', 'Cairns', 'Average of all areas']

    json_series = []
    vic_series = []
    nsw_series = []
    qld_series = []
    categories = [str] * 4

    # for key, value in data.items():
    #     new_data = {
    #         'name': str(key),
    #         'data': [int] * 4
    #     }
    #     # print key
    #     for time, count in value.items():
    #         if len(categories) < 4:
    #             categories.append(str(time))
    #         new_data['data'].append(count)
    #         # print str(time)
    #     json_series.append(new_data)

    for key, value in data.items():
        new_data = {
            'name': str(key),
            'data': [0] * 4
        }
        for time, count in value.items():
            if str(time) == "00:00 - 05:59":
                categories[0] = str(time)
                new_data['data'][0] = count
            elif str(time) == "06:00 - 11:59":
                categories[1] = str(time)
                new_data['data'][1] = count
            elif str(time) == "12:00 - 17:59":
                categories[2] = str(time)
                new_data['data'][2] = count
            elif str(time) == "18:00 - 23:59":
                categories[3] = str(time)
                new_data['data'][3] = count

        json_series.append(new_data)

        if new_data["name"] in vic_place:
            vic_series.append(new_data)
        if new_data['name'] in nsw_place:
            nsw_series.append(new_data)
        if new_data["name"] in qld_place:
            qld_series.append(new_data)

    return render_template('graph1.js', series1=vic_series, categories=categories)


# @app.route('/graph1.js')
# def timeline1():
#
#     with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
#         data = json.load(f, object_pairs_hook=OrderedDict)
#
#     vic_place = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne', 'Average of all areas']
#     nsw_place = ['Newcastle', 'Sydney', 'Wollongong', 'Average of all areas']
#     qld_place = ['Brisbane', 'Townsville', 'Cairns', 'Average of all areas']
#
#     json_series = []
#     vic_series = []
#     nsw_series = []
#     qld_series = []
#     categories = [str] * 4
#     for key, value in data.items():
#         new_data = {
#             'name': str(key),
#             'data': [int] * 4
#         }
#         # print key
#
#         for time, count in value.items():
#             if len(categories) < 4:
#                 categories.append(str(time))
#             new_data['data'].append(count)
#         json_series.append(new_data)
#
#         if new_data["name"] in vic_place:
#             vic_series.append(new_data)
#         if new_data['name'] in nsw_place:
#             nsw_series.append(new_data)
#         if new_data["name"] in qld_place:
#             qld_series.append(new_data)
#     return render_template('graph1.js', series1=vic_series, categories=categories)

@app.route('/graph2.js')
def timeline2():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    vic_place = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne', 'Average of all areas']
    nsw_place = ['Newcastle', 'Sydney', 'Wollongong', 'Average of all areas']
    qld_place = ['Brisbane', 'Townsville', 'Cairns', 'Average of all areas']

    json_series = []
    vic_series = []
    nsw_series = []
    qld_series = []


    categories = [str] * 4

    for key, value in data.items():
        new_data = {
            'name': str(key),
            'data': [int] * 4
        }
        for time, count in value.items():
            if str(time) == "00:00 - 05:59":
                categories[0] = str(time)
                new_data['data'][0] = count
            elif str(time) == "06:00 - 11:59":
                categories[1] = str(time)
                new_data['data'][1] = count
            elif str(time) == "12:00 - 17:59":
                categories[2] = str(time)
                new_data['data'][2] = count
            elif str(time) == "18:00 - 23:59":
                categories[3] = str(time)
                new_data['data'][3] = count

        json_series.append(new_data)

        if new_data["name"] in vic_place:
            vic_series.append(new_data)
        if new_data['name'] in nsw_place:
            nsw_series.append(new_data)
        if new_data["name"] in qld_place:
            qld_series.append(new_data)
    # print nsw_series
    # print categories
    return render_template('graph2.js', series2=nsw_series, categories=categories)


@app.route('/graph3.js')
def timeline3():
    with open('web/json_output/content and timeline/number of tweets in time ranges of a day.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    vic_place = ['Ballarat', 'Bendigo', 'Geelong', 'Melbourne', 'Average of all areas']
    nsw_place = ['Newcastle', 'Sydney', 'Wollongong', 'Average of all areas']
    qld_place = ['Brisbane', 'Townsville', 'Cairns', 'Average of all areas']

    json_series = []
    vic_series = []
    nsw_series = []
    qld_series = []
    categories = [str] * 4

    # for key, value in data.items():
    #     new_data = {
    #         'name': str(key),
    #         'data': [int] * 4
    #     }
    #     # print key
    #     for time, count in value.items():
    #         if len(categories) < 4:
    #             categories.append(str(time))
    #         new_data['data'].append(count)
    #         # print str(time)
    #     json_series.append(new_data)

    for key, value in data.items():
        new_data = {
            'name': str(key),
            'data': [int] * 4
        }
        for time, count in value.items():
            if str(time) == "00:00 - 05:59":
                categories[0] = str(time)
                new_data['data'][0] = count
            elif str(time) == "06:00 - 11:59":
                categories[1] = str(time)
                new_data['data'][1] = count
            elif str(time) == "12:00 - 17:59":
                categories[2] = str(time)
                new_data['data'][2] = count
            elif str(time) == "18:00 - 23:59":
                categories[3] = str(time)
                new_data['data'][3] = count

        json_series.append(new_data)

        if new_data["name"] in vic_place:
            vic_series.append(new_data)
        if new_data['name'] in nsw_place:
            nsw_series.append(new_data)
        if new_data["name"] in qld_place:
            qld_series.append(new_data)

    return render_template('graph3.js', series3=qld_series, categories=categories)


@app.route('/graph4.js')
def edulevel9():
    with open('web/json_output/scenario/education level.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    categories = []
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    series4 = [percen_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Completed Year 9 or equivalent (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph4.js', series4=series4, categories=categories)


#
@app.route('/graph5.js')
def edulevel10():
    with open('web/json_output/scenario/education level.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    categories = []
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    series5 = [percen_data, norm_data]
    for key, value in data.items():
        for types, count in value.items():
            if types == "Persons with Postgraduate degree (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    # print(series5)
    return render_template('graph5.js', series5=series5, categories=categories)


@app.route('/graph6.js')
def employtypelabour():
    with open('web/json_output/scenario/employment type.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    categories = []
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    series6 = [percen_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Labourers (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph6.js', series6=series6, categories=categories)


#


@app.route('/graph7.js')
def employtypeprof():
    with open('web/json_output/scenario/employment type.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    categories = []
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    series7 = [percen_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Professionals (%)":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)

    return render_template('graph7.js', series7=series7, categories=categories)


@app.route('/graph8.js')
def gini():
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    gini_data = {
        'name': 'Gini coefficient',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    categories = []
    with open('web/json_output/scenario/income.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    series8 = [gini_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Gini coefficient":
                gini_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    # print (series8)
    return render_template('graph8.js', series8=series8, categories=categories)


@app.route('/graph9.js')
def bornasia():
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    categories = []
    with open('web/json_output/scenario/background.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    series9 = [percen_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Born in Asia":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    return render_template('graph9.js', series9=series9, categories=categories)


#
@app.route('/graph10.js')
def borneur():
    percen_data = {
        'name': 'Percentage',
        'type': 'column',
        'yAxis': 1,
        'data': [],
        'tooltip': {
            'valueSuffix': ' %'
        }}
    norm_data = {
        'name': 'Normalized num of tweets',
        'type': 'spline',
        'data': [],
        'tooltip': {
            'valueSuffix': ''
        }}
    categories = []
    with open('web/json_output/scenario/background.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    series10 = [percen_data, norm_data]
    for key, value in data.items():
        if len(categories) < 10:
            categories.append(str(key))
        for types, count in value.items():
            if types == "Born in Europe":
                percen_data['data'].append(float(count))
            elif types == "normalised total number of envy tweets per year":
                norm_data['data'].append(count)
    return render_template('graph10.js', series10=series10, categories=categories)


#@app.route('/index')
#def index():
#    categories = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
#
#    #chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
#    series = [
#        {
#        'name': 'John',
#        'data': [5, 3, 4, 7, 2]
#        },
#        {
#        'name': 'Jane',
#        'data': [2, 2, 3, 2, 1]
#        }
#    ]
#    #db.samplefunction()
#    #title = {"text": 'My Title'}
#    #xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
#    #yAxis = {"title": {"text": 'yAxis Label'}}
#
#    return render_template('index.html', series=series, categories=categories)
#



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=80, passthrough_errors=True)

#if __name__ == "__main__":
#    app.run(debug = True)

# , host='127.0.0.1', port=80, passthrough_errors=True
