function add_version_dropdown(json_loc, target_loc, text) {

    var dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";
    var button = document.createElement("button");
    button.className = "dropdownbutton";
    var content = document.createElement("div");
    content.className = "dropdown-content md-hero";
    dropdown.appendChild(button);
    dropdown.appendChild(content);

    fetch(json_loc)
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(versions => {
        for (const key in versions) {
            if (Object.prototype.hasOwnProperty.call(versions, key)) {
                console.log(key, versions[key]);
                const a = document.createElement("a");
                a.innerHTML = key;
                a.title = key;
                a.href = target_loc + versions[key];
                content.appendChild(a);
            }
        }

        // Success equivalent of `.done()`
        button.innerHTML = text;
    })
    .catch(() => {
        // Equivalent of `.fail()`
        button.innerHTML = "Other Versions Not Found";
    })
    .finally(() => {
        // Equivalent of `.always()`
        document.querySelector(".navheader").appendChild(dropdown);
    });
};
