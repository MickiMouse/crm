<template>
    <div class="card container-fluid">
        <div class="row card__header header-wrapper">
            <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                <h6 class="header">Клиенты агента</h6>

                <button class="main-btn ml-auto" @click="">Добавить агента</button>
                <button class="more-btn ml-2" @click="isTableExpanded = !isTableExpanded">Все</button>
            </div>
        </div>
        <div class="row">
            <div class="col-12 py-3 card__header justify-content-start">
                <h6 class="header">Наиминование</h6>
            </div>
            <div class="col-12 py-3 card__header justify-content-start" v-for="client in $store.getters.getAgentDetails.agent.clients">
                <h6 class="header table-accent">{{client.short_name}}</h6>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AgentsClients"
    }
</script>

<style scoped>

</style>