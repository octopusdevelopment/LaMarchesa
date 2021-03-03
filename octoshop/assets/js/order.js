window.addEventListener('DOMContentLoaded', load_listeners);

// Variables

// Input
const wilaya_input = document.querySelector('#id_wilaya')
const url_input = document.querySelector('checkoutForm')

const load_listeners = function() {
    url_input.addEventListener('change', change_commune)
} 
// Functions
const change_commune = function() {
    const url_value = url_input.getAttribute('data-communes-url')
    console.log(url_value)
}