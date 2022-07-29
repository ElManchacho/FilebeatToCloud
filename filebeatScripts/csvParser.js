function process(event) {
    event.Put("filebeatScriptMessage", event.Get())
    return event
}
