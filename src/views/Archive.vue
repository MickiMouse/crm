<template>
    <h3>archive</h3>
</template>

<script>
    export default {
        name: "Archive",
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>