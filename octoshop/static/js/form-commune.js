$(document).ready(function(){

    $("#id_wilaya").change(function () {
        console.log('INSIDE')
        var url = $("#checkoutForm").attr("data-communes-url");  // get the url of the `load_cities` view
        
        var wilayaId = $(this).val();  // get the selected country ID from the HTML input
        
        if (wilayaId == ''){
        $("#id_commune").empty();
        }
    
        console.log('WILAYA', wilayaId)

        $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
            'wilaya': wilayaId       // add the country id to the GET parameters
        },
        
        success: function (data) { 
             // `data` is the return of the `load_cities` view function

           // $("#id_commune").html(data);  // replace the contents of the city input with the data that came from the server        
        }              
        }); 
    });

    const change_delivery_price = function () {

    }

    $("select#id_wilaya").change(function(){

    var selectedWilaya = $(this).children('option:selected').text();
    var coutLivraison = $('#id_livraison span')
    var totalPrice = $('#id_total_price span')
    var livraisonAlger = '400'
    var livraisonAutre = '600'

    // var numLivraisonAlger = parseInt(livraisonAlger)
   
    //    if (selectedWilaya== 'Alger')  {
    //     coutLivraison.html(livraisonAlger)
    //    } else {
    //     coutLivraison.html(livraisonAutre)
    //    }


    // prix = parseInt($('#id_price span').text());
    // livraison = parseInt(coutLivraison.text());
    // quantity = parseInt($('#id_quantity span').text())
    // console.log(prix);
    // console.log(quantity);
    // console.log(livraison);

    });


    // $('#id_quantity').change(function(){
    //     var prix = parseInt($('#id_price span').text());
    //     var livraison = parseInt($('#id_livraison span').text())
    //     var quantity = $('#id_quantity');
    //     var quantityVal = parseInt(quantity.val());
    //     var coutProduits = prix * quantityVal
    //     var ttc = coutProduits + livraison 
    //     var totalPrice = $('#id_total_price span')
    //     totalPrice.html(ttc)

    // });
    // $('#id_wilaya').change(function(){
    //     var prix = parseInt($('#id_price span').text());
    //     var livraison = parseInt($('#id_livraison span').text())
    //     var quantity = $('#id_quantity');
    //     var quantityVal = parseInt(quantity.val());
    //     var coutProduits = prix * quantityVal
    //     var ttc = coutProduits + livraison 
    //     var totalPrice = $('#id_total_price span')
    //     totalPrice.html(ttc)

    // });

});
