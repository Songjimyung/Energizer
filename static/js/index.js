function submit() {
    let name = $('#name').val()
    let reply = $('#reply').val()
        }
    $.ajax({
        type: "POST",
        url: "/reply",
        data: {
            name_give: name,
            reply_give: reply
        },
        success: function (response) {

                alert(response["msg"]);
                window.location.reload();
            }
        }
    });
}