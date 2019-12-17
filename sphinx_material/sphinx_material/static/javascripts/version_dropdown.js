function add_version_dropdown(json_loc, target_loc, text) {

    var dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";
    var button = document.createElement("button");
    button.className = "dropdownbutton";
    button.innerHTML = text;
    var content = document.createElement("div");
    content.className = "dropdown-content";
    dropdown.appendChild(button);
    dropdown.appendChild(content);

    $.getJSON(json_loc).done(function(versions) {
        for (var i = 0; i < versions.length; i++) {
            if (versions[i].substring(0, 1) == "v") {
                versions[i] = [versions[i], versions[i].substring(1)];
            } else {
                versions[i] = [versions[i], versions[i]];
            };
        };
        for (var i = 0; i < versions.length; i++) {
            var a = document.createElement("a");
            a.innerHTML = versions[i][1];
            a.href = target_loc + versions[i][0] + "/index.html";
            a.title = versions[i][1];
            content.appendChild(a);
        };
    }).fail(function() {
        button.innerHTML = "Other Versions Not Found";
    });
    $(".navheader").append(dropdown);
};
