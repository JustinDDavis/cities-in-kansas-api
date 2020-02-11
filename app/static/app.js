
(function(){
    const url = '/api/ks/cities';

    fetch(url)
        .then((resp) => resp.json())
        .then(function(results) {
            var html_results = '';
            html_results += `<div class="row">`;

            results["data"].forEach((city)=>{

                html_results += `<div class="col-sm-6 col-md-4 col-lg-3 card">`;
                html_results += `   <div class="card-body">`;
                html_results += `       <h2>${city.name}</h2>`;
                html_results += `       <p>County: ${city.county}</p>`;
                html_results += `       <p>Population: ${city.population}</p>`;
                html_results += `       <p>Region: ${city.region}</p>`;
                html_results += `       <p><a href="${city.wikipedia}">Wikipedia</a></p>`;
                html_results += `       <img src="${city.image_url}" />`;
                html_results += `   </div>`;
                html_results += `</div>`;
            });
            html_results += `</div>`;

            document.getElementById("results").innerHTML = html_results;

        }).catch(function(error) {
            // If there is any error you will catch them here
            document.getElementById("results").innerHTML = `Error retrieving results : ${error}`;
        });


})()