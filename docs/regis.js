firebase.initializeApp({
    apiKey: 'AIzaSyCKqrBhHXZoUdznArZzgLvvpRSGHc6nDok',
    authDomain: 'hshacks-investment.firebaseapp.com',
    projectId: 'hshacks-investment'
  });
  
  // Initialize Cloud Firestore through Firebase
  var db = firebase.firestore();
  
  // Disable deprecated features
  db.settings({
    timestampsInSnapshots: true
  });

var errors, index, loggedIn;

index = 0;

function Store(){
    var output = document.getElementById("output");
    var user ={};
    user.ign = document.getElementById("ign").value;
    user.email = document.getElementById("email").value;
    user.pass= ""+document.getElementById("pass").value;
    user.cpass = ""+document.getElementById("cpass").value;
    errors="";
    var success = true;

    //scan database for matching usernames

    var emailSuccess= validateEmail(user.email);
    if(emailSuccess==false){
        success = false;
        errors+= " Invalid Email! "
    }

    if(user.pass.localeCompare(user.cpass)!=0){
        errors += " Passwords Do Not Match! "
        success = false;
    }
    output.innerHTML = errors;

    if(success){
        db.collection("users").add({
            ign: user.ign,
            email: user.email,
            pass: user.pass,
            id: index,
            balance: 10000
            })
            .then(function(docRef) {
                console.log("Document written with ID: ", docRef.id);
            })
            .catch(function(error) {
                console.error("Error adding document: ", error);
            });
        index+=1;
    } 
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}