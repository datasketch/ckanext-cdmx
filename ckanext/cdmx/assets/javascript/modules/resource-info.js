ckan.module('resource-info', function (jQuery) {
  return {
    initialize: function() {
      const isMobileBreakpoint = window.matchMedia('only screen and (max-width: 767px)').matches
      if ((this.options.dashboard && this.options.dashboard === "none") || (isMobileBreakpoint && this.options.dashboard !== "pdf")) {
        this.el.removeClass('d-none')
      }
    }
  }
})