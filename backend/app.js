const express = require('express')
const app = express()

const axios = require('axios')
const cron = require('node-cron')

const mongoose = require('mongoose')
mongoose.connect('mongodb://localhost:27017/moonful')
const db = mongoose.connection
db.on("error", console.error.bind(console, "connection error:"))
db.once("open", ()=>{
    console.log("Database connect");
})


app.get('/', (req,res)=> {
    res.send("Moonful!")
})


cron.schedule('1 * * * * *', () => { console.log("Task is running every minute " + new Date()) });


app.listen(3000 , (req,res)=>{
    console.log('Listening on port 3000')
})