ckan.module('pdf', function (jQuery) {
  return {
    initialize: function() {
      const doc = this.options.doc
      console.log(doc);
    }
  }
})