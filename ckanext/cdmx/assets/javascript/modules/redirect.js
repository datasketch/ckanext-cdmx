ckan.module('redirect', function (jQuery) {
  return {
    options: {
      href: ''
    },
    initialize: function() {
      console.log(this)
      console.log(this.options.href);
      console.log('******');
    }
  }
})