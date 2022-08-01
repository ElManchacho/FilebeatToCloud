function process(event) {

    var message = event.Get("message");
    
    event.Put("eventMessage", message);

    var slicedText = message.split(';');

    slicedText.forEach(function(field, index) {
        event.Put('parsed.'+index, field);
    });
    
    return event;
}