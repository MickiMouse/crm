<template>
    <h3>agents</h3>
</template>

<script>
    export default {
        name: "Agents",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>