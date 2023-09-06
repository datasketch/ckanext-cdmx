ckan.module('change-iframe', function (jQuery) {
    return {
        initialize() {
            const root = this.el.get(0)

            this.resources = root.querySelector('#resourceDropdown')
            this.frame = root.querySelector('#resourceFrame')

            this.resources.addEventListener('change', () => {
               this.frame.src = `https://datasketch.shinyapps.io/cdmxApp/?ckanConf=${this.resources.value}` 
            })

        }
    }
})