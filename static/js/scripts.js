document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded and parsed');
    
    checkAuthentication();
    //populateCountryFilter();
    
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        console.log('Login form found');
        loginForm.addEventListener('submit', async (event) => {
            console.log('Form submitted');
            event.preventDefault(); // Prevent the default form submission

            // Get the values from the form fields
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            console.log('Email:', email);
            console.log('Password:', password);

            try {
                // Send a POST request to the login endpoint
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email, password })
                });

                // Check if the response status is OK (status code 200-299)
                if (response.ok) {
                    const data = await response.json();
                    const expirationMinutes = 1;
                    
                    // Calculate the expiration date
                    const now = new Date();
                    now.setMinutes(now.getMinutes() + expirationMinutes);
                    const expires = now.toUTCString();
                    
                    // Store the JWT token in a cookie
                    document.cookie = `token=${data.access_token}; expires=${expires}; path=/`;
                    
                    // Redirect to the main page
                    window.location.href = '/';
                } else {
                    // Attempt to parse error response as JSON
                    let errorText = 'Login failed. Please check your credentials.';
                    try {
                        const errorData = await response.json();
                        errorText = errorData.msg || errorText;
                    } catch (jsonError) {
                        console.error('Error parsing JSON response:', jsonError);
                    }
                    alert(errorText);
                }
            } catch (error) {
                console.error('An error occurred:', error);
                alert('An unexpected error occurred. Please try again.');
            }
        });
    } else {
        console.log('Login form not found');
    }
});





function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
/*
async function fetchPlaces(token) {
    try {
        const response = await fetch('https://api.example.com/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            displayPlaces(data);
        } else {
            console.error('Failed to fetch places');
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(place => {
        const placeElement = document.createElement('div');
        placeElement.className = 'place';
        placeElement.dataset.country = place.country;
        placeElement.innerHTML = `
            <h3>${place.name}</h3>
            <p>${place.description}</p>
            <p><strong>Location:</strong> ${place.location}</p>
        `;
        placesList.appendChild(placeElement);
    });
}

function populateCountryFilter() {
    const countryFilter = document.getElementById('country-filter');
    // Assuming we have a predefined list of countries. This can also be fetched dynamically.
    const countries = ['USA', 'Canada', 'UK', 'Australia'];

    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countryFilter.appendChild(option);
    });

    countryFilter.addEventListener('change', (event) => {
        const selectedCountry = event.target.value;
        filterPlacesByCountry(selectedCountry);
    });
}

function filterPlacesByCountry(country) {
    const places = document.querySelectorAll('.place');
    places.forEach(place => {
        if (country === '' || place.dataset.country === country) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    });
}

*/