<template>
    <div class="w-100 card container-fluid h-100">
        <div class="row">
            <div class="col-12 pt-1 d-flex align-items-center justify-content-start">
                <span class="icon"> <font-awesome-icon :icon="icon"/></span>
                <h6 class="header ml-1">{{header}}</h6>
            </div>
        </div>
        <div class="row">
            <div class="col-12 my-5 pt-1">
                <h3 class="value">{{value}}</h3>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "infoCard",
        props: {
            value: Number,
            header: String,
            icon: Array,
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

    .card {
        .icon{
            display: flex;
            align-items: center;
            justify-content: center;
            color: $primary;
            svg{
                width: 34px !important;
                height: 34px !important;
            }
        }
        .header{
            font-size: convertFontToRem(14);
            font-weight: bold;
            margin-bottom: 0;
        }
        .value{
            font-size: convertFontToRem(48);
            font-weight: 400;
            margin-bottom: 0;
        }
    }
</style>