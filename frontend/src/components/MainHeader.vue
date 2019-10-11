<template>
  <div class="fixed-top" :class="{'col-sm-9 offset-sm-3': !$store.getters.getIsMenuActive,'col-sm-11 offset-sm-1':$store.getters.getIsMenuActive}">
      <header class="row main-header align-items-center justify-content-between">
          <div class="col-5 main-header__element-wrapper  d-flex align-items-center">
              <h3 class="panel-name mt-1">{{this.$route.meta.title}}</h3>
          </div>
          <div class="col-7 d-flex justify-content-end main-header__element-wrapper">
              <div class="main-header__search main-header__icon main-header__element-wrapper--border">
                  <font-awesome-icon :icon="['fas' ,'search']"/>
              </div>
              <div class="main-header__icon main-header__element-wrapper--border">
                  <font-awesome-icon :icon="['far' ,'envelope']"/>
              </div>
              <div class="main-header__icon main-header__element-wrapper--border">
                  <font-awesome-icon :icon="['fas' ,'clipboard-list']"/>
              </div>
              <div class="d-flex align-items-start justify-content-center flex-column">
                  <span class="main-header__name">{{ this.$session.get('username').split(' ')[0]}}</span>
                  <span class="main-header__name">{{ this.$session.get('username').split(' ')[1]}}</span>
                  <span class="main-header__position">{{ this.$session.get('role')}}</span>
              </div>
          </div>
      </header>
  </div>

</template>

<script>
    export default {
        name: "MainHeader"
    }
</script>

<style lang="scss" scoped>
    @import "../scss/main";

    .main-header {
        background: $white;
        .panel-name {
            /*padding-left: 35px;*/
        }

        &__element-wrapper {
            min-height: 85px;
            > div {
                padding-right: 35px;
                padding-left: 35px;
            }
            svg {
                width: convertFontToRem(30);
                height: convertFontToRem(30);
            }
            h3 {
                font-size: convertFontToRem(24);
                color: $primary;
            }
            .main-header__search, .main-header__icon {
                display: flex;
                align-items: center;
            }
            &--border {
                border-right: 2px solid $secondary;
            }
        }
        &__name {
            font-size: convertFontToRem(18);
        }
        &__position {
            font-size: convertFontToRem(12);
            color: #cdcdcd;
        }
    }
</style>