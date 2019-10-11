<template>
    <div class="mb-3">
        <div class="card container-fluid">
            <div class="row header-wrapper">
                <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                    <h6 class="header pr-1">{{$store.getters.getClientDetails.full_name}}</h6>
                    <!--<div class="header-border"></div>-->
                    <!--<span class=__email ml-1">-->
                    <!--{{$store.getters.getAgentDetails.agent.user.email}}-->
                    <!--</span>-->
                </div>
            </div>
            <div class="row">
                <div class="col-6">
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Организация:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.organization}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Вид деятельности:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.kind_of_activity.map((item)=>{return
                                item.activity})}}</h6>
                            <!--<h6 class="header">{{$store.getters.getAgentDetails.agent.user.email}}</h6>-->
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Наименование:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.full_name}}</h6>

                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">БИН/ИНН:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.bin_iin}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Адрес (физ.):</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.address_physical}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Адрес (юр.):</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.address_legal}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Доп. адрес:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.extra_address}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Контактный номер:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.phone_number}}</h6>
                        </div>
                    </div>
                </div>
                <div class="col-6">
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">БИК:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.bik}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">ИИК:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.iik}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Банк:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.bank_name}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Кбе:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.kbe}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Руководитель:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.leader}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Должность:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.position_leader}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">Контактный номер:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.phone}}</h6>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-4 py-3 justify-content-start">
                            <h6 class="header">УГД:</h6>
                        </div>
                        <div class="col-8 py-3 justify-content-start">
                            <h6 class="header">{{$store.getters.getClientDetails.tax.name}}</h6>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row clients__info-wrapper py-2">
                <div class="col-4 d-flex">
                    <span class="table__icon clients__icon"> <font-awesome-icon :icon="['fas' ,'users']"/></span>
                    <div>
                        <p class="mb-0 clients__info">Дата создания: {{$store.getters.getClientDetails.date}}</p>
                        <p class="mb-0 clients__info">Дата изменения: </p>
                    </div>
                </div>
                <div class="col-4 d-flex">
                    <span class="table__icon clients__icon"> <font-awesome-icon :icon="['fas' ,'users']"/></span>
                    <div>
                        <p class="mb-0 clients__info">Дата подписания договора:
                            {{$store.getters.getClientDetails.date}}</p>
                        <p class="mb-0 clients__info">Дата окончания договора: </p>
                        <p class="mb-0 clients__info">Сумма договора: </p>
                    </div>
                </div>
                <div class="col-4 d-flex">
                    <span class="table__icon clients__icon"> <font-awesome-icon :icon="['fas' ,'users']"/></span>
                    <div>
                        <p class="mb-0 clients__info">Агент: {{$store.getters.getClientDetails.date}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ClientsDetails"
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

    .clients__icon {
        color: $gray !important;
        justify-content: flex-start !important;
        align-items: flex-start !important;
    }

    .clients__info {
        font-size: convertFontToRem(12);
        color: $gray;
        margin-left: 19px;
        &-wrapper{
            border-top: 1px solid $gray;
        }
    }
</style>