/* Fire Valaidate */
$(document).ready(function(){
    $("#validation").validate({
        rules: {
            tweettext: {
                required: true
            }
        },
        messages: {
            tweettext: "Required Field"
        }
    });
});