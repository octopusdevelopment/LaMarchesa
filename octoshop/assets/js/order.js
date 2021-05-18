// Variables
let wilaya_price = 0
// Input
const url_input = document.querySelector('#checkoutForm')
const commune_input = document.querySelector('#id_commune')
const delivery_price_container = document.querySelector('#delivery_price')
const order_total_container = document.querySelector('#order_total')

// Functions

const change_commune = function(e) {
    if(e.target.id == 'id_wilaya') {
        const url_value = url_input.getAttribute('data-communes-url')
        
        const wilaya_id = e.target.value
        const url = `${window.location.origin}${url_value}?wilaya=${wilaya_id}`
        const language = window.location.pathname.split('/')[1]
    fetch(url, {
        headers : { 
            'Accept': 'application/json'
           } 
    } )
    .then(response => {
        return response.json()
    })
    .then(data => {
        const communes = data
        console.log(communes)
        commune_input.innerHTML = `<option class="option" value='' selected>---------</option>`

        for(i = 0; i< communes.length; i++) {
            
            let commune = communes[i]
            commune_input.innerHTML += `
            <option value="${commune.id}">${commune.translations[language].name}</option>
            `
        }
        change_wilaya(wilaya_id)

    })
    .catch(err => {
        // empty communes and price
        console.log(err)
        commune_input.innerHTML =  `<option class="option" value='' selected>---------</option>`
        delivery_price_container.innerHTML = ``
        wilaya_price = 0
        change_price()
    })

}

const change_wilaya = function(wilaya_id){
    const url = `${window.location.origin}/orders/fetch/load-wilaya/?wilaya=${wilaya_id}`

    fetch(url, {
        headers : { 
            'Accept': 'application/json'
           } 
    } )
    .then(response => response.json())
    .then(data => {
        const wilaya = JSON.parse(data)[0]
        wilaya_price = wilaya.fields.cout
      
        delivery_price_container.innerHTML = ` ${wilaya_price} DA`
        change_price()
    })
    .catch(err => {
        delivery_price_container.innerHTML = ``
        wilaya_price = 0
        change_price()
    })

    }
    
}

const change_price = function() {
    
    const total_without_delivery = parseFloat(order_total_container.getAttribute('data-order-total'))
    const total_price = parseFloat(total_without_delivery)+ parseFloat(wilaya_price)
    order_total_container.innerHTML = `${total_price.toFixed(2)} DA`
}
window.addEventListener('DOMContentLoaded', function() {
    order_total_container.innerHTML = `${document.querySelector('#order_total').getAttribute('data-order-total')} DA`
    url_input.addEventListener('change', change_commune)
});