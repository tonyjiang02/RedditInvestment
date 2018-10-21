
var config = {
    apiKey: "AIzaSyCKqrBhHXZoUdznArZzgLvvpRSGHc6nDok",
    authDomain: "hshacks-investment.firebaseapp.com",
    databaseURL: "https://hshacks-investment.firebaseio.com",
    projectId: "hshacks-investment",
    storageBucket: "hshacks-investment.appspot.com",
    messagingSenderId: "334189266034"
};
// Initialize Firebase
// TODO: Replace with your project's customized code snippet
firebase.initializeApp(config);
var db = firebase.firestore();
// Initialize Cloud Firestore through Firebase
getDoc(function(data){
    addData(data)
})
function addData(data) {
    var div = document.getElementById("most_common")
    var stock = data["stock"]
    var mentions = data["mentions"]
    var sentiment = data["sentiment"]
    for(var i = 0; i<stock.length; i++){
        var element = document.createElement('div')
        element.className="row"

        var col1 = document.createElement('div')
        col1.className="col-md-4"
        element.appendChild(col1)
        col1.innerHTML=i+1+". "+stock[i]

        var col2 = document.createElement('div')
        col2.className="col-md-4"
        element.appendChild(col2)
        col2.innerHTML=mentions[i]

        var col3 = document.createElement('div')
        col3.className="col-md-4"
        element.appendChild(col3)
        col3.innerHTML=sentiment[i]

        div.appendChild(element)
    }
}

function getDoc(callback){
    var docRef = db.collection("stocks").doc("10-20");
    data = {}
    docRef.get().then(function(doc) {
        if (doc.exists) {
            console.log(doc.data)
            data = doc.data()
            callback(data)
        } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
        }
    }).catch(function(error) {
        console.log("Error getting document:", error);
    });
}
