var darkMode = localStorage.getItem("darkmode");

if(darkMode) {
    $("#darkModeSwitch").prop("checked", true);
    $("body").toggleClass("body-dark");
    $("nav").toggleClass("navbar-dark bg-dark");
    $("footer").toggleClass("footer-dark");
    $("a").toggleClass("anchor-styling-dark");
}

$("#darkModeSwitch").change(function() {
    darkMode = !darkMode;
    if (darkMode) localStorage.setItem("darkmode", "1");
    else localStorage.removeItem("darkmode");

    $("body").toggleClass("body-dark", darkMode);
    $("nav").toggleClass("navbar-dark bg-dark", darkMode);
    $("footer").toggleClass("footer-dark", darkMode);
    $("a").toggleClass("anchor-styling-dark", darkMode);
});