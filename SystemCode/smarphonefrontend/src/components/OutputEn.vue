<template>
    <v-app>
        <div>
            <v-container fluid>
                <v-row>
                    <v-col cols="12">
                        <v-row
                                class="grey lighten-5"
                                style="height: 1000px;"
                        >
                            <v-card
                                    v-for="output_id in [0,1,2]"
                                    :key="output_id"
                                    class="mx-auto"
                                    max-width="400px"
                                    elevation="14"
                            >
                                <v-img
                                        class="mx-auto"
                                        height="160px"
                                        width="130px"
                                        :src="output[output_id]['img_src']"
                                >
                                </v-img>

                                <v-card-title>{{ output[output_id]['brand_model'] }}</v-card-title>

                                <v-card-subtitle
                                        class="v-card__title"

                                >SGD {{ output[output_id]['price'] }}
                                </v-card-subtitle>

                                <v-card-subtitle class="pb-0">Specification</v-card-subtitle>

                                <v-card-text class="text--primary">
                                    <v-simple-table>
                                        <template v-slot:default>
                                            <tbody>
                                            <!-- CPU -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >CPU
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['chipset'] }}</td>
                                            </tr>

                                            <!-- GPU -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >GPU
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['gpu'] }}</td>
                                            </tr>

                                            <!-- RAM -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >RAM
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['ram'] }}</td>
                                            </tr>

                                            <!-- Storage -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Storage
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['storage'] }}</td>
                                                
                                            </tr>
                                            
                                            <!-- Resolutions -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Resolutions
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['resolutions'] }}</td>
                                            </tr>

                                            <!-- Screen size-->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Screen Size
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['screen size'] }}</td>
                                            </tr>

                                            <!-- Dimensions -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Dimensions
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['dimensions'] }}</td>
                                            </tr>

                                            <!-- Weight -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Weight
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['weight'] }}</td>
                                            </tr>

                                            <!-- Front Cam -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Front Camera
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['front'] }}</td>
                                            </tr>

                                            <!-- Rear Cam -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Rear Camera
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['rear'] }}</td>
                                            </tr>

                                            <!-- Batt Capacity -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Battery
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['capacity'] }}</td>
                                            </tr>

                                            <!-- Fast Charge -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Fast Charge
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['fast_charging'] }}</td>
                                            </tr>

                                            <!-- SIM -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >SIM Card
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['sim'] }}</td>
                                            </tr>

                                            <!-- Color -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Color
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['color'] }}</td>
                                            </tr>

                                            <!-- Carrier -->
                                            <tr>
                                                <td>
                                                    <v-btn
                                                            rounded
                                                            color="primary"
                                                    >Carrier
                                                    </v-btn>
                                                </td>
                                                <td>{{ output[output_id]['carrier'] }}</td>
                                            </tr>

                                            </tbody>
                                        </template>
                                    </v-simple-table>
                                </v-card-text>

                                <v-card-actions>
                                    <v-btn
                                            color="orange"
                                            text
                                            :href="output[output_id]['link']"
                                    >
                                        Detail Link
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-row>
                    </v-col>
                </v-row>
            </v-container>
        </div>


        <v-speed-dial
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        color="blue darken-2"
                        dark
                        fab
                        v-on:click="back"
                >
                    <v-icon>mdi-arrow-left-circle</v-icon>
                </v-btn>
            </template>
        </v-speed-dial>

    </v-app>
</template>

<script>
    export default {
        pat: '/output-en',
        data() {
            return {
                price: '',
                purpose: '',
                brand:'',
                FastCharge: '',
                Need_5G: '',
                BatteryLife: '',
                screen: '',

                output: {},

                fit1: false,
            }
        },
        created() {
            this.price = this.$route.params.price;
            this.purpose = this.$route.params.purpose;
            this.brand = this.$route.params.brand;
            this.FastCharge = this.$route.params.FastCharge;
            this.Need_5G = this.$route.params.Need_5G;
            this.BatteryLife = this.$route.params.BatteryLife;
            this.screen = this.$route.params.screen;            
            

            let res = {
                price: this.price,
                purpose: this.purpose,
                brand: this.brand,
                FastCharge: this.FastCharge,
                Need_5G: this.Need_5G,
                BatteryLife: this.BatteryLife,
                screen: this.screen,
            }

            function create_res(res) {
                let values = Object.values(res);
                let res_str = '';
                let count = 0;
                for (let keys in res) {
                    if (res_str === '') {
                        res_str = keys + '=' + values[count];
                    } else {
                        res_str = res_str + '&' + keys + '=' + values[count];
                    }
                    count++;
                }
                return res_str;
            }

            let res_str = create_res(res);
            console.log('post: ' + JSON.stringify(res));

            fetch('http://127.0.0.1:5000/interface', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                }, // this line is important, if this content-type is not set it wont work
                body: res_str,
                //mode: 'cors',
            })
                .then(response => response.json())
                .then(response => {
                    console.log('post: ' + JSON.stringify(res));
                    for (let i = 0; i < Object.keys(response).length; i++)
                        console.log('output: ' + JSON.stringify(response[i]));

                    this.output = response;
                    console.log(Object.keys(this.output[0]));
                    console.log(Object.keys(this.output));
                    if(Object.keys(this.output[0])[0] == 'mes')
                    {
                        alert("Unable to reason about the result, please re-fill the questionnaire and try again")
                        this.$router.go(-1);
                    }
                })
                .catch(error => console.error('Error:', error));

        },
        methods: {
            back() {
                this.$router.go(-1);
            }
        }

    }
</script>

<style scoped>

</style>