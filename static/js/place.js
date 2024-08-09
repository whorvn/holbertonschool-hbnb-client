// Function to extract place ID from the URL query parameters
function getPlaceIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    //console.log(window.location.search)
    return urlParams.get('place_id');
}

// Function to get a cookie by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Function to check authentication and fetch place details if authenticated
function checkAuthentication() {
    const token = getCookie('token');
    const addReviewSection = document.getElementById('add-review');
    
    if (!token) {
        addReviewSection.style.display = 'none';
    } else {
        addReviewSection.style.display = 'block';
        const placeId = getPlaceIdFromURL();
        if (placeId) {
            fetchPlaceDetails(token, placeId);
            fetchReviews(token, placeId); 
        } else {
            console.error('Place ID not found in URL');
        }
    }
    return token;
}

// Function to fetch reviews from the server
async function fetchReviews(token, placeId) {
    try {
        const response = await fetch(`/places/${placeId}/reviews`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch reviews');
        }
        
        const reviews = await response.json();
        displayReviews(reviews);
    } catch (error) {
        console.error(error);
    }
}


// Function to populate reviews in the HTML
function displayReviews(reviews) {
    const reviewsSection = document.getElementById('reviews');

    // Clear existing content
    reviewsSection.innerHTML = '';

    if (reviews.length === 0) {
        reviewsSection.innerHTML = '<p>No reviews yet.</p>';
        return;
    }

    // Create and append review elements
    reviews.forEach(review => {
        const reviewElement = document.createElement('div');
        reviewElement.classList.add('review');

        const reviewText = document.createElement('p');
        reviewText.textContent = review.comment;
        reviewElement.appendChild(reviewText);

        reviewsSection.appendChild(reviewElement);
    });
}











// Function to fetch place details from the server
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`/places/${placeId}/reviews`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch place details');
        }
        console.log("fetch succes")
        const place = await response.json();
        displayPlaceDetails(place);
    } catch (error) {
        console.error(error);
    }
}

// Function to populate place details in the HTML
function displayPlaceDetails(place) {

    
    const placeDetailsSection = document.getElementById('place-details');

    // Clear existing content
    placeDetailsSection.innerHTML = '';

    // Create and append elements
    const nameElement = document.createElement('h1');
    nameElement.textContent = place.name;
    placeDetailsSection.appendChild(nameElement);

    const descriptionElement = document.createElement('p');
    descriptionElement.textContent = place.description;
    placeDetailsSection.appendChild(descriptionElement);

    const locationElement = document.createElement('p');
    locationElement.textContent = `Country: ${place.country}`;
    placeDetailsSection.appendChild(locationElement);

}
  
async function submitReview(token, placeId, reviewText) {
    try {
        const response = await fetch(`/places/${placeId}/reviews`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ comment: reviewText })
        });

        if (!response.ok) {
            throw new Error('Failed to submit review');
        }
        alert('Review submitted successfully!');
        document.getElementById('review-form').reset();
    } catch (error) {
        alert('Failed to submit review');
    }
}








document.addEventListener('DOMContentLoaded', () => {
    const token = checkAuthentication();
    
    
    const placeId = getPlaceIdFromURL();
/*
    if (placeId) {
        fetchPlaceDetails(token, placeId);
    } else {
        console.error('Place ID not found in URL');
    }
*/
    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewText = document.getElementById('review-text').value;
            await submitReview(token, placeId, reviewText);
        });
    }



});








