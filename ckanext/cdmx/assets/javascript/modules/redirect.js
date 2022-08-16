ckan.module('redirect', function (jQuery) {
  return {
    options: {
      href: ''
    },
    initialize: function() {
      this.el.on('change', jQuery.proxy(this._onChange, this))
    },
    _onChange: function(event) {
      const origin = window.location.origin
      const href = this.options.href
      event.preventDefault()
      console.log(origin + href);
    }
  }
})