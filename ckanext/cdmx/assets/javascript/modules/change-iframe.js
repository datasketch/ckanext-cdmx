ckan.module('change-iframe', function (jQuery) {
    return {
        initialize() {
            const root = this.el.get(0)

            console.log(this.options.url);

            this.resources = root.querySelector('#resourceDropdown')
            this.frame = root.querySelector('#resourceFrame')

            this.resources.addEventListener('change', () => {
                if (this.options.url == 'https://datos-prueba.cdmx.gob.mx'){
                    this.frame.src = `https://services.datasketch.co/cdmxApp/?ckanConf=${this.resources.value}` 
                } else {
                    this.frame.src = `https://visdatos.cdmx.gob.mx/app_direct_i/cdmx/_/?ckanConf=${this.resources.value}`
                }               
            })
        }
    }
})