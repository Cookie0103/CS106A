/**
 * File: code.js
 * -------------
 * This is a javascript file which has the logic for the front-end of the chat client.
 * JavaScript is a language a lot like python! 
 */

// JavaScript has constants just like python!
const HOST = "http://localhost:8000/"

// JavaScript has classes just like python
class ChatClient {

	// this is the same as def __init__():
	constructor() {
		// these are instance variables
		// note that self is the JavaScript equivalent of this
		this.msgIndex = 0
		this.username = ""
	}

	// these are each methods in the ChatClient class. Where is the def? Its implied
	getMessageHtml(msg) {
		// javascript allows for back-tick strings
		return `<li class="list-group-item"> > ${msg}</li>`
	}

	// this performs a server request! Wow.
	loadMessages() {
		var url = HOST + "getMsgs"
		var params = { 
			index: "" + this.msgIndex
		}
		var callbackFn = (e) => this.renderMessages(e)
	 	$.get(url, params , callbackFn);
	}

	// when the server request comes back, this method is called
	renderMessages(msgString){
		// ! is JavaScript for "not"
		if(!msgString) return
		// eval is the JavaScript equivalent of json.loads
		var messages = eval(msgString)
		// thats the same as "for i in range(messages.length)"
		for (var i = 0; i < messages.length; i++) {
			var msg = messages[i]
			var msgHtml = this.getMessageHtml(msg);
			$("#messages").append(msgHtml);
		};
		this.msgIndex += messages.length
	}

	// a nice method which simply calls loadMessages
	refreshMessages() {
		this.loadMessages();
	}

	// send the text which is in the "#msgInput" text-input field
	sendMessage() {
		var url = HOST + "newMsg"
		var params = {
			'msg': $("#msgInput").val(),
			'user': this.username
		}
		var callbackFn = () => this.loadMessages()
	  	$.get( url, params , callbackFn)
	  	// clear whats in the msgInput text-input field
		$("#msgInput").val('')
	}

	// handler for when the log in button is clicked
	logIn() {
		// extract the user name. Save it in the instance var
		this.username = $("#usernameInput").val()
		// hide the modal!
		$("#loginModal").modal('hide')
	}
}

// this is the same as the main function!
$( document ).ready(function() {
	// make a new instance of the ChatClienct class
	client = new ChatClient()
	// show the username modal
	$("#loginModal").modal()
	// load any messages from the server
	client.loadMessages();
	// when the user hits enter on msgInput, call sendMessage
	$('#msgInput').keyup(function(e){
		if(e.keyCode == 13){
			client.sendMessage()
		}
	});
});

