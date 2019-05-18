json2chart = function(json){
        console.log(json); // this will show the info it in firebug console
//        chart1DataPoints = json
//        chart1Data = ;
        var chart = new CanvasJS.Chart("chartContainer", json
//        {
//            title:{text: "My First Chart in CanvasJS"},
//            data: {type: "spline", dataPoints: chart1DataPoints}
//        }
        );
        chart.render();
}

chartLoad = function () {

    $.getJSON("../res/201903/temp_20190301.json", json2chart);
};

