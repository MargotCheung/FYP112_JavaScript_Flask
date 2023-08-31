// -------------------------- myChart1 -------------------------------- //
const ctx1 = document.getElementById('myChart1');
const myChart1  = new Chart(ctx1, {
    type: 'radar',
    data: {
        labels: ['數學', '編程', '創新', '解題', '邏輯'],
          datasets: [{            
            label: '目前能力',
            // data: [65, 90, 81, 56, 40],
            data: [2, 3, 4, 2, 4],
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




// -------------------------- myChart2 -------------------------------- //
const ctx2 = document.getElementById('myChart2');
const myChart2  = new Chart(ctx2, {
    type: 'radar',
    data: {
        labels: ['數學', '編程', '創新', '解題', '邏輯'],
          datasets: [{
            label: '目前能力',
            // data: [28, 48, 19, 96, 27],
            data: [2, 3, 4, 2, 4],
            //data: [3, 3, 4, 4, 4],
            fill: true,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            pointBackgroundColor: 'rgb(255, 99, 132)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgb(255, 99, 132)'
          }, {            
            label: '原始能力',
            // data: [65, 90, 81, 56, 40],
            data: [1, 2, 4, 3, 2],
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





