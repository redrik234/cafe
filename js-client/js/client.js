$(window).on('load', function() {

    var disableStart = function() {
        $('#start-record').prop('disabled', true);
        $('#stop-record').prop('disabled', false);
    }

    var disableStop = function() {
        $('#start-record').prop('disabled', false);
        $('#stop-record').prop('disabled', true);
    }

    var startRecord = function() {
        $('#start-record').on('click', function() {
            disableStart();

            rec.record();
            // interval = setInterval(function() {
            //     rec.exportWAV(function(blob) {
            //         rec.clear();
            //         ws.send(blob);
            //     });
            // }, 1000);
        });
    }

    var stopRecord = function() {
        $('#stop-record').on('click', function() {
            disableStop();
            rec.stop();
            rec.exportWAV(function(blob) {
                rec.clear();
                ws.send(blob);
            });
            //clearInterval(interval);
        });
    }

    var callbackAudio = function(stream) {
        var context = new AudioContext();
        var mediaStreamSource = context.createMediaStreamSource(stream);
        rec = new Recorder(mediaStreamSource);
    }

    var callbackAudioError = function () {
        console.warn("Error getting audio stream from getUserMedia");
    }

    disableStop();
    startRecord();
    stopRecord();

    navigator.webkitGetUserMedia({audio: true}, callbackAudio, callbackAudioError);

    var ws = new WebSocket("ws://localhost:8081");
    ws.onopen = function() {
        console.log("Open websocket(js)");
    };

    ws.onmessage = function(e) {
        var jsonResponse = $.parseJSON(e.data);
        console.log(jsonResponse);
        if (jsonResponse.hypotheses.length > 0) {
            var bestMatch = jsonResponse.hypotheses[0].utterance;
            console.log(bestMatch);
        }
    };
});