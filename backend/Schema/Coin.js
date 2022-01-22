const mongoose = require('mongoose')
const { Schema } = mongoose

const CoinSchema = new Schema({
    _id: String,
    symbol: String,
    name: String
})

module.exports = mongoose.model('Coin', CoinSchema);