var util = require('util'),
    twitter = require('twitter');
var twit = new twitter({
    consumer_key: //add yours,
    consumer_secret: //add yours,
    access_token_key: //add yours,
    access_token_secret: //add yours
});

twit.stream('statuses/filter', {track: ['good day']}, function(stream) {
	console.log('This is working');
    stream.on('data', function(data) {
        console.log(util.inspect(data.text));
    });
});
