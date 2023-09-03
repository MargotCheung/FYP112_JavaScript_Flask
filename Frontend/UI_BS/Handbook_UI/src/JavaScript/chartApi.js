const ctx1 = document.getElementById('myChart1');
const myChart1 = new Chart(ctx1, {
    type: 'radar',
    data: {
        labels: ['數學', '編程', '創新', '解題', '邏輯'],
        datasets: [{
            label: '個人能力',
            data: [1, 3, 3, 3, 5],
            borderWidth: 2
        }]
    },
    options: {
        scale: {
            ticks: {
                beginAtZero: true, // 刻度从0开始
                stepSize: 1,       // 刻度间距
                max: 5,            // 刻度的最大值
                min: 0             // 刻度的最小值
            }
        }
    }
});









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













// const myChart2  = new Chart(ctx2, {
//     type: 'radar',
//     data: {
//         labels: [
//             'Eating',
//             'Drinking',
//             'Sleeping',
//             'Designing',
//             'Coding',
//             'Cycling',
//             'Running'
//           ],
//           datasets: [{
//             label: 'My First Dataset',
//             data: [65, 59, 90, 81, 56, 55, 40],
//             fill: true,
//             backgroundColor: 'rgba(255, 99, 132, 0.2)',
//             borderColor: 'rgb(255, 99, 132)',
//             pointBackgroundColor: 'rgb(255, 99, 132)',
//             pointBorderColor: '#fff',
//             pointHoverBackgroundColor: '#fff',
//             pointHoverBorderColor: 'rgb(255, 99, 132)'
//           }, {
//             label: 'My Second Dataset',
//             data: [28, 48, 40, 19, 96, 27, 100],
//             fill: true,
//             backgroundColor: 'rgba(54, 162, 235, 0.2)',
//             borderColor: 'rgb(54, 162, 235)',
//             pointBackgroundColor: 'rgb(54, 162, 235)',
//             pointBorderColor: '#fff',
//             pointHoverBackgroundColor: '#fff',
//             pointHoverBorderColor: 'rgb(54, 162, 235)'
//           }]

//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });



