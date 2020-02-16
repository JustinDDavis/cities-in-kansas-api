
let api_data_results = {};

function write_city_tables(api_data_results){
    var html_results = '';
            html_results += `<div class="row">`;
            api_data_results["data"].forEach((city)=>{

                html_results += `<div class="col-sm-6 col-md-4 col-lg-3 card">`;
                html_results += `   <div class="card-body">`;
                html_results += `       <h2>${city.name}</h2>`;
                html_results += `       <p>County: ${city.county}</p>`;
                html_results += `       <p>Population: ${city.population}</p>`;
                html_results += `       <p>Region: ${city.region}</p>`;
                html_results += `       <p><a href="${city.wikipedia}">Wikipedia</a></p>`;
                html_results += `       <img style="width:100%;" src="${city.image_url}" />`;
                html_results += `   </div>`;
                html_results += `</div>`;
            });
            html_results += `</div>`;

            document.getElementById("results").innerHTML = html_results;
}
var sort_name_toggle = false;
function sort_name(){
    document.getElementById("results").innerHTML = "";
    console.log("sort by name");
    sort_name_toggle = !sort_name_toggle;

    api_data_results["data"].sort((city1, city2)=>{
        if(sort_name_toggle){
            if (city1.name > city2.name) {
                return 1;
            }
            if (city2.name > city1.name) {
                return -1;
            }
            return 0;
        }else{
            if (city2.name > city1.name) {
                return 1;
            }
            if (city1.name > city2.name) {
                return -1;
            }
            return 0;
        }
    });
    write_city_tables(api_data_results);
}

var sort_population_toggle = false;
function sort_population(){
    console.log("sort by population");
    sort_population_toggle = !sort_population_toggle;

    api_data_results["data"].sort((city1, city2)=>{
        if(sort_population_toggle){
            return parseInt(city1.population) - parseInt(city2.population);
        }else{
            return parseInt(city2.population) - parseInt(city1.population);
        }

    });
    write_city_tables(api_data_results);
}

var sort_county_toggle = false;
function sort_county(){
    console.log("sort by county");
    sort_county_toggle = !sort_county_toggle;

    api_data_results["data"].sort((city1, city2)=>{
        if(sort_county_toggle){
            if (city1.county > city2.county) {
                return 1;
            }
            if (city2.county > city1.county) {
                return -1;
            }
            return 0;
        }else{
            if (city2.county > city1.county) {
                return 1;
            }
            if (city1.county > city2.county) {
                return -1;
            }
            return 0;
        }

    });
    write_city_tables(api_data_results);
}

function search_data(){
    //search-box
    const searchString = document.getElementById('search-box').value;
    console.log(searchString);

    try{
         const data = api_data_results["data"].filter((city)=>{
            if(city.name.toLowerCase().includes(searchString.toLowerCase())){
                return true
            }else{
                return false
            }
        });
        write_city_tables({
            'data':data
        });
    }catch(err){
        console.log(err);
    }



}


(function(){
    const url = '/api/ks/cities';
    fetch(url)
        .then((resp) => resp.json())
        .then(function(results) {
            api_data_results = results;

            write_city_tables(api_data_results);

        }).catch(function(error) {
            // If there is any error you will catch them here
            document.getElementById("results").innerHTML = `Error retrieving results : ${error}`;
        });

    document.getElementById('search-box').addEventListener("input", search_data);
    document.getElementById('city-name-sort').addEventListener("click", sort_name);
    document.getElementById('population-sort').addEventListener("click", sort_population);
    document.getElementById('county-sort').addEventListener("click", sort_county);


})()