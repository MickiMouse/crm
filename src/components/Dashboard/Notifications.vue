<template>
    <div class="card container-fluid">
        <div class="row header-wrapper pl-3">
            <div class="col-12 pl-0 pt-1 d-flex align-items-center justify-content-start">
                <span class="icon"> <font-awesome-icon :icon="icon"/></span>
                <h6 class="header ml-1">{{header}}</h6>
                <button class="more-btn" @click="isTableExpanded = !isTableExpanded">Все</button>
            </div>
        </div>
        <div class="row">
            <div class="col-12 notification text-left" v-for="itam in visibleItems">
                <h6 class="notification__username">
                    Диана Айтхожина
                </h6>
                <p class="notification__message">
                    Добрый день, оставляю Вам сообщение...
                </p>
                <span class="notification__date">
                    11.05 19:07
                </span>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Notifications",
        data() {
            return {
                isTableExpanded: false
            }
        },
        props: {
            items: Array,
            header: String,
            icon: Array
        },
        computed: {
            visibleItems() {
                // return this.isTableExpanded === false ? 5 : this.items.length
                return this.isTableExpanded === false ? 5 : 11
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

    .card {
        text-align: center;
    }

    .icon {
        display: flex;
        align-items: center;
        justify-content: center;
        color: $primary;
        margin-top: 9px;
        margin-bottom: 9px;
        svg {
            width: 24px !important;
            height: 24px !important;
        }
    }

    .header {
        font-size: convertFontToRem(14);
        font-weight: bold;
        margin-bottom: 0;
    }

    .more-btn {
        font-size: convertFontToRem(16);
        text-decoration: underline;
        background: transparent;
        border: none;
        text-transform: uppercase;
        color: #716d6d;
        margin-left: auto;
        margin-right: 34px;
    }
    .notification{
        border-top: 1px solid $secondary;
        border-bottom: 1px solid $secondary;
        &__username{
            font-size: convertFontToRem(14);
            font-weight: bold;
            margin-bottom: 9px;
            padding-top: 17px;
        }
        &__message{
            font-size: convertFontToRem(14);
            margin-bottom: 11px;
        }
        &__date{
            font-size: convertFontToRem(12);
            color: #b9b9b9;
        }
    }
</style>