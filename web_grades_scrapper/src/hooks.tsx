import {useQuery} from "react-query";
import {
    getImdbDetailData,
    getImdbListData,
    getMetacriticDetailData,
    getMetacriticListData, getOpencriticDetailData,
    getOpencriticListData
} from "./api.tsx";


export function useMetacriticListQuery() {
    return useQuery("metacritic_list", getMetacriticListData);
}

export function useOpencriticListQuery() {
    return useQuery("opencritic_list", getOpencriticListData);
}

export function useImdbListQuery() {
    return useQuery("imdb_list", getImdbListData);
}

export function useMetacriticDetailQuery() {
    return useQuery("metacritic_detail", getMetacriticDetailData);
}

export function useOpencriticDetailQuery() {
    return useQuery("opencritic_detail", getOpencriticDetailData);
}

export function useImdbDetailQuery() {
    return useQuery("imdb_detail", getImdbDetailData);
}