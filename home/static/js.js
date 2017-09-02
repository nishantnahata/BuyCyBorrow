    $(function() {
      $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var tegrat = $(this.hash);
          tegrat = tegrat.length ? tegrat : $('[name=' + this.hash.slice(1) +']');
          if (tegrat.length) {
            $('html, body').animate({
              scrollTop: tegrat.offset().top
            }, 1000);
            return false;
          }
        }
      });
    });
