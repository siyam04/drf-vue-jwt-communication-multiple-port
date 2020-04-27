<template>

    <div class="container">
        <div class="jumbotron">
            <h1>Players</h1>
            <br><br>

            <table class="table">
                <TableHead v-bind:headerContent="headerContent"></TableHead>
                <!--<TableBody v-bind:bodyContent="bodyContent" v-bind:headerContent="headerContent">></TableBody>-->
                <TableBody v-bind:contents="{header: headerContent, body: bodyContent}"></TableBody>
            </table>

            <button class="btn btn-dark">
                <router-link :to="{name: 'User'}">GoTo User</router-link>
            </button>

        </div>
    </div>

</template>


<script>
    import TableHead from "../table_parts/TableHead";
    import TableBody from "../table_parts/TableBody";


    export default {
        name: "Players",
        components: {TableHead, TableBody},
        data() {
            return {
                headerContent: {
                    serial: 'SERIAL',
                    player_name: 'PLAYER NAME',
                    score: 'SCORE',
                },
                bodyContent: [
                    {
                        player_name: 'Maruf',
                        serial: '1',
                        score: '100',
                    },
                    {
                        serial: '2',
                        player_name: 'Julu',
                        score: '80',
                    },
                    {
                        score: '50',
                        serial: '3',
                        player_name: 'Tajal',
                    },
                    {
                        score: '60',
                        serial: '4',
                        player_name: 'Sayket',
                    },
                ]
            }
        }
    }
</script>


<style scoped>


</style>

