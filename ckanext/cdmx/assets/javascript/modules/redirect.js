ckan.module('redirect', function (jQuery) {
  return {
    options: {
      href: ''
    },
    initialize: function() {
      this.el.on('change', jQuery.proxy(this._onChange, this))
    },
    _onChange: function(event) {
      event.preventDefault()
      const origin = window.location.origin
      const href = this.options.href
      window.location = origin + href
    }
  }
})