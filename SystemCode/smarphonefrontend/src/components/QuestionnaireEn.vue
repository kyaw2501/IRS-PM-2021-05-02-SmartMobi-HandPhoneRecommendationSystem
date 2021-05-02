<template>
    <v-app>
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    May I know your budget to buy a smartphone?
                    <template v-slot:actions>
                        <!--                        <v-icon v-if="is_finish[0] === 0" color="error">mdi-alert-circle</v-icon>-->
                        <v-icon v-if="price === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="price !== ''" color="teal">mdi-check</v-icon>
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <div class="col-md-3 vue-bg h-100 d-flex justify-content-center align-items-left form-group">
                        <input type="text" class="form-control form-control-lg" placeholder="Enter a number (in SGD)" v-model = "price"/>
                        <br /><br />
                        <v-btn
                            rounded
                            color="primary"
                            dark
                            v-on:click="jump"
                            >Next
                        </v-btn>
                        <br /><br />
                    </div>
                </v-expansion-panel-content>
            </v-expansion-panel> 

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Would you like only iPhones?
                    <template v-slot:actions>
                        <v-icon v-if="brand.length === 0" color="primary">$expand</v-icon>
                        <v-icon v-else-if="brand.length !== 0" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="brand" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='apple'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='none'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    What do you mostly do with your phone?
                    <template v-slot:actions>
                        <v-icon v-if="purpose === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="purpose !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="purpose" column>
                        <v-radio
                                label="Watch video"
                                color="orange darken-3"
                                value='video'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Reading"
                                color="orange darken-3"
                                value='reading'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Play games"
                                color="orange darken-3"
                                value='game'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Do you want Fast Charge?
                    <template v-slot:actions>
                        <v-icon v-if="FastCharge === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="FastCharge !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="FastCharge" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='true'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='false'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    Do you want 5G carrier?
                    <template v-slot:actions>
                        <v-icon v-if="Need_5G === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="Need_5G !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="Need_5G" column>
                        <v-radio
                                label="Yes"
                                color="orange darken-3"
                                value='true'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="No"
                                color="orange darken-3"
                                value='false'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    How often do you need to charge your previous phone in one day?
                    <template v-slot:actions>
                        <v-icon v-if="BatteryLife === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="BatteryLife !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="BatteryLife" column>
                        <v-radio
                                label="One time"
                                color="orange darken-3"
                                value='false'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="More than One time"
                                color="orange darken-3"
                                value='true'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    May I ask which of the following categories do you satisfy with screen size?
                    <template v-slot:actions>
                        <v-icon v-if="screen === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="screen !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="screen" column>
                        <v-radio
                                label="Small (less than 6.2 inches), "
                                color="orange darken-3"
                                value='small'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Medium (between 6.2 and 6.7 inches) "
                                color="orange darken-3"
                                value='medium'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Large (greater than 6.7 inches)"
                                color="orange darken-3"
                                value='large'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="Doesn't matter"
                                color="orange darken-3"
                                value='dontcare'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>
            
        </v-expansion-panels>


        <div>
            <v-btn
                    rounded
                    class="ma-2"
                    color="primary"
                    dark
                    v-on:click="submit"
            >Submit
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
        </div>


        <v-progress-linear
                fixed
                background-opacity="0.3"
                :value="degree"
                color="primary"
        ></v-progress-linear>


        <v-speed-dial
                v-model="fab"
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        v-model="fab"
                        color="blue darken-2"
                        dark
                        fab
                >
                    <v-icon v-if="fab">mdi-close</v-icon>
                    <v-icon v-else>mdi-menu</v-icon>
                </v-btn>
            </template>
            <v-btn
                    fab
                    dark
                    small
                    color="green"
            >
                En/Ch
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="indigo"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="red"
            >
                <v-icon>mdi-account-circle</v-icon>
            </v-btn>
        </v-speed-dial>


    </v-app>

</template>

<script>
    export default {
        name: "QuestionnaireEn",
        data() {
            return {
                price: '',
                purpose: '',
                brand:'',
                FastCharge: '',
                Need_5G: '',
                BatteryLife: '',
                screen: '',


                fab: false, 
                active_question: 0, 
                degree: '',
                num_question: 7,
                num_ans: 0, 
            }
        },


        methods: {
            submit() {                
                this.$router.push(
                    {
                        name: 'OutputEn',
                        params: {
                            price: this.price,
                            purpose: this.purpose,
                            brand: this.brand,
                            FastCharge: this.FastCharge,
                            Need_5G: this.Need_5G,
                            BatteryLife: this.BatteryLife,
                            screen: this.screen,
                        }
                    });
            },

            jump() {
                let count_ans = 0;
                let flag = {
                    price: this.price,
                    purpose: this.purpose,
                    brand: this.brand,
                    FastCharge: this.FastCharge,
                    Need_5G: this.Need_5G,
                    BatteryLife: this.BatteryLife,
                    screen: this.screen,
                }

                for (let i = 0; i < Object.keys(flag).length; i++) {
                    if (Object.values(flag)[i] !== '') {
                        count_ans += 1
                    }
                }

                this.active_question += 1

                this.degree = count_ans / this.num_question * 100

            },
        }
    }
</script>

<style scoped>

</style>