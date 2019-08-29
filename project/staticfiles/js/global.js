$( document ).ready(function() {

  $('textarea').autogrow({onInitialize: true});


  //Cloner for infinite input lists
  $(".circle--clone--list").on("click", ".circle--clone--add", function(){
    var parent = $(this).parent("li");
    // find the ul element
    var copy = parent.clone();

    // find the total value of form
    var totalFormVal =  parseInt(parent.parent().find('input[name$=TOTAL_FORMS]').attr('value'));

    // find all input and text-area.  change name and id to format PREFIX-{TOTALFORM}-FIELD_VAR_NAME
    copy.find('input, textarea').each(function() {
        var name = $(this).attr('name').replace('-' + (totalFormVal-1) + '-', '-' + totalFormVal + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').attr('checked');
    });

    parent.after(copy);

    // update totalFormVal to avoid "data tempered" error
    parent.parent().find('input[name$=TOTAL_FORMS]').attr({'value': totalFormVal+1});
    copy.find("input, textarea, select").val("");
    copy.find("*:first-child").focus();
  });

  $(".circle--clone--list").on("click", "li:not(:only-child) .circle--clone--remove", function(){
    var parent = $(this).parent("li");
    parent.find('input:checkbox').prop('checked', true);
    parent.hide();
  });

  // Adds class to selected item
  $(".circle--pill--list a").click(function() {
    $(".circle--pill--list a").removeClass("selected");
    $(this).addClass("selected");
  });

  // Adds class to parent div of select menu
  $(".circle--select select").focus(function(){
   $(this).parent().addClass("focus");
   }).blur(function(){
     $(this).parent().removeClass("focus");
   });

  // Clickable table row
  $(".clickable-row").click(function() {
      var link = $(this).data("href");
      var target = $(this).data("target");

      if ($(this).attr("data-target")) {
        window.open(link, target);
      }
      else {
        window.open(link, "_self");
      }
  });

  // Custom File Inputs
  var input = $(".circle--input--file");
  var text = input.data("text");
  var state = input.data("state");
  input.wrap(function() {
    return "<a class='button " + state + "'>" + text + "</div>";
  });




});