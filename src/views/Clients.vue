<template>
    <h3>clients</h3>
</template>

<script>
    export default {
        name: "Clients",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>