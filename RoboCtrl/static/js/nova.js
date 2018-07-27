$(document).ready(function() {
  $("#main_feed").on("click", function(event) {
    var width = this.clientWidth;
    var height = this.clientHeight;
    var x = event.pageX - this.offsetLeft;
    var y = event.pageY - this.offsetTop;
    var percent_x_calc = ((event.pageX - this.offsetLeft) / this.clientWidth) * 100;
    var percent_y_calc = ((event.pageY - this.offsetTop) / this.clientHeight) * 100;
    var percent_x = percent_x_calc.toFixed(2);
    var percent_y = percent_y_calc.toFixed(2);
      $.getJSON('/click_pos', {
        x: x,
        y: y,
        width: width,
        height: height,
        percent_x: percent_x,
        percent_y: percent_y
      }, console.log(x + ", " + y + ", " + width + ", " + height + ", " + percent_x + ", " + percent_y));
  });
});
