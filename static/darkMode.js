var darkMode = localStorage.getItem("darkmode"); /* Sets localStorage value for the dark mode switch */

if(darkMode) {
    /* Sets classes for darker colours, and changes text colour on the darker backgrounds */
    $("#darkModeSwitch").prop("checked", true);
    $("body").toggleClass("body-dark");
    $("nav").toggleClass("navbar-dark bg-dark");
    $("table").toggleClass("table-colour");
    $("td a").toggleClass("table-anchors");
    $("footer").toggleClass("footer-dark");
    $("#footer").children().toggleClass("anchor-styling-dark");
}

$("#darkModeSwitch").change(function() {
    darkMode = !darkMode;
    /* 
        Switches the classes on and shows the switch as checked
        if darkMode is read from the localStorage function,
        and unchecks the switch and removes the classes if
        darkMode is removed
    */
    if (darkMode) localStorage.setItem("darkmode", "1");
    else localStorage.removeItem("darkmode");
    
    $("body").toggleClass("body-dark", darkMode);
    $("nav").toggleClass("navbar-dark bg-dark", darkMode);
    $("table").toggleClass("table-colour");
    $("td a").toggleClass("table-anchors");
    $("footer").toggleClass("footer-dark", darkMode);
    $("#footer").children().toggleClass("anchor-styling-dark", darkMode);
});