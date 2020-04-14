setTimeout(function(){
    let p = document.getElementById('content');
    p.removeAttribute("hidden");
}, 7030);


function changeCategoryName(name) {
    document.getElementById("idleview-input-streamer").placeholder = name;
}

