$(document).ready(function(){
    var form = $('#form_buy_product');
    console.log(form);

    form.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number').val();
        var submit_button = $('#submit_button');
        var product_id = submit_button.data("product_id");
        var product_name = submit_button.data("product_name");
        var product_price = submit_button.data("product_price");
        var sum = number * product_price;
        console.log(number, product_id, product_name, product_price);

        $('.miniCartTable table tbody').append('<tr class="miniCartProduct">' +
            '<td style="width:20%" class="miniCartProductThumb">' +
            '<div><a href="product-details.html"><img src="images\\product\\3.jpeg" alt="img"> </a></div>' +
            '</td>' +
            '<td style="width:40%">' +
            '<div class="miniCartDescription">' +
            '<h4><a href="product-details.html"> '+product_name+' </a></h4>' +
            '<div class="price"><span> '+product_price+' тенге</span></div>' +
            '</div>' +
            '</td>' +
            '<td style="width:10%" class="miniCartQuantity"><a> X '+number+' </a></td>' +
            '<td style="width:15%" class="miniCartSubtotal"><span> '+sum+' тенге</span></td>' +
            '<td style="width:5%" class="delete"><a> x </a></td>' +
            '</tr>');
    })
});

$(document).on('click', '.delete', function () {
    $(this).closest('tr').remove();
});