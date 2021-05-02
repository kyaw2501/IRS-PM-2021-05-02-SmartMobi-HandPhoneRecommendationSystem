<template>
    <v-app>
        <v-parallax
                height="750"
                src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
        >
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col class="text-center" cols="12">
                    <h1 class="display-1 font-weight-thin mb-4">Smartphone Recommender systems</h1>

                    <v-btn
                            rounded
                            class="ma-2"
                            color="orange"
                            dark
                            to="/en-1">
                        Enter
                    </v-btn>
                    <h4 class="subheading">Best Smartphone for You</h4>
                </v-col>
            </v-row>
        </v-parallax>
    </v-app>
</template>

<script>
    // @ is an alias to /src
    // import bgimg from '@/../public/back.png';

    export default {
        name: 'Home',
        components: {},
        data() {
            return {
                backgroundDiv: {
                    backgroundImage: 'url(' + require('@/../public/back.png') + ')',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: '100% 100%'
                }

            }
        }
    }
</script>