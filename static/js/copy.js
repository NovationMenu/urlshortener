function copyFunction() {
    var copyText = document.getElementById("clip");
    console.log(copyText)
    copyText.select();
    console.log(copyText.value)
    document.execCommand("copy");
    alert("Copied the text: " + copyText.value);}