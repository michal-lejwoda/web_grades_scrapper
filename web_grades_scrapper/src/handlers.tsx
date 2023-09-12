import {
    useImdbDetailQuery,
    useImdbListQuery,
    useMetacriticDetailQuery,
    useMetacriticListQuery,
    useOpencriticDetailQuery,
    useOpencriticListQuery
} from "./hooks.tsx";

export const handleMetacriticList = () => {
    console.log("handleMetacriticList")
    const metacritic_list = useMetacriticListQuery()
    console.log("endhandleMetacriticList")
}

export const handleOpencriticList = () => {
    const opencritic_list = useOpencriticListQuery()
}

export const handleImdbList = () => {
    const imdb_list = useImdbListQuery()
}

export const handleMetacriticDetail = () => {
    const metacritic_detail = useMetacriticDetailQuery()
}

export const handleOpencriticDetail = () => {
    const opencritic_detail = useOpencriticDetailQuery()
}

export const handleImdbDetail = () => {
    const imdb_detail = useImdbDetailQuery()
}