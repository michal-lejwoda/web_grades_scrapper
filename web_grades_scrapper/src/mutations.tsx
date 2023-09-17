import {useMutation} from "react-query";
import {getListData} from "./api.tsx";

export const useGetListData = () => {
    return useMutation(getListData)
}