<template>
    <div class="card">
        <div class="row header-wrapper pl-3">
            <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                <span class="table__icon"> <font-awesome-icon :icon="icon"/></span>
                <h6 class="header ml-1">{{header}}</h6>
                <button class="more-btn ml-auto" @click="isTableExpanded = !isTableExpanded">Все</button>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <b-table striped hover
                         :items="items"
                         :fields="fields"
                         :striped="false"
                         :per-page="visibleItems"
                         :fixed="true"
                         class="mb-0"
                >
                </b-table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "expandTable",
        data() {
            return {
                isTableExpanded: false
            }
        },
        props: {
            items: Array,
            fields: Array,
            header: String,
            icon: Array
        },
        computed: {
            visibleItems() {
                return this.isTableExpanded === false ? 5 : this.items.length
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

    .card {
        text-align: center;
    }

</style>