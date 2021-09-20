window.onload = function () {
    setIframeHeight(document.getElementById('admin-frame'));
};

function setIframeHeight(iframe) {
    if (iframe) {
        var iframeWin = iframe.contentWindow || iframe.contentDocument.parentWindow;
        if (iframeWin.document.body) {
            iframe.height = iframeWin.document.documentElement.scrollHeight || iframeWin.document.body.scrollHeight;
        }
    }
};

$(document).ready(function () {
    $("dd>a").click(function (e) {
      e.preventDefault();
      $("#admin-frame").attr("src", $(this).attr("href"));
    });
});

$(document).ready(function () {
    $("li>a").click(function (e) {
        e.preventDefault();
        $("#admin-frame").attr("src", $(this).attr("href"));
    });
});
