document.addEventListener('DOMContentLoaded', function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const result = data.result;
            const topicsDistribution = data.topics_distribution;

            const intensityData = result.map(item => item.intensity);
            const likelihoodData = result.map(item => item.likelihood);
            const labels = result.map(item => item.year);

            const intensityCtx = document.getElementById('intensityChart').getContext('2d');
            const likelihoodCtx = document.getElementById('likelihoodChart').getContext('2d');
            const topicsPieCtx = document.getElementById('topicsPieChart').getContext('2d');

            const intensityChart = new Chart(intensityCtx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Intensity',
                        data: intensityData,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            const likelihoodChart = new Chart(likelihoodCtx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Likelihood',
                        data: likelihoodData,
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            const topicLabels = Object.keys(topicsDistribution);
            const topicData = Object.values(topicsDistribution);

            const topicsPieChart = new Chart(topicsPieCtx, {
                type: 'pie',
                data: {
                    labels: topicLabels,
                    datasets: [{
                        data: topicData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
