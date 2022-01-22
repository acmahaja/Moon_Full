const getCoinList = require("./getData");

const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/moonful");
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
  console.log("Database connect");
});

const CoinSchema = require("../Schema/Coin");

async function updateCoinsList() {
  let { data } = await getCoinList();
  data.forEach(async (coin) => {
    const checkCoin = await CoinSchema.findById(coin.id);
    if (checkCoin === null) {
      const c = new CoinSchema({
        _id: coin.id,
        symbol: coin.symbol,
        name: coin.name,
      });
      c.save();
      console.log(c);
    }
  });
}

module.exports = updateCoinsList;
