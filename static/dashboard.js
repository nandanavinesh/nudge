async function loadDashboard() {
    const response = await fetch('/api/analysis')
    const data = await response.json()

    document.getElementById('avg-score').textContent = data.average_score + ' / 100'
    document.getElementById('prediction').textContent = data.prediction + ' / 100'

    const dates = data.chart_data.dates
    const scores = data.chart_data.productivity_scores
    const social = data.chart_data.social_media
    const productive = data.chart_data.productive_screen

    new Chart(document.getElementById('productivityChart'), {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Productivity Score',
                data: scores,
                borderColor: '#534AB7',
                backgroundColor: 'rgba(83, 74, 183, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { min: 0, max: 100 } }
        }
    })

    new Chart(document.getElementById('screenTimeChart'), {
        type: 'bar',
        data: {
            labels: dates,
            datasets: [
                {
                    label: 'Social Media',
                    data: social,
                    backgroundColor: '#F09595'
                },
                {
                    label: 'Productive',
                    data: productive,
                    backgroundColor: '#5DCAA5'
                }
            ]
        },
        options: {
            responsive: true,
            scales: { x: { stacked: true }, y: { stacked: true } }
        }
    })

    const insightsList = document.getElementById('insights-list')
    data.insights.forEach(insight => {
        const div = document.createElement('div')
        div.className = 'insight-item'
        div.textContent = insight
        insightsList.appendChild(div)
    })
}

loadDashboard()