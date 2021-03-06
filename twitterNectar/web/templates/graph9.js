var seriesJS9 = {{ series9|safe }}
var categoriesJS = {{ categories|safe }}
Highcharts.chart('container9', {
    chart: {
        zoomType: 'xy', 
        width : 600,
        height : null,
    },
    title: {
        text: 'Personal History VS Normalized number of Tweets'
    },
    subtitle: {
        text: 'Born in Asia'
    },
    xAxis: [{
        categories: categoriesJS,
        crosshair: true
    }],
    yAxis: [{ // Primary yAxis
        labels: {
            format: '{value}',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        },
        title: {
            text: 'Normalized num of Tweets',
            style: {
                color: Highcharts.getOptions().colors[1]
            }
        }
    }, { // Secondary yAxis
        title: {
            text: 'Percentage',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        labels: {
            format: '{value} %',
            style: {
                color: Highcharts.getOptions().colors[0]
            }
        },
        opposite: true
    }],
    tooltip: {
        shared: true
    },
    legend: {
        layout: 'vertical',
        x: 150,
        verticalAlign: 'top',
        y: 70,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255,255,255,0.25)'
    },
    series: seriesJS9
});
