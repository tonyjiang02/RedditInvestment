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


  function verify(){
    


  }