async function getWeather() {
    const city = document.getElementById('cityInput').value;
    if (!city) {
        alert("Please enter a city name.");
        return;
    }

    const res = await fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ city })
    });

    const data = await res.json();

    const resultsDiv = document.getElementById('weatherResults');
    resultsDiv.innerHTML = '';

    if (data.error) {
        resultsDiv.innerHTML = `<p class='text-danger'>${data.error}</p>`;
        return;
    }

    const current = data.current;
    const forecast = data.forecast;

    resultsDiv.innerHTML += `
        <h3>${current.name}, ${current.sys.country}</h3>
        <p><strong>Temperature:</strong> ${current.main.temp} °C</p>
        <p><strong>Condition:</strong> ${current.weather[0].description}</p>
        <p><strong>Humidity:</strong> ${current.main.humidity}%</p>
        <p><strong>Wind Speed:</strong> ${current.wind.speed} m/s</p>
        <h5>5-Day Forecast:</h5>
        <ul>
            ${forecast.map(f => `<li>${new Date(f.dt_txt).toLocaleString()}: ${f.main.temp} °C, ${f.weather[0].main}</li>`).join('')}
        </ul>
    `;
}

