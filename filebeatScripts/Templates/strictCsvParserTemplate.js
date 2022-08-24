function process(event) {

    var message = event.Get("message");

    if(message.charAt(message.length-1) == ";" || message.charAt(message.length-1) == ",")
    {
        message = message.slice(0,-1);
    }

    var slicedText = message.split(';');

    var headersConfig = [];

    var logCols = slicedText.length

    var headers = []

    headersConfig.forEach(function(config, indexConfig){
        if(config.length == logCols){
            headers = config
        }
    })

    var headersLength = headers.length

    var sortedHeaders = []

    for (var index = 0; index < headersLength; index++) { // Prepare tampon headers array
        sortedHeaders.push('')
    }

    headers.forEach(function(header, indexHeader) { // Tampon array takes headers with their position as index
        sortedHeaders[header['position']] = header
    });

    headers = sortedHeaders // Tampon into used headers array

    headersLength = headers.length // Update value

    for (var index = 0; index < headersLength; index++) { // Remove empty headers from input array
        if(headers[index]['title'] == '' || headers[index]['title'] == ' '){
            // TODO : decrement all the next header's position
            for (var indexHeaderToDelete = index + 1; indexHeaderToDelete < headersLength; indexHeaderToDelete++){ // start just after the index of the header to delete until the end of header's list
                var updatedHeader = {
                    'title':headers[indexHeaderToDelete]["title"],
                    'position':headers[indexHeaderToDelete]["position"]-1
                }
                headers[indexHeaderToDelete] = updatedHeader
            }
            headers.splice(index, 1)
            headersLength -= 1
        }
    }

    event.Put('test.logsColumns', logCols)

    event.Put('test.headersLength', headersLength)

    if (logCols != headersLength) // Add empty headers for missing one in input (compare with logs columns)
    {
        for (var index = 0; index < logCols - headersLength ; index++){
            headers.push({
                'title':'<emptyHeaderName'+String(index)+'>',
                'position':(logCols - headersLength) + index 
            })
        }
        
    }

    slicedText.forEach(function(field, indexField) {
        event.Put('parsed.'+headers[indexField]['title'], field);
    });

    event.Put('script.message', 'Filebeat script successfully executed')
    event.Put('script.executionState', 'OK')
    
    return event;
}