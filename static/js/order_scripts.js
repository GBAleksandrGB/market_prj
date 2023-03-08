window.onload = function () {
    var _nights, _price, orderitem_num, delta_nights, orderitem_nights, delta_cost;
    var nights_arr = [];
    var price_arr = [];
    var TOTAL_FORMS = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    var order_total_nights = parseInt($('.order_total_nights').text()) || 0;
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (var i=0; i < TOTAL_FORMS; i++) {
        _nights = parseInt($('input[name="orderitems-' + i + '-nights"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        nights_arr[i] = _nights;

        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }

    if (!order_total_nights) {

        for (var i=0; i < TOTAL_FORMS; i++) {
            order_total_nights += nights_arr[i];
            order_total_cost += nights_arr[i] * price_arr[i];
        }

        $('.order_total_nights').html(order_total_nights.toString());
        $('.order_total_cost').html(Number(order_total_cost.toFixed(2)).toString());
    }

    $('.order_form').on('click', 'input[type="number"]', function () {
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-nights', ''));

        if (price_arr[orderitem_num]) {
            orderitem_nights = parseInt(target.value);
            delta_nights = orderitem_nights - nights_arr[orderitem_num];
            nights_arr[orderitem_num] = orderitem_nights;
            orderSummaryUpdate(price_arr[orderitem_num], delta_nights);
        }
    });

    $('.order_form').on('click', 'input[type="checkbox"]', function () {
        var target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));

        if (target.checked) {
            delta_nights = -nights_arr[orderitem_num];
        } else {
            delta_nights = nights_arr[orderitem_num];
        }

        orderSummaryUpdate(price_arr[orderitem_num], delta_nights);
    });

    function orderSummaryUpdate(orderitem_price, delta_nights) {
        delta_cost = orderitem_price * delta_nights;
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_nights = order_total_nights + delta_nights;
        $('.order_total_cost').html(order_total_cost.toString());
        $('.order_total_nights').html(order_total_nights.toString());
    }

}