$(document).ready(function(){
    var form = $('#form_buy_product');
    console.log(form);

    form.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number').val();
        var submit_button = $('#submit_button');
        var product_id = submit_button.data("product_id");
        var product_name = submit_button.data("product_name");
        var product_price= submit_button.data("product_price");
        console.log(number, product_id, product_name, product_price);
    })
});