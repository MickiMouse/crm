<template>
    <h3>debtors</h3>
</template>

<script>
    export default {
        name: "Debtors",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>