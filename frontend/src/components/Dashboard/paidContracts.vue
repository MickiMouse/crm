<template>
    <div class="w-100 card">
        <div class="row card__header">
            <div class="col-2">
                <span class="card__header-icon">
                     <font-awesome-icon :icon="['fas' ,'clipboard-list']"/>
                </span>

            </div>
            <div class="col-10">
                <h4>Оплаченных договоров</h4>
            </div>
        </div>
        <div class="row">
            <div class="col-12 d-flex justify-content-center">
                <v2-datepicker-range v-model="date" :lang="'en'"
                                     format="dd/MM/yyyy" @change="getData"></v2-datepicker-range>
            </div>
            <div class="col-12">
                <apexchart type=donut height=300 :options="chartOptions" :series="data"/>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "paidContracts",
        data() {
            return {
                date: '',
                data: this.data,

                chartOptions: {
                    labels: ['Paid', 'Unpaid',],
                    responsive: [{
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 200
                            },
                            legend: {
                                position: 'bottom'
                            }
                        }
                    }]
                }
            }
        },
        props: {
            data: Array
        },
        methods: {
            getData() {
                axios.post(`${this.$hostname}/api/dashboard/`, {
                    type: 'pie',
                    range: {
                        'from': this.dateFormatFrom,
                        to: this.dateFormatTo
                    }
                })
                    .then((response) => {
                        if(response.status === 200){
                            this.data = response.data.pie_chart;
                            console.log(response.data)
                        }

                    })
            }
        },
        computed: {
            dateFormatFrom() {
                return `${new Date(this.date[0]).getDate()}.${new Date(this.date[0]).getMonth() + 1}.${new Date(this.date[0]).getFullYear()}`
            },
            dateFormatTo() {
                return `${new Date(this.date[1]).getDate()}.${new Date(this.date[1]).getMonth() + 1}.${new Date(this.date[1]).getFullYear()}`
            },
        },

    }
</script>

<style>
    .v2-date-wrap {
        border: none;
    }
</style>