let heart = $('.some-info svg')
console.log(heart)

function sendRequest(id){
    $.ajax({
        url: `/like/${id}`,
        method: "GET",
        dataType: "json",
        success: function (data) {
            // $("#content").html(data);
            console.log(data);
            $(heart).toggleClass("liked");
        }
    });
}

sendRequest();


$(heart).click(function (e) { 
    e.preventDefault();
    let id = $(this).data("id")
    sendRequest(id);
});