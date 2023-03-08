window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {

        $.ajax({
            url: "{% url 'edit' %}",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });

        event.preventDefault();
    });

}