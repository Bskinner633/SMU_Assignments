
var tableData = data;
var tbody = d3.select("tbody");
tableData.forEach((sheepleReport) => {
    var row = tbody.append("tr");
    Object.values(sheepleReport).forEach((value) => {
        var cell = row.append("td");
        cell.text(value);
    });
});


var button = d3.select("#filter-btn");
button.on("click", function () {
    
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
    let inputCity = d3.select("#city").property("value");
    let inputState = d3.select("#state").property("value");
    let inputCountry = d3.select("#country").property("value");
    let inputShape = d3.select("#shape").property("value");
    
    // Remove all table row in the body
    d3.select("tbody").selectAll("tr").remove();
    
    // Filter table
    let filterData = tableData;
    if (inputValue !== "") {
        filterData = tableData.filter(ufoRow => ufoRow.datetime === inputValue);
    };

    if (inputCity !== "") {
        filterData = filterData.filter(ufoRow => ufoRow.city === inputCity);
    }
    if (inputState !== "") {
        filterData = filterData.filter(ufoRow => ufoRow.state === inputState);
    }
    if (inputCountry !== "") {
        filterData = filterData.filter(ufoRow => ufoRow.country === inputCountry);
    }
    if (inputShape !== "") {
        filterData = filterData.filter(ufoRow => ufoRow.shape === inputShape);
    }
    filterData.forEach((sheepleReport) => {
        var row = tbody.append("tr");
        Object.values(sheepleReport).forEach(value => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
});