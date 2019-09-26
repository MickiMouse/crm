<template>
    <div class="w-100 card">
        <div class="row card__header">
            <div class="col-2">
                <span class="card__header-icon">
                     <font-awesome-icon :icon="['fas' ,'clipboard-list']"/>
                </span>

            </div>
            <div class="col-10">
                <h4>Динамика роста клиентов</h4>
            </div>
        </div>
        <div class="row">
                <div class="col-12">
                    <apexchart type=line height=300 :options="chartOptions" :series="series" />
                </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "dynamicsClients",
        data(){
            return{
                series: [{
                    name: "Desktops",
                    data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
                }],
                chartOptions: {
                    chart: {
                        height: 350,
                        zoom: {
                            enabled: false
                        }
                    },
                    dataLabels: {
                        enabled: false
                    },
                    stroke: {
                        curve: 'straight'
                    },
                    grid: {
                        row: {
                            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                            opacity: 0.5
                        },
                    },
                    xaxis: {
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
                    }
                }
            }
        }
    }
</script>

<style scoped>

</style>