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
                <div class="col-12">
                    <apexchart type=donut height=300 :options="chartOptions" :series="series" />
                </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "paidContracts",
        data(){
            return{
                series: [44, 56],
                chartOptions: {
                    labels: ['Team A', 'Team B',],
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
        }
    }
</script>

<style scoped>

</style>