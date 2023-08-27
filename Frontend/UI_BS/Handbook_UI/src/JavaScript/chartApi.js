const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: ['數學', '編程', '創新', '解題', '邏輯'],
      datasets: [{
        label: '個人能力',
        data: [1, 3, 3, 3, 5],
        borderWidth: 1
      }]
    },
    options: {
        maintainAspectRatio: false, // Set to true to maintain aspect ratio, false to adjust independently
        scales: {
            y: {
                beginAtZero: true
        }
      }
    }
  });