<template>
    <div class="div">
        <div class="card container-fluid">
            <div class="row card__header header-wrapper">
                <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                    <h6 class="header pr-1">{{$store.getters.getAgentDetails.agent.user.full_name}}</h6>
                    <div class="header-border"></div>
                    <span class="card__header__email ml-1">
                   {{$store.getters.getAgentDetails.agent.user.email}}
                </span>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">ФИО:</h6>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <h6 class="header">{{$store.getters.getAgentDetails.agent.user.full_name}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">E-mail:</h6>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <h6 class="header">{{$store.getters.getAgentDetails.agent.user.email}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Номер телефона:</h6>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <h6 class="header">{{$store.getters.getAgentDetails.agent.phone}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Клиентов:</h6>
                </div>
                <div class="col-8 py-3 card__header justify-content-start">
                    <h6 class="header">{{$store.getters.getAgentDetails.agent.clients.length}}</h6>
                </div>
            </div>
        </div>
        <div class="card card-dark container-fluid my-3">
            <div class="row">
                <div class="col-4 card__header"></div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Учтено налогов</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Оплата БУ</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">План</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.plan_taxes}}</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.plan_accounting_services}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Факт</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.fact_taxes}}</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.fact_accounting_services}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Отколнение</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.deflection_taxes}}</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.deflection_accounting_services}}</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Уведомлено</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.notified}}</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">test@mail.ru</h6>
                </div>
            </div>
            <div class="row">
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="header">Не уведомлено</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">{{$store.getters.getAgentDetails.not_notified}}</h6>
                </div>
                <div class="col-4 py-3 card__header justify-content-start">
                    <h6 class="subheader">test@mail.ru</h6>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AgentsDetails"
    }
</script>

<style scoped>

</style>