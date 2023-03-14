function join() {
    let id = $('#id').val()
    let pw = $('#pw').val()
    if (id =='' || pw==''){
        alert("아이디와 비밀번호를 모두 입력해주세요")
    }else{
        $.ajax({
            type: "POST",
            url: "/createUserData",
            data: {'id_give': id, 'pw_give': pw},
            success: function (response) {
                if(response["result"]=='success'){
                    alert(response["msg"])
                window.close
                }
                else{
                    alert(response["msg"])
                }
            }
        });
    }
}
