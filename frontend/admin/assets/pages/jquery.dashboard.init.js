var dash_spark_1 = {
    chart: {
        type: "area",
        height: 80,
        sparkline: {
            enabled: !0
        }
    },
    stroke: {
        curve: "smooth",
        width: 2
    },
    fill: {
        opacity: .05
    },
    series: [{
        data: [4, 8, 5, 10, 4, 16, 5, 11, 6, 11, 30, 10]
    }],
    yaxis: {
        min: 0
    },
    colors: ["#fbb624"],
    tooltip: {
        theme: "dark"
    }
};
new ApexCharts(document.querySelector("#dash_spark_1"), dash_spark_1).render();
var options = {
    chart: {
        height: 80,
        animations: {
            enabled: !1
        },
        sparkline: {
            enabled: !0
        },
        type: "bar"
    },
    plotOptions: {
        bar: {
            horizontal: !1,
            endingShape: "rounded",
            columnWidth: "40%"
        }
    },
    dataLabels: {
        enabled: !1
    },
    stroke: {
        show: !0,
        width: 2,
        colors: ["transparent"]
    },
    colors: ["#1ecab8"],
    series: [{
        name: "Revenue",
        data: [50, 60, 70, 80, 90, 100, 95, 85, 75, 65, 55, 65, 75, 85, 95, 105, 80, 70, 60, 50, 40, 30, 45, 55, 65, 75, 85, 95, 100, 80, 60]
    }],
    xaxis: {
        categories: ["1-Jan", "2-Jan", "3-Jan", "4-Jan", "5-Jan", "6-Jan", "7-Jan", "8-Jan", "9-Jan", "10-Jan", "11-Jan", "12-Jan", "13-Jan", "14-Jan", "15-Jan", "16-Jan", "17-Jan", "18-Jan", "19-Jan", "20-Jan", "21-Jan", "22-Jan", "23-Jan", "24-Jan", "25-Jan", "26-Jan", "27-Jan", "28-Jan", "29-Jan", "30-Jan", "31-Jan"],
        crosshairs: {
            show: !1
        }
    },
    fill: {
        opacity: .5
    },
    tooltip: {
        theme: "dark",
        y: {
            formatter: function(a) {
                return "$ " + a + " thousands"
            }
        }
    }
};
(chart = new ApexCharts(document.querySelector("#apex_column1"), options)).render();
options = {
    chart: {
        height: 180,
        type: "radialBar"
    },
    series: [67],
    colors: ["#20E647"],
    plotOptions: {
        radialBar: {
            hollow: {
                margin: 0,
                size: "60%",
                background: "#18191f"
            },
            track: {
                background: "#21253f",
                dropShadow: {
                    enabled: !0,
                    top: 2,
                    left: 0,
                    blur: 4,
                    opacity: .15
                }
            },
            dataLabels: {
                name: {
                    offsetY: -5,
                    color: "#fff",
                    fontSize: "14px"
                },
                value: {
                    offsetY: 5,
                    color: "#fff",
                    fontSize: "14px",
                    show: !0
                }
            }
        }
    },
    fill: {
        type: "gradient",
        gradient: {
            shade: "dark",
            type: "vertical",
            gradientToColors: ["#fbb624"],
            stops: [0, 100]
        }
    },
    stroke: {
        lineCap: "round"
    },
    labels: ["Progress"]
};
(chart = new ApexCharts(document.querySelector("#d1-radialBarMap"), options)).render(), $("#world-map-markers").vectorMap({
    map: "world_mill_en",
    scaleColors: ["#eff0f1", "#eff0f1"],
    normalizeFunction: "polynomial",
    hoverOpacity: .7,
    hoverColor: !1,
    regionStyle: {
        initial: {
            fill: "#4c5486"
        }
    },
    markerStyle: {
        initial: {
            stroke: "transparent"
        },
        hover: {
            stroke: "rgba(112, 112, 112, 0.30)"
        }
    },
    backgroundColor: "transparent",
    markers: [{
        latLng: [37.09024, -95.712891],
        name: "USA",
        style: {
            fill: "#f93b7a"
        }
    }, {
        latLng: [71.70694, -42.604301],
        name: "Greenland",
        style: {
            fill: "#f0961f"
        }
    }, {
        latLng: [-21.943369, 123.102198],
        name: "Australia",
        style: {
            fill: "#5766da"
        }
    }],
    series: {
        regions: [{
            values: {
                AU: "#c4c9f2",
                US: "#fdcede",
                GL: "#fae1be"
            },
            attribute: "fill"
        }]
    }
});
var chart;
options = {
    chart: {
        height: 250,
        type: "donut"
    },
    series: [15, 85],
    stroke: {
        colors: void 0
    },
    legend: {
        show: !0,
        position: "bottom",
        horizontalAlign: "center",
        verticalAlign: "middle",
        floating: !1,
        fontSize: "14px",
        offsetX: 0,
        offsetY: -13
    },
    labels: ["Possibility","Risk"],
    colors: ["#00dd9f","#f65f4d"],
    responsive: [{
        breakpoint: 600,
        options: {
            chart: {
                height: 240
            },
            legend: {
                show: !1
            }
        }
    }]
};
(chart = new ApexCharts(document.querySelector("#d1_payment"), options)).render();