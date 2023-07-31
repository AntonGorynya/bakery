function loadJson(elementID) {
  return JSON.parse(document.getElementById(elementID).textContent);
}
var cakeNames = loadJson('cake_names');
var cakeCosts = loadJson('cake_costs');
var cake = loadJson('cake');

console.log(cake);
if (cake != null){
    var cakeLevels = JSON.stringify(cake.levels_number) || 0;
    var cakeForm =  JSON.stringify(cake.form) || 0;
    var cakeTopping = JSON.stringify(cake.topping) || 0;
    var cakeBerries = JSON.stringify(cake.berry) || 0;
    var cakeDecor =  JSON.stringify(cake.decor) || 0;
    var cakeComments = cake.name;
}
else {
    var cakeLevels = 0;
    var cakeForm =   0;
    var cakeTopping =  0;
    var cakeBerries =  0;
    var cakeDecor =  0;
    var cakeComments = '';

}


Vue.createApp({
    name: "App",
    components: {
        VForm: VeeValidate.Form,
        VField: VeeValidate.Field,
        ErrorMessage: VeeValidate.ErrorMessage,
    },
    data() {
        return {
            schema1: {
                lvls: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' количество уровней';
                },
                form: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' форму торта';
                },
                topping: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' топпинг';
                }
            },
            schema2: {
                name: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' имя';
                },
                phone: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' телефон';
                },
                name_format: (value) => {
                    const regex = /^[a-zA-Zа-яА-Я]+$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат имени нарушен';
                    }
                    return true;
                },
                email_format: (value) => {
                    const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат почты нарушен';
                    }
                    return true;
                },
                phone_format:(value) => {
                    const regex = /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/
                    if (!value) {
                        return true;
                    }
                    if ( !regex.test(value)) {

                        return '⚠ Формат телефона нарушен';
                    }
                    return true;
                },
                email: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' почту';
                },
                address: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' адрес';
                },
                date: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' дату доставки';
                },
                time: (value) => {
                    if (value) {
                        return true;
                    }
                    return ' время доставки';
                }
            },
            DATA: {
                Levels: cakeNames['levels'],
                Forms: cakeNames['forms'],
                Toppings: cakeNames['toppings'],
                Berries: cakeNames['berries'],
                Decors: cakeNames['decors'],
            },
            Costs: {
                Levels: cakeCosts['levels'],
                Forms: cakeCosts['forms'],
                Toppings: cakeCosts['toppings'],
                Berries: cakeCosts['berries'],
                Decors: cakeCosts['decors'],
                Words: 500
            },
            Levels: cakeLevels  ,
            Form: cakeForm ,
            Topping: cakeTopping ,
            Berries: cakeBerries ,
            Decor: cakeDecor ,
            Words: '',
            Comments: cakeComments,
            Designed: false,

            Name: '',
            Phone: null,
            Email: null,
            Address: null,
            Dates: null,
            Time: null,
            DelivComments: ''
        }
    },
    methods: {
        ToStep4() {
            this.Designed = true
            setTimeout(() => this.$refs.ToStep4.click(), 0);
        }
    },
    computed: {
        Cost() {
            let W = this.Words ? this.Costs.Words : 0
            return this.Costs.Levels[this.Levels] + this.Costs.Forms[this.Form] +
                this.Costs.Toppings[this.Topping] + this.Costs.Berries[this.Berries] +
                this.Costs.Decors[this.Decor] + W
        }
    }
}).mount('#VueApp')
