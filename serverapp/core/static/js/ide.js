window.onunload = endTerminal();

function start_terminal(data) {
    //fill this iframe with whats given in the variable data
    console.log("Trying to start up server with the ip of: " + data);
    $term_iframe = $('#tiframe');
    $term_iframe.attr({
        //TEST IP.
        'src': 'http://' + data,
        //DEPLOYED IP
        // WTAMU IP here.
    });
}

function reloadTerminal() {
    // reloads terminal
    stopTerminal();
    loadTerminal();
}

function endTerminal() {
    return $.ajax({
        method: 'POST',
        url: "endTerminal",
        data: {},
        success: function(data) {
            $('#tiframe').attr({
                src: ''
            });
        },
        error: function(data) {}
    });
}

function beginTerminal() {
    console.log("Beginning terminal.");
    return $.ajax({
        method: 'POST',
        url: "makeTerminal",
        data: {},
        success: function(data) {
            delay(function() {
                start_terminal(data);
            }, 2000);
        },
        error: function(data) {}
    });
}




$('#closeTerminal').bind('click', function(e) {
    e.preventDefault();
    new $.Zebra_Dialog('This will close the terminal. Reload the page if you want to restart the terminal. <br><br><strong>Continue? </strong>', {
        'type': 'question',
        'title': 'End Terminal',
        'buttons': [
            {caption: 'Yes', callback: function() {
                endTerminal();
            }}, 
            {
                caption: 'No', callback: function() {

                }
            },
        ]
    });
});

$('#reloadTerminal').bind('click', function(e) {
    e.preventDefault();
    new $.Zebra_Dialog('This will close the reload the terminal. <br> Anything in the environment will be lost. <br><br><strong>Continue ?</strong>', {
    'type':     'question',
    'title':    'Reload terminal',
    'buttons':  [
                    {caption: 'Yes', callback: function() {
                        reloadTerminal();
                    }},
                    {caption: 'No', callback: function() {
                    }},
                ]
});
});

var delay = (function() {
    //allows a delay of ms seconds
    var timer = 0;
    return function(callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();


$(function(){

    $.ajaxSetup({
          headers: { "X-CSRFToken": getCookie("csrftoken") }
      });

    $('#submitbutton').on('click', function(){

      // for each form in your html you can process then and save the information in an object 
      var form_data = {}
      var input_id = 1;
      var input_value = editor.getValue();
      form_data[input_id] = input_value;
          console.log(form_data);

      $.ajax({
        type: "POST",
        url: "/ide/",
        data : {code: editor.getValue()},
        success : function(result) {
          console.log("Success!");
        }
      });
    });
});

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

 $(document).ready(function() {
     console.log("I loaded.");
     beginTerminal();
 });