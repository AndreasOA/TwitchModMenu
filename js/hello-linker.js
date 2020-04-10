function link_hello() {
    var python = require("python-shell")
    var path = require("path")
    
    var account_name = document.getElementById("autoview-input-email").value
    document.getElementById("autoview-input-email").value = ""

    var account_password = document.getElementById("autoview-input-password").value
    document.getElementById("autoview-input-password").value = ""

    var options = {
        scriptPath : path.join(__dirname, '../python/'),
        args : [account_name, account_password]
    }
    var hello = new python("hello.py", options)

    hello.on('message', function(message) { 
        alert(message);
    })
}