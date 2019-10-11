<template>
    <div class="content">
        <div class="row">
            <div class="col-12">
              <debtors-table/>
            </div>
        </div>
    </div>
</template>

<script>
    import DebtorsTable from "../components/Debtors/DebtorsTable";
    export default {
        name: "Debtors",
        components: {DebtorsTable},
        beforeCreate() {
            if (!this.$session.exists()) {
                this.$router.push('/')
            }
        },
    }
</script>

<style scoped>

</style>