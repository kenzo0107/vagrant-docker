var current_circuit_id;
$(function(){

  function displayCircuitBlock(circuit_id) {
    var blocksCircuit = $('#block-stations');
    blocksCircuit.hide();
    $('.block-circuit').each(function(k,v){
      var cid = $(this).data('circuit_id');
      if (circuit_id == cid) {
        $(this).show();
      } else {
        $(this).hide();
      }
      blocksCircuit.show();

      var position = blocksCircuit.offset().top;
      var speed = 500; // ミリ秒で記述
      $('body,html').animate({scrollTop:position}, speed, 'swing');
    });
  }

  $('#select_circuit').on('click', function() {

    var t = $('li.circuit.is-selected');
    var circuit_id = t.data('circuit_id');

    if (current_circuit_id == circuit_id) {
      console.log('You select same circuit_id.');
      displayCircuitBlock(circuit_id);
      return;
    }

    var postData = {}
    postData["circuit_id"] = circuit_id;
    $('.blocks-circuit').hide();

    var request = window.superagent;
    request
      .post('/circuit')
      .type('form')
      .set('Content-Type', 'application/json; charset=utf-8')
      .send(postData)
      .end(function(err, res){
        if (res.ok) {
          if (circuit_id == res.body['circuit_id']) {
            console.log("success");
            current_circuit_id = circuit_id;
            displayCircuitBlock(circuit_id);
            return false;
          }
        } else {
          console.log('error occured');
        }
      });
  });
});
