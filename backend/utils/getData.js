const axios = require('axios')

async function getData(){
    try {
        let result = await axios.get("https://api.coingecko.com/api/v3/coins/list")
        return result
        
    } catch (error) {
        console.log("error");
    }
}

module.exports = getData;