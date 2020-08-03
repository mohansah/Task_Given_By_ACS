var express=require("express"); 
var bodyParser=require("body-parser");
  
const mongoose = require('mongoose'); 
mongoose.connect('mongodb://localhost:27017/gfg'); 

var db=mongoose.connection; 
db.on('error', console.log.bind(console, "connection error")); 
db.once('open', function(callback){ 
    console.log("connection succeeded"); 
}) 
  
var app=express() 
  
  
app.use(bodyParser.json()); 
app.use(express.static('public')); 
app.use(bodyParser.urlencoded({ extended: true })); 
  
app.post('/samp', function(req,res){
    var vid = Array()
    var vname = Array()
    var vphone = Array()
    var vemail = Array()
    var vaddress = Array()

    var iid = Array()
    var iname = Array()
    var idescription = Array()
    var iprice = Array()

    vid[0] = req.body.vid1; vid[1] = req.body.vid2; vid[2] = req.body.vid3; vid[3] = req.body.vid4;
    vname[0] = req.body.vname1; vname[1] = req.body.vname2; vname[2] = req.body.vname3; vname[3] = req.body.vname4;
    vphone[0] = req.body.vphone1; vphone[1] = req.body.vphone2; vphone[2] = req.body.vphone3; vphone[3] = req.body.vphone4;
    vemail[0] = req.body.vemail1; vemail[1] = req.body.vemail2; vemail[2] = req.body.vemail3; vemail[3] = req.body.vemail4;
    vaddress[0] = req.body.vaddress1; vaddress[1] = req.body.vaddress2; vaddress[2] = req.body.vaddress3; vaddress[3] = req.body.vaddress4;

    iid[0] = req.body.iid1; iid[1] = req.body.iid2; iid[2] = req.body.iid3; iid[3] = req.body.iid4;
    iname[0] = req.body.iname1; iname[1] = req.body.iname2; iname[2] = req.body.iname3; iname[3] = req.body.iname4;
    idescription[0] = req.body.idescription1; idescription[1] = req.body.idescription2; idescription[2] = req.body.idescription3; idescription[3] = req.body.idescription4;
    iprice[0] = req.body.iprice1; iprice[1] = req.body.iprice2; iprice[2] = req.body.iprice3; iprice[3] = req.body.iprice4;


    var i, j;
    var vStatus = false, iStatus = false;
    for(i=0;i<4;i++){
        if(vid[i].length > 0 && vname[i].length > 0){
            vStatus = true;
            var arr = Array(), k = 0;
            for(j=0;j<4;j++){
                    iid[j] = "" + iid[j]
                    iname[j] = "" + iname[j]
                    if(iid[j].length > 0 && iname[j].length > 0){
                        iStatus = true;
                        arr[k] = {"_id":iid[j], "Name":iname[j], "Description": idescription[j], "Price": iprice[j]}
                        k++;
                    }
                }
            
            if(vStatus && iStatus){ 
                var data = {
                    "_id": vid[i],
                    "Full Name":vname[i],
                    "Phone":vphone[i],
                    "Email":vemail[i],
                    "Address":vaddress[i],
                    "Item" : arr
                }
                db.collection('details').insertOne(data,function(err, collection){ 
                    if (err)
                    console.log("Vender ID already exit, try with another ID");
                    else 
                        console.log("Record inserted Successfully");       
                });
            }
            else
                console.log("Filled at least one section from both page");
        }
    }
    
 
          
    return res.redirect('index.html'); 
}) 


app.get('/',function(req,res){ 
    res.set({ 'Access-control-Allow-Origin': '*' }); 
    return res.redirect('index.html'); 
}).listen(3000)