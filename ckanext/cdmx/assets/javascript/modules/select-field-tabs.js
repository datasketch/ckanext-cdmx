ckan.module('select-field-tabs', function (jQuery) {
  return {
    initialize () {
      this.panelsContainer = document.getElementById(this.options.panels)
      this.panels = Array.prototype.map.call(this.panelsContainer.children, el => el)
      this._extendAttrs.call(this)
      this._showPanel.call(this)
      
      this.el.on('change', jQuery.proxy(this._onChange, this))
    },
    _onChange: function (event) {
      this._showPanel.call(this, event.target.value)
    },
    _showPanel: function (value) {
      const option = value || this.options.open
      this.panels.forEach((panel) => {
        if (panel.id === option) {
          this._enable(panel)
        } else {
          this._disable(panel)
        }
      })
    },
    _extendAttrs: function () {
      this.panels.forEach(function (panel) {
        const elements = panel.querySelectorAll('[name]')
        elements.forEach(function (element) {
          element.dataset.name = element.name
        })
      })
    },
    _enable: function (panel) {
      panel.style.display = 'block'
      const elements = panel.querySelectorAll('[data-name]')
      elements.forEach(function (element) {
        element.setAttribute('name', element.dataset.name)
      })
    },
    _disable: function (panel) {
      panel.style.display = 'none'
      const elements = panel.querySelectorAll('[data-name]')
      elements.forEach(function (element) {
        element.removeAttribute('name')
      })
    }
   }
})