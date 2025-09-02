let temperateForest =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/Temperate_Forest');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let tropicalRainforest =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/Tropical_Rainforest');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let desert =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/desert');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let grassland =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/grassland');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let taiga =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/taiga');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let tundra =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/tundra');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let chaparral =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/chaparral');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}

let ocean =   async function(event){
    let response =  await axios.get('https://en.wikipedia.org/api/rest_v1/page/summary/ocean');
    console.log(response.data.extract)
    alert(response.data.extract)
    return false
}
