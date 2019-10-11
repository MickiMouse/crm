<template>
    <button @click="handleClick">
        <font-awesome-icon :icon='icon'/>
    </button>
</template>

<script>
    export default {
        name: "ActionButton",
        methods: {
            handleClick() {
                this.$emit('click')
            },
        },
        props: {
            icon: Array
        }
    }
</script>

<style lang="scss" scoped>
    @import "../../scss/main";

    button {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 1px solid $gray;
        display: flex;
        align-items: center;
        justify-content: center;
        color: $darkgray;
        svg {
            width: .55rem !important;
        }
        &:hover {
            background: $primary;
            color: $white;
        }
    }
</style>