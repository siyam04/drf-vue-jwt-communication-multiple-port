<template>

    <tbody>
    <tr v-for="(item, i) in contents.body" :key="i">
        <td v-if="contents.serialActivate">{{i+1}}</td>
        <td v-for="(data, key) in contents.header" :key="key">
            {{item[key]}}
        </td>
    </tr>
    </tbody>

</template>


<script>
    export default {
        name: "TableBody",
        // props: ['headerContent', 'bodyContent']
        props: ['contents'],
        data (){
            return {

            }
        },

    }
</script>


<style scoped>

</style>

