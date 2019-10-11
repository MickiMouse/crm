<template>
    <div class="container-fluid">
        <div class="row align-items-center justify-content-center form-wrapper">
            <form class="col-sm-4" @submit.stop.prevent="submitForm">
                <b-form @submit.stop.prevent>
                    <label for="email">Email</label>
                    <b-input v-model="email" :state="emailValidation" id="email"></b-input>
                    <b-form-invalid-feedback :state="emailValidation">
                        Invalid email
                    </b-form-invalid-feedback>
                    <b-form-valid-feedback :state="emailValidation">
                        Looks Good.
                    </b-form-valid-feedback>

                    <label for="password">Password</label>
                    <b-input v-model="password" :state="passwordValidation" type="password" id="password"></b-input>
                    <b-form-invalid-feedback :state="passwordValidation">
                        Password length must be from 8 and more
                    </b-form-invalid-feedback>
                    <b-form-valid-feedback :state="passwordValidation">
                        Looks Good.
                    </b-form-valid-feedback>
                </b-form>
                <b-button variant="success" type="submit">Войти</b-button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Login",
        data() {
            return {
                email: '',
                password: ''
            }
        },
        computed: {
            emailValidation() {
                const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                return pattern.test(this.email)
            },
            passwordValidation() {
                return this.password.length > 8
            }
        },
        methods: {
            submitForm() {
                if (this.emailValidation && this.passwordValidation) {
                    axios.post(`${this.$hostname}/api/login/ `, {email: this.email, password: this.password})
                        .then((response) => {
                            console.log(response.data)
                            if (response.status === 200) {
                                console.log(response)
                                this.$session.start()
                                this.$session.set('jwt', response.data.access_token)
                                axios.defaults.headers.common['Authorization'] = 'Token ' + this.$session.get('jwt');
                                this.$router.push('/dashboard')
                            }
                        }).catch((error) => {

                    });
                }
            }
        },
        beforeCreate() {
            this.$session.destroy();
            this.$router.push('/');
            axios.defaults.headers.common['Authorization'] = '';
            if (this.$route.params.token) {
                this.verifyRegisterLoading = true;
                axios.get(`${this.$hostname}/api/register_activate/${this.$route.params.token}/`)
                    .then((response) => {
                        if (response.status === 200) {
                            this.verifyRegisterLoading = false;
                            this.name = response.username;
                            this.text = "Registration successful";
                            this.snackbar = true;
                        }
                    }).catch((error) => {
                    this.verifyRegisterLoading = false;
                    this.text = "Connection error";
                    console.log(error)
                    this.snackbar = true;
                });
            }
        }
    }
</script>

<style lang="scss" scoped>
    .form-wrapper {
        min-height: 100vh;
    }
</style>