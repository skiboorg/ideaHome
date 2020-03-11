Vue.component('header-cart-items', {
    delimiters: ['[[', ']]'],
    props: ['item','index'],
    template: '<div class="header-cart-item">\n' +
        '                                    <img src="http://placehold.it/50" alt="">\n' +
        '                                    <div class="header-cart-item-info">\n' +
        '                                        <p>[[item.name]]</p>\n' +
        '                                        <span class="header-cart-item-info-num">[[item.num]]</span>\n' +
        '                                        x\n' +
        '                                        <span class="header-cart-item-info-price">[[item.price]]</span>\n' +
        '                                        =\n' +
        '                                        <span class="header-cart-item-info-total">[[item.num * item.price]]</span>\n' +
        '                                    </div>\n' +
        '                                    <div class="header-cart-item-remove">\n' +
        '                                        <a  v-on:click="userDelete(index)">X</a>\n' +
        '                                    </div>\n' +
        '\n' +
        '                                </div>',
    methods: {
        userDelete: function(index){
            this.$emit('userdelete', index);
        }
    }
})

var HeaderCart = new Vue({
    delimiters: ['[[', ']]'],
    el: '#HeaderCart',
    data: {
        cartTotal:0,
        headerCartItems: [
        ]
    },
    methods:{
        remove: function(index){
            this.headerCartItems.splice(index, 1)
        }
    },
    watch: {
        headerCartItems: function (val) {
            this.cartTotal = 0
            for(var item in val){
                console.log(val[item]['price'])
                this.cartTotal +=  parseInt(val[item]['price']) * parseInt(val[item]['num'])
            }
        }
}
})