// // -------------------------- myChart1 -------------------------------- //
// const ctx1 = document.getElementById('myChart1');
// const myChart1 = new Chart(ctx1, {
//     type: 'radar',
//     data: {
//         labels: ['數學', '編程', '創新', '解題', '邏輯'],
//         datasets: [{
//             label: '個人能力',
//             // data: [1, 3, 3, 3, 5],
//             //data: [1, 2, 4, 3, 2],
//             data: [0, 0, 0, 0, 0],
//             borderWidth: 2
//         }]
//     },
//     options: {
//         maintainAspectRatio: false, // Set to true to maintain aspect ratio, false to adjust independently
//         scales: {
//             y: {
//                 beginAtZero: true
//             },
//             min: 0.0,
//             max: 5.0,
//             ticks: {
//                 // forces step size to be 50 units
//                 stepSize: 1.0
//             }
//         }
//     }
// });


const ctx1 = document.getElementById('myChart1');
const myChart1 = new Chart(ctx1, {
    type: 'radar',
    data: {
        labels: ['數學', '編程', '創新', '解題', '邏輯'],
        datasets: [{
            label: '個人能力',
            data: [0, 0, 0, 0, 0],
            borderWidth: 2
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: false, // Let the y-axis not always begin at 0 initially
                suggestedMax: 5,
                ticks: {
                    stepSize: 1
                }
            }
        },
        plugins: {
            afterLayout: ctx1 => {
                // Manually set y-axis minimum to 0 if all data values are 0
                const datasets = myChart1.data.datasets;
                const allZero = datasets.every(dataset => dataset.data.every(value => value === 0));
                if (allZero) {
                    myChart1.scales.y.options.min = 0;
                }
            }
        }
    }
});









// -------------------------- myChart2 -------------------------------- //
const ctx2 = document.getElementById('myChart2');
const myChart2  = new Chart(ctx2, {
    type: 'radar',
    data: {
        labels: ['數學', '編程', '創新', '解題', '邏輯'],
          datasets: [{
            label: 'My First Dataset',
            // data: [65, 90, 81, 56, 40],
            data: [1, 2, 4, 3, 2],
            fill: true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)'
          }, {
            label: 'My Second Dataset',
            // data: [28, 48, 19, 96, 27],
            data: [3, 3, 3, 4, 4],
            fill: true,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            pointBackgroundColor: 'rgb(54, 162, 235)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(54, 162, 235)'
          }]

    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            },
            min: 0.0,
            max: 5.0,
            ticks: {
                // forces step size to be 50 units
                stepSize: 1.0
            }
        }
    }
});





