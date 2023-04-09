(function($) {
    'use strict';
  
    function handlePrintShortcut(e) {
      // Listen for ctrl + p key combination
      if (e.keyCode === 80 && e.ctrlKey) {
        // Trigger print dialog
        window.print();
      }
    }
  
    $(function() {
      // Add print button to admin header
      var $printBtn = $('<a>', {
        'class': 'button',
        'href': '#',
        'text': 'Print'
      }).on('click', function(e) {
        e.preventDefault();
        window.print();
      });
      $('.model-header').append($printBtn);
  
      // Listen for ctrl + p key combination
      $(document).on('keydown', handlePrintShortcut);
    });
  
  })(django.jQuery);
  