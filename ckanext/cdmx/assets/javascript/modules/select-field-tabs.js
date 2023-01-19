ckan.module('select-field-tabs', function (jQuery) {
  return {
    initialize () {
      this.panelsContainer = document.getElementById(this.options.panels)
      this.panels = Array.prototype.map.call(this.panelsContainer.children, el => el)
      this._showPanel(this.panels, this.options.open)
      
      this.el.on('change', jQuery.proxy(this._onChange, this))
    },
    _onChange: function (event) {
      this._showPanel(this.panels, event.target.value)
    },
    _showPanel: function (panels, value) {
      panels.forEach(function (panel) {
        if (panel.id === value) {
          panel.style.display = 'block'
        } else {
          panel.style.display = 'none'
        }
      })
    }
  }
})