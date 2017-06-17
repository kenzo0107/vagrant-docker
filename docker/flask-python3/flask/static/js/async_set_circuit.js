$(function(){
  $('#select_circuit').on('click', function() {
    var t = $('li.circuit.is-selected');
    var circuit_id = t.data('circuit_id');
    console.log("circuit_id:"+circuit_id);

    var postData = {}
    postData["circuit_id"] = circuit_id;

    var request = window.superagent;
    request
      .post('/circuit')
      .type('form')
      .send(postData)
      .end(function(err, res){
        if (res.ok) {
          if (circuit_id == res.body['circuit_id']) {
            console.log("success");
          }
        } else {
          console.log('error occured');
        }
      });
  });
});
