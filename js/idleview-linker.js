function link_hello() {
    var python = require("python-shell")
    var path = require("path")

    var account_name = document.getElementById("idleview-input-email").value
    //document.getElementById("idleview-input-email").value = ""

    var account_password = document.getElementById("idleview-input-email-password").value
    //document.getElementById("idleview-input-email-password").value = ""

    var twitch_username = document.getElementById("idleview-input-twitch-username").value
    //document.getElementById("idleview-input-twitch-username").value = ""

    var twitch_password = document.getElementById("idleview-input-twitch-password").value
    //document.getElementById("idleview-input-twitch-password").value = ""

    var twitch_viewgenre = document.getElementById("idleview-input-streamer").value
    //document.getElementById("idleview-input-streamer").value = ""


    var options = {
        scriptPath : path.join(__dirname, '../../python/'),
        args : [twitch_username, twitch_password, twitch_viewgenre, account_name, account_password]
    }
    var hello = new python("TwitchChatbot.py", options)

    hello.on('message', function(message) { 
        alert(message);
    })
}