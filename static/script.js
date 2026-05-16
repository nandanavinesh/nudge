async function submitLog() {
    const data = {
        date: document.getElementById('date').value,
        social_media: parseFloat(document.getElementById('social_media').value),
        productive_screen: parseFloat(document.getElementById('productive_screen').value),
        tasks_completed: parseInt(document.getElementById('tasks_completed').value),
        sleep_hours: parseFloat(document.getElementById('sleep_hours').value),
        mood: parseInt(document.getElementById('mood').value)
    }

    const response = await fetch('/api/log', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })

    const result = await response.json()
    document.getElementById('message').textContent = '✅ Day saved!'
}