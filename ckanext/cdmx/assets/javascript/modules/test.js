ckan.module('example_theme_popover', function ($) {
    return {
      initialize: function () {
        console.log("I've been initialized for element: ", this.el);
      }
    };
  });