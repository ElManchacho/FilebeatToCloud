function process(event) {

    var message = event.Get("message");

    if(message.charAt(message.length-1) == ";" || message.charAt(message.length-1) == ",")
    {
        message = message.slice(0,-1);
    }

    var slicedText = message.split(';');

    slicedText.forEach(function(field, index) {
        event.Put('parsed.'+index, field);
    });
    
    return event;
}