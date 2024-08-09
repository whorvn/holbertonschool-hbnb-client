
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
    populateCountryFilter();
});

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

async function fetchPlaces(token) {
    try {
        const response = await fetch('http://127.0.0.1:5000/places', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
            
        });

        if (response.ok) {
            const data = await response.json();
            displayPlaces(data);
            console.log('fetch worked')
            console.log(data)
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
            <h3 class="mb">${place.name}</h3>
            <p class="mb">Price per night: $${place.price_per_night}</p>
            <p class="mb"><strong>Location:</strong> ${place.city},${place.country}</p>
            <a class="view-details"  href="place?place_id=${place.id}" >View Details</a>
        `;
        placesList.appendChild(placeElement);
    });
}




/*
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
        }0
    });
}
*/





async function populateCountryFilter() {
    const countryFilter = document.getElementById('country-filter');
    
    // Fetch country names
    const countries = await fetchCountryNames(); // Wait for the promise to resolve
    
    if (!countries) {
        console.error('No countries fetched');
        return; // Exit if there is an error fetching countries
    }
    
    // Clear any existing options
    countryFilter.innerHTML = '';


    const allOption = document.createElement('option');
    allOption.value = ''; // Set the value to an empty string for "All"
    allOption.textContent = 'All'; // Set the text content to "All"
    countryFilter.appendChild(allOption);

    
    // Add each country as an option
    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countryFilter.appendChild(option);
    });

    // Add event listener for filtering
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

const apiUrl = 'http://127.0.0.1:5000/countries'; // Replace with your actual API URL

async function fetchCountryNames() {
    try {
        // Fetch data from the API
        const response = await fetch(apiUrl);

        // Check if the response is okay (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON data from the response
        const data = await response.json();

        // Initialize an empty array to store country names
        const countryNames = [];

        // Iterate over the data array and extract country names
        for (let i = 0; i < data.length; i++) {
            countryNames.push(data[i].name);
        }

        // Log or use the array of country names
        console.log('Country Names:', countryNames);
        
        return countryNames;

    } catch (error) {
        // Handle errors
        console.error('Error fetching country names:', error);
    }
}



