function submit() {
    let name = $('#name').val()
    let reply = $('#reply').val()
        if (reply.trim() =='' || name.trim()=='') {
        alert("내용과 작성자이름을 입력해주세요")
        return;
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
)}

function show_reply() {
    let a = $('#name').text()
    $.ajax({
        type: "GET",
        url: "/replys",
        data: {},
        success: function (response) {

            let replys = response['all_reply']

            for (let i = 0; i < replys.length; i++) {
                let name = replys[i]['name']
                let reply = replys[i]['reply']
                let date = replys[i]['date']

                let year = new Date(date).getFullYear().toString()
                let month = new Date(date).getUTCMonth() + 1
                let day = new Date(date).getUTCDate()
                let strdate = `${year}.${month}.${day}`

                let temp_html = ` 
            <tr>
                <td>${name}</td>
                <td>${reply}</td>
                <td>${strdate}</td>
            </tr>`
                $('#replys').append(temp_html)
            }
        }
    })
}