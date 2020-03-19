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


Vue.component('main-cart-item', {
    delimiters: ['[[', ']]'],
    props: ['item','index'],
    template :`  <div class="main-cart-item">
                            <div class="main-cart-item-name">
                                <img src="https://dummyimage.com/70x80/000/fff" alt=""> <span>[[item.name]]</span>
                            </div>
                            <div class="main-cart-item-number">
                                <div class="item-info-price-quantity">
                                    <p v-on:click="delQt(index)">-</p><input style="background: transparent; color:#e63d44 " id="quantity" readonly type="number" :value="[[item.num]]" min="1"><p v-on:click="addQt(index)">+</p>
                                </div>
                            </div>
                            <div class="main-cart-item-price">[[item.price]] <i class="fa fa-rub"></i></div>
                            <div class="main-cart-item-total-price">[[item.num * item.price]] <i class="fa fa-rub"></i></div>
                            <div class="main-cart-item-action"><span class="cart-delete-btn" v-on:click="userDelete(index)">&#10006;</span></div>
                        </div>`,

    methods: {
        userDelete: function (index) {
            this.$emit('userdelete', index);
        },
        delQt: function (index) {

            this.$emit('del_qt', index);
        },
        addQt: function (index) {
            this.$emit('add_qt', index);
        }
    }
})

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        cartTotal:0,
        cartNotEmpty : false,
        headerCartItems: [
        ]
    },

    methods:{
        remove: function(index){
            this.headerCartItems.splice(index, 1)
        }
        ,
        del_qt: function (index) {
            if (this.headerCartItems[index]['num'] > 1){
                this.headerCartItems[index]['num'] -= 1
                this.updateCart()
            }
        },
        add_qt: function (index) {
           this.headerCartItems[index]['num'] += 1
             this.updateCart()
        },
        updateCart: function () {
            console.log('update')
             this.cartTotal = 0
            for(var item in this.headerCartItems){
                console.log(this.headerCartItems[item]['price'])
                this.cartTotal +=  parseInt(this.headerCartItems[item]['price']) * parseInt(this.headerCartItems[item]['num'])
            }
        },
        addItem: function (event) {
            item_id = event.target.getAttribute('data-id')
            item_name = event.target.getAttribute('data-name')
            item_price = event.target.getAttribute('data-price')
            console.log('add')
            this.headerCartItems.push({id:item_id,name:item_name,price:item_price,num:1 })
           event.target.innerText='в клрзине'
            event.target.setAttribute('disabled','disabled')




        }
    },
    watch: {
        headerCartItems: function (val) {
            console.log('change')
            this.cartTotal = 0
            for(var item in val){
                console.log(val[item]['price'])
                this.cartTotal +=  parseInt(val[item]['price']) * parseInt(val[item]['num'])
            }
        }
    }
})