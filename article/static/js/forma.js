/**
 * Created by a.nazarov on 09.08.2017.
 */

$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    contactform();
});