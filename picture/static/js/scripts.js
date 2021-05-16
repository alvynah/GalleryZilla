function copyFunction() {
    var copyText = document.getElementById("pic_url");
    copyText.focus();
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
    document.execCommand("copy");
    alert("Copied the text: " + copyText.value);

}