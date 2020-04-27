<template>

    <div class="container">
        <div class="jumbotron">
            <h1>Users</h1>
            <br><br>

            <table class="table">
                <TableHead v-bind:headerContents="{header: headerContent, serialActivate: true}"></TableHead>
                <TableBody v-bind:contents="{header: headerContent, body: bodyContent, serialActivate: true}"></TableBody>
            </table>

            <button class="btn btn-dark">
                <router-link :to="{name: 'Players'}">GoTo Players</router-link>
            </button>

        </div>
    </div>

</template>


<script>

    import TableHead from "../table_parts/TableHead";
    import TableBody from "../table_parts/TableBody";


    export default {
        name: "User",
        components: {TableHead, TableBody},
        data() {
            return {
                headerContent: {
                    name: 'NAME',
                    age: 'AGE',
                },
                bodyContent: [
                    {
                        age: '20',
                        name: 'Mostaq',
                    },
                    {
                        name: 'Tazel',
                        age: '23',
                    },
                    {
                        age: '66',
                        name: 'Karim',
                    },
                ]

            }
        },
    }
</script>


<style scoped>

</style>


