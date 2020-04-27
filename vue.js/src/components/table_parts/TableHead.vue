<template>

    <thead>
        <tr>
            <th v-if="headerContents.serialActivate">SL</th>
            <th v-for="(item, i) in headerContents.header" :key="i" scope="col" @click="sorting(item)">
                <router-link to="#">{{item}}</router-link>
            </th>
        </tr>
    </thead>

</template>


<script>

    export default {
        name: "TableBody",
        props: ['headerContents'],
        methods: {
            sorting(param){
                console.log(param)

            }
        },
        data () {
            return {
                showHide: true
            }
        },
    }
</script>


<style scoped>

</style>

