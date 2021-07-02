function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
        }
    }

});

function order_shoe(pk) {
    $.ajax({
        url: orderUrl,
        type: 'post',
        data: {
            shoe_id: pk
        },
        cache: false,
        success: function(response) {
            window.location.href = summaryUrl + response['id'];
        },
        error: function(xhr, status, error) {
            alert(xhr.responseText);
        }
    });
}