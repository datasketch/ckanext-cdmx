ckan.module('change-iframe', function (jQuery) {
    return {
        initialize() {
            const root = this.el.get(0)

            this.resources = root.querySelector('#resourceDropdown')
            this.frame = root.querySelector('#resourceFrame')
            this.button = root.querySelector('#resourceButton')

            this.resources.addEventListener('change', () => {
                const package = this.resources.value.split(";")[1]
                const resource = this.resources.value.split(";")[0]

                this.button.style.cssText = 'visibility: visible'
                this.frame.style.cssText ='height: 600px'

                this.button.addEventListener('click', () => {
                    window.open(this.options.url + `/dataset/` + package)
                })

                if (this.options.url == 'https://datos-prueba.cdmx.gob.mx') {
                    this.frame.src = `https://services.datasketch.co/cdmxApp/?ckanConf=${resource}`
                } else {
                    this.frame.src = `https://visdatos.cdmx.gob.mx/app_direct_i/cdmx/_/?ckanConf=${resource}`
                }
            })
        }
    }
})