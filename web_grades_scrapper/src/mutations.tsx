import {useMutation} from "react-query";
import {getImdbDetailData, getListData, getMetacriticDetailData, getOpencriticDetailData} from "./api.tsx";

export const useGetListData = () => {
    return useMutation(getListData)
}

export const useGetOpencriticDetails = () => {
    return useMutation(getOpencriticDetailData)
}

export const useGetMetacriticDetails = () => {
    return useMutation(getMetacriticDetailData)
}

export const useGetImdbDetails = () => {
    return useMutation(getImdbDetailData)
}